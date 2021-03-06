# Generated by Django 2.0 on 2017-12-12 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Split',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('amount', models.FloatField()),
                ('op', models.CharField(choices=[('C', 'CREDIT'), ('D', 'DEBIT')], max_length=1)),
                ('is_reconciled', models.BooleanField(default=False)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.Account')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('tdate', models.DateField()),
                ('ttype', models.CharField(choices=[('INC', 'Income'), ('EXP', 'Expense')], default='EXP', max_length=3)),
                ('other_party', models.CharField(max_length=50)),
                ('amount', models.FloatField()),
                ('categories', models.CharField(max_length=128)),
                ('is_reconciled', models.BooleanField(default=False)),
                ('recurrent', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='split',
            name='transaction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.Transaction'),
        ),
        migrations.AddField(
            model_name='account',
            name='transactions',
            field=models.ManyToManyField(through='finance.Split', to='finance.Transaction'),
        ),
    ]
