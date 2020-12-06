from django.db import models
from datetime import datetime
from UserService.models import User
from CommodityService.models import Commodity

# Create your models here.
class Favourites_detail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE, verbose_name="商品")
    favourites_detail_id = models.AutoField(primary_key=True)
    collect_time = models.DateTimeField(null=True, blank=True, verbose_name="收藏时间")

    class Meta:
        verbose_name = "收藏夹明细"
        verbose_name_plural = verbose_name
        
    def __str__(self):
        return self.commodity.commodity_name
