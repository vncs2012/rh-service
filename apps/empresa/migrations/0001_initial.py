# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nome', models.CharField(verbose_name='Empresa/Consultor', max_length=128)),
                ('email', models.EmailField(verbose_name='E-mail', max_length=128)),
                ('contato', models.CharField(verbose_name='Telefone de Contato', max_length=12)),
                ('status', models.BooleanField(verbose_name='Status', default=True)),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresa/Consultor',
            },
        ),
    ]
