# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-23 07:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsAlbumModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('album_image', models.ImageField(upload_to='album', verbose_name='商品图片地址')),
            ],
            options={
                'verbose_name': '商品相册表',
                'verbose_name_plural': '商品相册表',
                'db_table': 'goods_categories',
            },
        ),
        migrations.CreateModel(
            name='GoodsClassifyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('class_name', models.CharField(max_length=50, verbose_name='分类名称')),
                ('class_intro', models.CharField(max_length=50, null=True, verbose_name='分类简介')),
            ],
            options={
                'verbose_name': '商品分类表',
                'verbose_name_plural': '商品分类表',
                'db_table': 'goods_classify',
            },
        ),
        migrations.CreateModel(
            name='GoodsSkuModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('goods_name', models.CharField(max_length=200, verbose_name='商品名称')),
                ('goods_intro', models.TextField(verbose_name='商品信息')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='商品价格')),
                ('num', models.PositiveIntegerField(verbose_name='商品库存')),
                ('sell_num', models.PositiveIntegerField(verbose_name='商品销售量')),
                ('logo', models.ImageField(upload_to='logo/%Y%m', verbose_name='商品图片')),
                ('is_putaway', models.BooleanField(default=False, verbose_name='商品是否上架')),
                ('goods_cate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commodity.GoodsClassifyModel', verbose_name='商品分类')),
            ],
            options={
                'verbose_name': '商品SKU表',
                'verbose_name_plural': '商品SKU表',
                'db_table': 'goods_sku',
            },
        ),
        migrations.CreateModel(
            name='GoodsUnitModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('unit_name', models.CharField(max_length=50, verbose_name='单位名称')),
            ],
            options={
                'verbose_name': '商品单位表',
                'verbose_name_plural': '商品单位表',
                'db_table': 'goods_unit',
            },
        ),
        migrations.CreateModel(
            name='SpuModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('spu_name', models.CharField(max_length=50, verbose_name='商品spu名称')),
                ('spu_desc', models.TextField(verbose_name='商品spu描述')),
            ],
            options={
                'verbose_name': '商品SPU表',
                'verbose_name_plural': '商品SPU表',
                'db_table': 'goods_spu',
            },
        ),
        migrations.AddField(
            model_name='goodsskumodel',
            name='goods_spu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commodity.SpuModel', verbose_name='商品spu分类'),
        ),
        migrations.AddField(
            model_name='goodsskumodel',
            name='unitinfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commodity.GoodsUnitModel', verbose_name='商品单位'),
        ),
        migrations.AddField(
            model_name='goodsalbummodel',
            name='album_sku',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commodity.GoodsSkuModel', verbose_name='商品sku的ID'),
        ),
    ]