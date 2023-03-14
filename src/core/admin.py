from django.contrib import admin

from account.models import UserAccount
from cargo.models import Cargo
from core.models import Transaction
from transport.models import Transport

admin.site.register([Cargo, Transport, Transaction])
