from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
on_sale = (
    (True, '上架'),
    (False, '下架')
)


# 删除和创建修改时间的基础模型
class BasicsModel(models.Model):
    is_delete = models.BooleanField(default=False, verbose_name='删除')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        # 设置为抽象类,不会被迁移
        abstract = True


# 商品分类表
class GoodsClassifyModel(BasicsModel):
    class_name = models.CharField(max_length=50, verbose_name='分类名称')
    class_intro = models.CharField(max_length=50, verbose_name='分类简介', null=True)

    def __str__(self):
        return self.class_name

    class Meta:
        db_table = 'goods_classify'
        verbose_name = '商品分类表'
        verbose_name_plural = verbose_name


# 商品SKU表
class GoodsSkuModel(BasicsModel):
    goods_name = models.CharField(max_length=200, verbose_name='商品名称')
    goods_intro = models.TextField(verbose_name='商品信息')
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0, verbose_name='商品价格')
    unitinfo = models.ForeignKey(to='GoodsUnitModel', verbose_name='商品单位')
    num = models.PositiveIntegerField(verbose_name='商品库存')
    sell_num = models.PositiveIntegerField(verbose_name='商品销售量')
    logo = models.ImageField(upload_to='logo/%Y%m', verbose_name='商品图片')
    is_putaway = models.BooleanField(choices=on_sale, default=False, verbose_name='商品是否上架')
    goods_cate = models.ForeignKey(to='GoodsClassifyModel', verbose_name='商品分类')
    goods_spu = models.ForeignKey(to='SpuModel', verbose_name='商品spu分类')

    def __str__(self):
        return self.goods_name

    class Meta:
        db_table = 'goods_sku'
        verbose_name = '商品SKU表'
        verbose_name_plural = verbose_name


# 商品单位表
class GoodsUnitModel(BasicsModel):
    unit_name = models.CharField(max_length=50, verbose_name='单位名称')

    def __str__(self):
        return self.unit_name

    class Meta:
        db_table = 'goods_unit'
        verbose_name = '商品单位表'
        verbose_name_plural = verbose_name


# 商品spu表
class SpuModel(BasicsModel):
    spu_name = models.CharField(max_length=50, verbose_name='商品spu名称')
    spu_desc = RichTextUploadingField(verbose_name='商品spu描述')

    def __str__(self):
        return self.spu_name

    class Meta:
        db_table = 'goods_spu'
        verbose_name = '商品SPU表'
        verbose_name_plural = verbose_name


# 商品相册表
class GoodsAlbumModel(BasicsModel):
    album_image = models.ImageField(upload_to='album', verbose_name='商品图片地址')
    album_sku = models.ForeignKey(to='GoodsSkuModel', verbose_name='商品sku的ID')

    def __str__(self):
        return '商品相册'

    class Meta:
        db_table = 'goods_categories'
        verbose_name = '商品相册表'
        verbose_name_plural = verbose_name


# 首页轮播
class BannerModel(BasicsModel):
    banner_name = models.CharField(max_length=200, verbose_name='轮播活动名')
    banner_sku = models.ForeignKey(to='GoodsSkuModel', verbose_name='商品sku')
    banner_image = models.ImageField(upload_to='banner/%Y%m/%d', verbose_name='轮播图片地址')
    order = models.SmallIntegerField(default=0, verbose_name='排序')

    def __str__(self):
        return self.banner_name

    class Meta:
        db_table = 'banner'
        verbose_name = '首页轮播管理'
        verbose_name_plural = verbose_name


# 首页活动表
class ActivityModel(BasicsModel):
    title = models.CharField(max_length=200, verbose_name='活动名称')
    activity_image = models.ImageField(upload_to='activity/%Y%m/%d', verbose_name='活动图片地址')
    url = models.URLField(max_length=200, verbose_name='活动url地址')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'activity'
        verbose_name = '活动管理'
        verbose_name_plural = verbose_name


# 首页活动专区
class ActivityZoneModel(BasicsModel):
    title = models.CharField(max_length=200, verbose_name='活动专区名')
    brief = models.CharField(verbose_name="活动专区的简介",
                             max_length=200,
                             null=True,
                             blank=True,
                             )
    order = models.SmallIntegerField(verbose_name="排序",
                                     default=0,
                                     )
    is_on_sale = models.BooleanField(verbose_name="上否上线",
                                     choices=on_sale,
                                     default=0,
                                     )
    goods_sku = models.ForeignKey(to="GoodsSkuModel", verbose_name="商品")

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'activity_zone'
        verbose_name = "活动专区管理"
        verbose_name_plural = verbose_name

