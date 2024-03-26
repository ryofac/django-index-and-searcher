from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic.detail import DetailView

from buscador import utils
from buscador.forms import UpdateParamsForm
from buscador.indexer import Indexer
from buscador.models import Evaluation, Page
from buscador.searcher import Searcher


# Create your views here.
def indexer(request):
    return redirect(reverse("buscador:searcher_form_view"))


def searcher(request):
    if Page.objects.count() <= 0:
        messages.info(
            request,
            "Sem páginas disponíveis: uma indexação ocorrerá !",
        )
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


def update_config(request):
    if request.POST:
        post_dict = request.POST
        new_config = utils.get_config()
        for key in post_dict:
            if post_dict[key]:
                print(post_dict[key])
                new_key = None
                try:
                    new_key = int(post_dict[key])
                except ValueError:
                    new_key = post_dict[key]
                new_config[key] = new_key
        utils.update_json_config_file(new_config)
        return redirect(reverse("buscador:searcher_form_view"))
    actual_params = utils.get_config()
    form = UpdateParamsForm()
    return render(
        request,
        "buscador/components/update_config.html",
        {"form": form, "current_conf": actual_params},
    )


class EvaluationView(DetailView):
    model = Evaluation
    template_name = "buscador/components/evaluation.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["config"] = utils.get_config()
        if context["evaluation"].is_date_invalid:
            messages.error(
                self.request,
                f"A data dessa página está inválida, por isso seu frescor recebe -{utils.get_config()['invalid_date_penalty']} pontos",
            )
        if context["evaluation"].is_auto_reference:
            messages.error(
                self.request,
                f"Essa página é auto referenciada, por isso recebe uma penalidade de {utils.get_config()['auto_reference_penalty']} pontos",
            )
        return context
