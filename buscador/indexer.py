import re
from datetime import datetime

import requests
from bs4 import BeautifulSoup

from buscador import utils
from buscador.models import Evaluation, ExternalLink, Page


class Indexer:
    def index(
        self,
        url: str = utils.get_config()["index_start_point"],
        depth=0,
        max_depth=utils.get_config()["max_depth_search"],
    ) -> None:
        print("Tentando indexar: " + url)
        if depth > max_depth:
            return
        # index.html; 1.html 2.html | 1.html -> 3html?
        try:
            url = url.lower().strip()
            response_from_page = requests.get(url)
            page_content = response_from_page.content
            soup = None
            try:
                soup = BeautifulSoup(page_content, "html.parser")
            except Exception:
                print("Beautiful soap não conseguiu pegar")
                return
            page_evaluation = Evaluation()
            page_body = soup.find("body").text
            # Título da página a ser criada
            page_title = soup.find("title").text
            anchor_tags = soup.find_all("a")

            page_links: list[str] = []

            _count = 0
            for a in anchor_tags:
                if _count > utils.get_config()["max_links_per_search"]:
                    break
                if utils.get_config()["is_domain_especifc"]:
                    regexHtpp = re.compile(
                        rf"{re.escape(utils.get_config()['index_start_point'])}.*"
                    )
                else:
                    regexHtpp = re.compile(r"\bhttps://\S+\b")

                link = a.get("href")
                if not link:
                    continue
                if regexHtpp.match(link):
                    page_links.append(link)
                    _count += 1

            if url in page_links:
                print("URL CHEGANDO", url)
                page_evaluation.auto_reference_penalty = utils.get_config()[
                    "auto_reference_penalty"
                ]
                page_evaluation.is_auto_reference = True

            page_date = self.get_page_date(page_body)
            page_evaluation.fresh_evaluation(page_date)

            page_evaluation.save()
            new_page = Page.objects.create(
                content=page_content.decode("UTF-8"),
                title=page_title,
                evaluation=page_evaluation,
                date=page_date,
                index=url,
            )
            for link in page_links:
                new_page.external_links.add(ExternalLink.objects.create(url=link))
                if Page.objects.filter(index=link).exists():
                    continue
                self.index(link, depth + 1, max_depth)
            new_page.save()
        except Exception as e:
            print("Erro indexando url: " + url)
            if hasattr(e, "message"):
                print(e.message, "SKIPANDO")
            else:
                print(e)

    def get_page_date(self, content: str):
        date_regex = re.compile(r"\d{2}\/\d{2}\/\d{4}")
        dates_found = date_regex.findall(content)
        if len(dates_found) <= 0:
            return None
        date_str = dates_found[0]
        try:
            date = datetime.strptime(date_str, "%d/%m/%Y")
            return date
        # Se isso ocorrer, significa que a data está inválida
        except ValueError:
            return None

    def atribute_autority_points(self):
        for page in Page.objects.all():
            for link in page.external_links.all():
                try:
                    page_found = Page.objects.get(index=link.url)
                    if link.url == page.index:
                        continue
                    page_found.evaluation.autority_points += utils.get_config()[
                        "autority"
                    ]
                    page_found.evaluation.save()
                except Exception:
                    print("URL sem pontuação - não relacionou com nenhuma: skipando")
