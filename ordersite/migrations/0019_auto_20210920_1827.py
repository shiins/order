# Generated by Django 2.2.19 on 2021-09-20 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordersite', '0018_auto_20210908_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='メールアドレス',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='購入者',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='サイズ',
            field=models.CharField(blank=True, editable=False, max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='数量',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]