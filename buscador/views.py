from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse

from buscador.indexer import Indexer
from buscador.models import Evaluation, Page
from buscador.searcher import Searcher


# Create your views here.
def indexer(request):
    return redirect(reverse("buscador:searcher_form_view"))


def searcher(request):
    return render(request, "buscador/components/searcher_form.html")


def clear_indexer(request):
    if Page.objects.count() > 0:
        Page.objects.all().delete()
        Evaluation.objects.all().delete()
    else:
        messages.error(request, "Páginas ainda não indexadas")
    return redirect(reverse("buscador:searcher_form_view"))


def results(request):
    if Page.objects.count() <= 0:
        indexer = Indexer()
        indexer.index()
        indexer.atribute_autority_points()
    search_term = request.GET.get("termo", None)
    searcher = Searcher()
    pages = searcher.search(search_term)
    return render(
        request,
        "buscador/components/results.html",
        {"pages": pages, "search_term": search_term},
    )
