from typing import TypedDict


class Multiplyers(TypedDict):
    autority: float
    occurrency: float
    meta: float
    h1: float
    h2: float
    p: float
    a: float
    fresh_content: float
    fresh_content_penalty: float
    auto_reference_penalty: float
    # criando penalidade para datas inválidas
    invalid_date_penalty: float
