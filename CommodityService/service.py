from .models import Commodity
from .serializer import CommodityDetailSerializer

# 业务类不应被实例化，其中的每个方法都用@staticmethod修饰符声明为静态方法

# 商品业务类


class CommodityService():
    @staticmethod
    def getCommodityDetail(commodity_id):
        commodity_detail = Commodity.objects.get(pk=commodity_id)
        return CommodityDetailSerializer(commodity_detail)
