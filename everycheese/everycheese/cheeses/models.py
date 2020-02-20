from django.db import models
from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel

class Cheese(TimeStampedModel):

    FIRMNESS_UNSPECIFIED = "unspecified"
    FIRMNESS_SOFT = "soft"
    FIRMNESS_SEMI_SOFT = "semi-soft"
    FIRMNESS_SEMI_HARD = "semi-hard"
    FIRMNESS_HARD = "hard"
    FIRMNESS_CHOICES = (
        (FIRMNESS_UNSPECIFIED, "Unspecified"),
        (FIRMNESS_SOFT, "Soft"),
        (FIRMNESS_SEMI_SOFT, "Semi-Soft"),
        (FIRMNESS_SEMI_HARD, "Semi-Hard"),
        (FIRMNESS_HARD, "Hard"),
        )

    name = models.CharField("Name of Cheese", max_length=255)
    slug = AutoSlugField("Cheese Address",
        unique=True, always_update=False, populate_from="name")

    description = models.TextField("Description", blank=True)

    firmness = models.CharField("Firmness", max_length=20,
        choices=FIRMNESS_CHOICES, default=FIRMNESS_UNSPECIFIED)
    
    def __str__(self):
        return self.name