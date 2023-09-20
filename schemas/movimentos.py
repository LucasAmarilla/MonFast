def movimentoEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "tipo": item["tipo"],
        "valor": item["valor"],
        "desc": item["desc"],
        "caixa": item["caixa"],
        "usr": item["usr"]
    }


def movimentosEntity(entity) -> list:
    return [movimentoEntity(item)for item in entity]
