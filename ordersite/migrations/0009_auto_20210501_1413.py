# Generated by Django 2.2.19 on 2021-05-01 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordersite', '0008_remove_product_合計価格'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='products',
            field=models.ManyToManyField(to='ordersite.Product'),
        ),
        migrations.AddField(
            model_name='offer',
            name='合計金額',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='サイズ',
            field=models.CharField(blank=True, help_text='商品を登録する際は空白にしてください。', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='価格',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='数量',
            field=models.IntegerField(blank=True, help_text='商品を登録する際は空白にしてください。'),
        ),
    ]