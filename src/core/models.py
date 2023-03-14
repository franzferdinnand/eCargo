from django.db import models


class Transaction(models.Model):
    transport = models.ForeignKey(to="transport.Transport", on_delete=models.CASCADE, related_name="transactions")
    cargo = models.ForeignKey(to="cargo.Cargo", on_delete=models.CASCADE, related_name="transactions")
