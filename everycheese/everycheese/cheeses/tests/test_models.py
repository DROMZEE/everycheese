import pytest

from ..models import Cheese

pytestmark = pytest.mark.django_db

def test__str__():
    cheese = Cheese.objects.create(
        name="Stracchino",
        description="Semi-sweet cheese that goes well with starches.",
        firmness=Cheese.FIRMNESS_SOFT,
    )
    assert cheese.__str__() == "Stracchino"