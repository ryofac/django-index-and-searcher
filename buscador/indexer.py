import re
from datetime import datetime

import requests
from bs4 import BeautifulSoup

from buscador.models import Evaluation, ExternalLink, Page
from buscador.utils import multiplyers


class Indexer:
    def index(
        self,
        url: str = "https://meidesu.github.io/movies-pages/matrix.html",
    ) -> None:
        print("Indexando: ", url)
        # index.html; 1.html 2.html | 1.html -> 3html?
        response_from_page = requests.get(url)
        page_content = response_from_page.content
        soup = BeautifulSoup(page_content, "html.parser")
        page_evaluation = Evaluation()
        page_body = soup.find("body").text
        # Título da página a ser criada
        page_title = soup.find("title").text
        anchor_tags = soup.find_all("a")

        page_links: list[str] = []
        for a in anchor_tags:
            page_links.append(a.get("href"))

        if url in page_links:
            page_evaluation.auto_reference_penalty = multiplyers[
                "auto_reference_penalty"
            ]

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
            self.index(link)
        new_page.save()

    def get_page_date(self, content: str):
        date_regex = re.compile(r"\d{2}\/\d{2}\/\d{4}")
        dates_finded = date_regex.findall(content)
        if len(dates_finded) <= 0:
            return None
        date_str = dates_finded[0]
        try:
            date = datetime.strptime(date_str, "%d/%m/%Y")
            return date
        # Se isso ocorrer, significa que a data está inválida
        except ValueError:
            return None

    def atribute_autority_points(self):
        for page in Page.objects.all():
            for link in page.external_links.all():
                page_found = Page.objects.get(index=link.url)
                if link.url == page.index:
                    continue

                page_found.evaluation.autority_points += multiplyers["autority"]
                page_found.evaluation.save()
