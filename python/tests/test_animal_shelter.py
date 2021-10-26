import pytest

from code_challenges.animal_shelter.animal_shelter import Animal,Animal_Shelter,Dog,Cat

def test_enqueue_one_animal_dog_type():
    pomeranian=Dog('pomeranian')
    new_animal=Animal_Shelter()
    new_animal.enqueue(pomeranian)
    assert new_animal.front.value.pref =="Dog"

def test_enqueue_one_animal_cat_type():
    bondoq=Cat('bondoq')
    new_animal=Animal_Shelter()
    new_animal.enqueue(bondoq)
    assert new_animal.front.value.pref =="Cat"

def test_dequeue_an_empty_queue():
    animal2=Animal_Shelter()
    with pytest.raises(Exception):
        animal2.dequeue()


