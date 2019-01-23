from django.contrib import admin
from commodity.models import GoodsSkuModel, GoodsUnitModel, GoodsClassifyModel, SpuModel, GoodsAlbumModel, BannerModel, \
    ActivityModel, ActivityZoneModel


# Register your models here.

# admin.site.register(GoodsClassifyModel)
# 商品sku
class GoodsAlbumModelInline(admin.TabularInline):
    model = GoodsAlbumModel
    extra = 2


@admin.register(GoodsSkuModel)
class GoodsSkuModelAdmin(admin.ModelAdmin):
    list_display = ["id", 'goods_name', 'price', 'unitinfo', 'num', 'sell_num', 'is_putaway', 'goods_spu']
    list_display_links = ["id", 'goods_name', 'price']

    search_fields = ['goods_name', 'price', 'sell_num']
    inlines = [
        GoodsAlbumModelInline,
    ]


admin.site.register(GoodsUnitModel)
# @admin.register(GoodsUnitModel)
# class GoodsUnitModelAdmin(admin.ModelAdmin):
#     list_per_page = 5
#     actions_on_top = False
#     actions_on_bottom = True
#     list_display = ['unit_name']


@admin.register(GoodsClassifyModel)
class GoodsClassifyModelAdmin(admin.ModelAdmin):
    # 自定义后台
    list_display = ['id', 'class_name', 'class_intro', 'update_time']
    list_display_links = ['id', 'class_name', 'class_intro']


admin.site.register(SpuModel)
# @admin.register(SpuModel)
# class SpuModelAdmin(admin.ModelAdmin):
#     list_per_page = 5
#     actions_on_top = False
#     actions_on_bottom = True


@admin.register(GoodsAlbumModel)
class GoodsAlbumModel(admin.ModelAdmin):
    list_per_page = 5
    actions_on_top = False
    actions_on_bottom = True


# 首页管理
admin.site.register(BannerModel)
admin.site.register(ActivityModel)


@admin.register(ActivityZoneModel)
class ActivityZoneModel(admin.ModelAdmin):
    pass
