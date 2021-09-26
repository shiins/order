# Generated by Django 2.2.19 on 2021-05-01 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordersite', '0013_offer_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='products',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='purchased_products',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='合計金額',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='名前',
        ),
        migrations.AddField(
            model_name='offer',
            name='サイズ',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='メールアドレス',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='価格',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='品名',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='品番',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='小計',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='数量',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='購入者',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
