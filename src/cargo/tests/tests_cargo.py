from django.core.exceptions import ValidationError
from django.test import TestCase

from cargo.models import Cargo
from core.utils.samples import sample_cargo, sample_user_account


class TestCargoModel(TestCase):
    def setUp(self) -> None:
        self.user = sample_user_account()
        self.cargo = sample_cargo(self.user)
        self.user.cargos.set((self.cargo,))

    def tearDown(self) -> None:
        self.cargo.delete()

    def test_cascade_deletion(self):
        self.user.delete()
        with self.assertRaises(self.cargo.DoesNotExist):
            Cargo.objects.get()

    def test_cargo_type_limit(self):
        with self.assertRaises(ValidationError):
            sample_cargo(user=self.user, cargo_type="T" * 300)
