from .models import Commodity

# 业务类不应被实例化，其中的每个方法都用@staticmethod修饰符声明为静态方法

# 商品业务类


class CommodityService():
    @staticmethod
    def getCommodityDetail(commodity_id):
        return Commodity.objects.get(pk=commodity_id)
