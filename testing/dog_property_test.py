from dog import Dog
import pytest

class TestDogProperties:
    def test_name_breed_valid(self):
        try:
            dog = Dog("Fido", "Corgi")
        except Exception as exc:
            assert False, f'Dog("Fido", "Corgi") raised an exception {exc}'

    def test_name_is_string_valid_length(self):
        dog = Dog("Fido", "Corgi")
        with pytest.raises(ValueError):
            dog.name = 7  # not a string
        with pytest.raises(ValueError):
            dog.name = ''  # too short
        with pytest.raises(ValueError):
            dog.name = 'Fido the adorable Corgi who likes to steal socks'  # too long

    def test_breed_is_approved_breed(self):
        dog = Dog("Snoopy", "Beagle")
        with pytest.raises(ValueError):
            dog.breed = "Poodle"  # not an approved breed
