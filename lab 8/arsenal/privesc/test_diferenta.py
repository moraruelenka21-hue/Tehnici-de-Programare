"""Regresie: verifica functia proiectului, nu doar operatorul Python."""
from arsenal.privesc.diferenta import compara


def test_doar_ce_e_nou():
    acum = {"a", "b", "c"}
    baza = {"a", "b"}
    assert acum - baza == {"c"}
    assert compara(baza, acum)["noi"] == ["c"]
