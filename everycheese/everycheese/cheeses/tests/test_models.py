import pytest

from ..models import Cheese
from .factories import CheeseFactory

pytestmark = pytest.mark.django_db

def test___str__():
    cheese = Cheese.objects.create(
        name="Stracchino",
        description="Semi-sweet cheese that goes well with starches.",
        #firmness=Cheese.FIRMNESS_SOFT,
        firmness=Cheese.Firmness.soft,
    )
    assert cheese.__str__() == "Stracchino"


def test___str__(self):
    cheese = CheeseFactory()
    self.assertEqual(cheese.__str__(), cheese.name)