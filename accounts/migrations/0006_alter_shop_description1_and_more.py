# Generated by Django 5.0.2 on 2024-02-21 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_shop_photo1_alter_shop_photo2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='description1',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='shop',
            name='description_block1_2',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='shop',
            name='description_block1_4',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='shop',
            name='description_block2_2',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='shop',
            name='description_block2_4',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='shop',
            name='description_block3',
            field=models.TextField(),
        ),
    ]
