# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CaracteristicasPersona',
            fields=[
                ('cd_caracteristica', models.AutoField(primary_key=True, editable=False, serialize=False)),
                ('no_caracteristica', models.CharField(verbose_name='Caracteristica ', max_length=100)),
                ('tp_caracteristica', models.IntegerField(verbose_name='Tipo ', choices=[(None, ''), (1, 'PERFECCIONISTA'), (2, 'PRESTATIVO'), (3, 'BEM-SUCEDIDO'), (4, 'ROMÂNTICO'), (5, 'OBSERVADOR'), (6, 'QUESTIONADOR'), (7, 'SONHADOR'), (8, 'CONFRONTADOR'), (9, 'PRESERVACIONISTA')])),
                ('tp_predominate', models.IntegerField(verbose_name='Predominante? ', choices=[(None, ''), (1, 'PADRÃO'), (2, 'PREDOMINANTE')])),
            ],
        ),
        migrations.CreateModel(
            name='PerguntaQuestionario',
            fields=[
                ('cd_per_questionario', models.AutoField(primary_key=True, editable=False, serialize=False)),
                ('nu_pergunta', models.CharField(verbose_name='Nº Pergunta', max_length=2)),
                ('ds_pergunta', models.CharField(verbose_name='Pergunta', max_length=250)),
                ('res_per_questionarioA', models.CharField(verbose_name='Alternativa (A)', max_length=100)),
                ('val_per_questionarioA', models.IntegerField(verbose_name='Tipo Resposta A', choices=[(None, ''), (1, 'PERFECCIONISTA'), (2, 'PRESTATIVO'), (3, 'BEM-SUCEDIDO'), (4, 'ROMÂNTICO'), (5, 'OBSERVADOR'), (6, 'QUESTIONADOR'), (7, 'SONHADOR'), (8, 'CONFRONTADOR'), (9, 'PRESERVACIONISTA')])),
                ('res_per_questionarioB', models.CharField(verbose_name='Alternativa (B)', max_length=100)),
                ('val_per_questionarioB', models.IntegerField(verbose_name='Tipo Resposta b', choices=[(None, ''), (1, 'PERFECCIONISTA'), (2, 'PRESTATIVO'), (3, 'BEM-SUCEDIDO'), (4, 'ROMÂNTICO'), (5, 'OBSERVADOR'), (6, 'QUESTIONADOR'), (7, 'SONHADOR'), (8, 'CONFRONTADOR'), (9, 'PRESERVACIONISTA')])),
            ],
        ),
        migrations.CreateModel(
            name='RelatorioProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('personalidade', models.TextField()),
                ('profisional', models.TextField()),
                ('caracteristicasPernonalidade', models.TextField()),
                ('infancia', models.TextField()),
                ('estadoInvolucao', models.TextField()),
                ('Asas', models.TextField()),
                ('tp_caracteristica', models.IntegerField(verbose_name='Tipo ', choices=[(None, ''), (1, 'PERFECCIONISTA'), (2, 'PRESTATIVO'), (3, 'BEM-SUCEDIDO'), (4, 'ROMÂNTICO'), (5, 'OBSERVADOR'), (6, 'QUESTIONADOR'), (7, 'SONHADOR'), (8, 'CONFRONTADOR'), (9, 'PRESERVACIONISTA')])),
            ],
            options={
                'verbose_name': 'Relatorio Profile',
                'verbose_name_plural': 'Relatorio Profiles',
            },
        ),
    ]
