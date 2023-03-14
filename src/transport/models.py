from django.contrib.auth import get_user_model
from django.db import models


class Transport(models.Model):
    car_name = models.CharField(max_length=120, null=False)
    car_model = models.CharField(max_length=120, null=False)
    max_weight = models.PositiveIntegerField(null=False)
    owner = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE, related_name="transports")
