import re

from bs4 import BeautifulSoup

from buscador.models import Page
from buscador.utils import multiplyers


class Searcher:
    def search(self, search_term: str) -> list[Page]:
        self._clean_values()
        self._search_occurencies(search_term)
        return self._get_filter_results()

    def _get_filter_results(self):
        all_pages = Page.objects.all()
        filtered_pages = []
        for page in all_pages:
            # Pegando as páginas que contém o termo buscado
            if page.evaluation.frequency_points > 0:
                filtered_pages.append(page)
        # Ordenar por pontuação
        filtered_pages.sort(
            key=lambda page: page.evaluation.get_total_points(), reverse=True
        )
        return filtered_pages

    def _search_occurencies(self, search_term: str):
        pages = Page.objects.all()
        for page in pages:
            tags = (
                "h1",
                "h2",
                "p",
                "a",
            )
            for tag in tags:
                occurrencies = self._get_ocurrencies(
                    tag,
                    page.content,
                    search_term,
                )
                page.evaluation.frequency_points += (
                    occurrencies * multiplyers["occurrency"]
                )
                print(f"Tag: {tag}, ocorrências: {occurrencies}; página {page.title}")
                page.evaluation.tags_points += occurrencies * multiplyers[tag]
                page.evaluation.save()

    def _get_ocurrencies(self, html_tag: str, content: str, search_term: str):
        regex = re.compile(search_term, re.IGNORECASE)
        soap = BeautifulSoup(content, "html.parser")
        elements = soap.find_all(html_tag)
        times_matched = 0
        for element in elements:
            times_matched += len(regex.findall(element.text))
        return times_matched

    def _clean_values(self):
        pages = Page.objects.all()
        for page in pages:
            page.evaluation.tags_points = 0.0
            page.evaluation.frequency_points = 0.0
            page.evaluation.save()
