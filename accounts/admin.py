from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import RegisterForm
from .models import InvestorUser


class InvestorUserAdmin(UserAdmin):
    add_form = RegisterForm
    model = InvestorUser
    list_display = ['username', 'email']


admin.site.register(InvestorUser, InvestorUserAdmin)

