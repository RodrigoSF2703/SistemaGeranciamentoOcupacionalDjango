# Generated by Django 3.2.16 on 2022-11-17 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atendimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_atendimento', models.DateField()),
                ('trabalhoaltura', models.BooleanField()),
                ('espacoconfinado', models.BooleanField()),
                ('apto', models.BooleanField()),
            ],
            options={
                'db_table': 'atendimento',
            },
        ),
        migrations.CreateModel(
            name='Coordenador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('crm', models.CharField(max_length=10)),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'coordenador',
            },
        ),
        migrations.CreateModel(
            name='Exame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('validade', models.IntegerField()),
            ],
            options={
                'db_table': 'exame',
            },
        ),
        migrations.CreateModel(
            name='Funcao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'funcao',
            },
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'grupo',
            },
        ),
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'setor',
            },
        ),
        migrations.CreateModel(
            name='TipoExame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'tipoexame',
            },
        ),
        migrations.CreateModel(
            name='TipoRisco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'tiporisco',
            },
        ),
        migrations.CreateModel(
            name='Risco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('tiporisco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tiporisco')),
            ],
            options={
                'db_table': 'risco',
            },
        ),
        migrations.CreateModel(
            name='GrupoRisco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.grupo')),
                ('risco', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.risco')),
            ],
            options={
                'db_table': 'gruporisco',
            },
        ),
        migrations.CreateModel(
            name='GrupoFuncao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('funcao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.funcao')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.grupo')),
                ('setor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.setor')),
            ],
            options={
                'db_table': 'grupofuncao',
            },
        ),
        migrations.CreateModel(
            name='GrupoExame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exame', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.exame')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.grupo')),
                ('tipoexame', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.tipoexame')),
            ],
            options={
                'db_table': 'grupoexame',
            },
        ),
        migrations.CreateModel(
            name='Empregado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('cpf', models.CharField(max_length=15)),
                ('ctps', models.CharField(max_length=20)),
                ('serie', models.CharField(max_length=10)),
                ('data_nascimento', models.DateField()),
                ('data_admissao', models.DateField()),
                ('data_demissao', models.DateField(blank=True, null=True)),
                ('funcao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.funcao')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.grupo')),
                ('setor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.setor')),
            ],
            options={
                'db_table': 'empregado',
            },
        ),
        migrations.CreateModel(
            name='AtendimentoRisco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atendimento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.atendimento')),
                ('risco', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.risco')),
            ],
            options={
                'db_table': 'atendimentorisco',
            },
        ),
        migrations.CreateModel(
            name='AtendimentoExame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atendimento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.atendimento')),
                ('exame', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.exame')),
            ],
            options={
                'db_table': 'atendimentoexame',
            },
        ),
        migrations.AddField(
            model_name='atendimento',
            name='coordenador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.coordenador'),
        ),
        migrations.AddField(
            model_name='atendimento',
            name='empregado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.empregado'),
        ),
        migrations.AddField(
            model_name='atendimento',
            name='funcao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.funcao'),
        ),
        migrations.AddField(
            model_name='atendimento',
            name='grupo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.grupo'),
        ),
        migrations.AddField(
            model_name='atendimento',
            name='setor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.setor'),
        ),
        migrations.AddField(
            model_name='atendimento',
            name='tipoexame',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.tipoexame'),
        ),
    ]