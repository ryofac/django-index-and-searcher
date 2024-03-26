from django import forms


class UpdateParamsForm(forms.Form):
    index_start_point = forms.URLField(
        label="Início personalizado da indexação", required=False
    )
    max_links_per_search = forms.IntegerField(
        label="Quantidade de links buscados em cada página", required=False
    )

    max_depth_search = forms.IntegerField(
        label="Qual a profundidade máxima da busca?", required=False
    )
    autority = forms.FloatField(label="Multiplicador de Autoridade", required=False)
    occurrency = forms.FloatField(label="Multiplicador de Ocorrência", required=False)
    meta = forms.FloatField(
        label="Multiplicador em meta tags/ tags title", required=False
    )
    h1 = forms.FloatField(label="Multiplicador em tags h1", required=False)
    h2 = forms.FloatField(label="Multiplicador em tags h2", required=False)
    p = forms.FloatField(label="Multiplicador em tags p", required=False)
    a = forms.FloatField(label="Multiplicador em tags a", required=False)
    fresh_content = forms.FloatField(
        label="Multiplicador de Frescor da Página", required=False
    )
    fresh_content_penalty = forms.FloatField(
        label="Penalização de Frescor da Página", required=False
    )
    auto_reference_penalty = forms.FloatField(
        label="Penalização de auto referência", required=False
    )
    # criando penalidade para datas inválidas
    invalid_date_penalty = forms.FloatField(
        label="Valor de data inválida", required=False
    )

    is_domain_especific = forms.BooleanField(
        label="Busca por páginas pelo prefixo da página inicial"
    )
