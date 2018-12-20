import pytest

from . import PROT

def test_basic_case():
    rna_in = "AUGUUCAAG"
    protein_out = "MFK"
    assert protein_out == PROT.rna_to_pro(rna_in)

def test_mixed_case():
    rna_in = "auGUUCAAG"
    protein_out = "MFK"
    assert protein_out == PROT.rna_to_pro(rna_in)

def test_two_stops():
    rna_in = "AUGUAGUUCAAGUAA"
    protein_out = "M"
    assert protein_out == PROT.rna_to_pro(rna_in)

def test_non_triplet_sequence():
    rna_in = "AUGUUCAA" # 8 bases in input
    with pytest.raises(AssertionError):
        PROT.rna_to_pro(rna_in)

def test_non_base():
    rna_in = "ANGUUCAAG"
    with pytest.raises(Exception) as custom_error:
        PROT.rna_to_pro(rna_in)
    assert "non-base" in str(custom_error)