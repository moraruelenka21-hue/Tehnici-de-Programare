"""Teste pentru numărarea eșecurilor și validarea pragului."""

import pytest

from arsenal.aparare.detector import suspecti
from arsenal.aparare.parse_auth import pe_ip


def test_numararea_si_pragul():
    esecuri = [
        {"user": "ana", "ip": "198.51.100.7"},
        {"user": "root", "ip": "203.0.113.9"},
        {"user": "admin", "ip": "203.0.113.9"},
    ]

    counts = pe_ip(esecuri)

    assert counts == {"203.0.113.9": 2, "198.51.100.7": 1}
    assert suspecti(counts) == []
    assert suspecti(counts, 2) == [("203.0.113.9", 2)]
    assert suspecti(counts, 1) == [("203.0.113.9", 2), ("198.51.100.7", 1)]


def test_prag_invalid():
    with pytest.raises(ValueError, match=r"^prag invalid: 0 \(cel putin 1\)$"):
        suspecti({}, 0)
