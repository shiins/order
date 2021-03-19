# Generated by Django 2.2.19 on 2021-03-13 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('品名', models.CharField(max_length=20)),
                ('品番', models.CharField(max_length=20)),
                ('価格', models.IntegerField(default=10000)),
                ('合計価格', models.IntegerField()),
                ('サイズ', models.CharField(max_length=20)),
                ('着数', models.IntegerField()),
            ],
        ),
    ]
