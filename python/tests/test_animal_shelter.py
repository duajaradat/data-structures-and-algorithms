import pytest

from code_challenges.animal_shelter.animal_shelter import Animal,Animal_Shelter

def test_enqueue_one_animal():
    new_animal=Animal_Shelter()
    new_animal.enqueue("Pomeranian")
    assert new_animal.front.value =="Pomeranian"
