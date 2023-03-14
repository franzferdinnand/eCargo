from django.contrib.auth import get_user_model
from django.db import models


class Cargo(models.Model):
    cargo_type = models.CharField(max_length=200, null=False)
    weight_kg = models.PositiveIntegerField(null=False)
    destination_from = models.CharField(max_length=120, null=False)
    destination_to = models.CharField(max_length=120, null=False)
    owner = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE, null=True, related_name="cargos")

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
