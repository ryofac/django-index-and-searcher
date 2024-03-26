from django.urls import path

from buscador import views

app_name = "buscador"

urlpatterns = [
    path("", views.searcher, name="searcher_form_view"),
    path("index/", views.indexer, name="indexer_view"),
    path("index/delete/", views.clear_indexer, name="clean_indexer_view"),
    path("results/", views.results, name="results"),
    path("evaluation/<pk>/", views.EvaluationView.as_view(), name="evaluation_view"),
    path("config/update/", views.update_config, name="update_config"),
]
