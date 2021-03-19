# Generated by Django 2.2.19 on 2021-03-13 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordersite', '0003_product_published_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='published_date',
        ),
        migrations.AddField(
            model_name='product',
            name='sizes',
            field=models.ManyToManyField(to='ordersite.Size'),
        ),
    ]