# Generated by Django 2.2.3 on 2020-04-20 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djmoney.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Metal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bought_price_currency', djmoney.models.fields.CurrencyField(choices=[('USD', 'USD $'), ('EUR', 'EUR €'), ('PLN', 'PLN ZŁ'), ('CHF', 'CHF +')], default='PLN', editable=False, max_length=3)),
                ('bought_price', djmoney.models.fields.MoneyField(currency_choices=[('USD', 'USD $'), ('EUR', 'EUR €'), ('PLN', 'PLN ZŁ'), ('CHF', 'CHF +')], decimal_places=2, default_currency='PLN', max_digits=10)),
                ('date_of_bought', models.DateTimeField()),
                ('name', models.CharField(choices=[('silver', 'Silver'), ('gold', 'Gold')], default='Ag', max_length=10)),
                ('unit', models.CharField(choices=[('oz', 'ounce'), ('g', 'gram'), ('kg', 'kilogram')], default='oz', max_length=10)),
                ('amount', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('description', models.TextField(blank=True, help_text='Type some information about this transaction (optional)')),
                ('owner', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bought_price_currency', djmoney.models.fields.CurrencyField(choices=[('USD', 'USD $'), ('EUR', 'EUR €'), ('PLN', 'PLN ZŁ'), ('CHF', 'CHF +')], default='PLN', editable=False, max_length=3)),
                ('bought_price', djmoney.models.fields.MoneyField(currency_choices=[('USD', 'USD $'), ('EUR', 'EUR €'), ('PLN', 'PLN ZŁ'), ('CHF', 'CHF +')], decimal_places=2, default_currency='PLN', max_digits=10)),
                ('date_of_bought', models.DateTimeField()),
                ('bought_currency_currency', djmoney.models.fields.CurrencyField(choices=[('USD', 'USD $'), ('EUR', 'EUR €'), ('PLN', 'PLN ZŁ'), ('CHF', 'CHF +')], default='CHF', editable=False, max_length=3)),
                ('bought_currency', djmoney.models.fields.MoneyField(blank=True, currency_choices=[('USD', 'USD $'), ('EUR', 'EUR €'), ('PLN', 'PLN ZŁ'), ('CHF', 'CHF +')], decimal_places=2, default_currency='CHF', max_digits=10, null=True)),
                ('owner', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('save_date', models.DateTimeField()),
                ('my_cash_currency', djmoney.models.fields.CurrencyField(choices=[('USD', 'USD $'), ('EUR', 'EUR €'), ('PLN', 'PLN ZŁ'), ('CHF', 'CHF +')], default='PLN', editable=False, max_length=3)),
                ('my_cash', djmoney.models.fields.MoneyField(blank=True, currency_choices=[('USD', 'USD $'), ('EUR', 'EUR €'), ('PLN', 'PLN ZŁ'), ('CHF', 'CHF +')], decimal_places=2, default_currency='PLN', max_digits=10, null=True)),
                ('owner', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
