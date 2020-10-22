# Generated by Django 3.1.2 on 2020-10-21 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20201020_0144'),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titile', models.CharField(max_length=200)),
                ('descTitle', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('pageLink', models.URLField()),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('S', 'Man Shirt'), ('SW', 'Sport Wear'), ('OW', 'Outwear')], max_length=2),
        ),
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('P', 'primary'), ('S', 'secondary'), ('D', 'danger')], max_length=2),
        ),
    ]
