# Generated by Django 4.2 on 2023-04-04 01:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historyprice',
            options={'verbose_name': '历史价格', 'verbose_name_plural': '历史价格'},
        ),
        migrations.AlterModelOptions(
            name='info',
            options={'verbose_name': '市场资讯', 'verbose_name_plural': '市场资讯'},
        ),
        migrations.AlterModelOptions(
            name='originprice',
            options={'verbose_name': '产地价格', 'verbose_name_plural': '产地价格'},
        ),
        migrations.AlterModelOptions(
            name='originstatistics',
            options={'verbose_name': '供应产地', 'verbose_name_plural': '供应产地'},
        ),
        migrations.AlterModelOptions(
            name='prescript',
            options={'verbose_name': '药方信息', 'verbose_name_plural': '药方信息'},
        ),
        migrations.AlterModelTable(
            name='historyprice',
            table='historyprice',
        ),
        migrations.AlterModelTable(
            name='info',
            table='info',
        ),
        migrations.AlterModelTable(
            name='originprice',
            table='originprice',
        ),
        migrations.AlterModelTable(
            name='originstatistics',
            table='originstatistics',
        ),
        migrations.AlterModelTable(
            name='prescript',
            table='prescript',
        ),
    ]
