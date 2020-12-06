from UserService.models import User
from UserService.serializer import UserSerializer
from CommodityService.models import Commodity
from CommodityService.serializer import CommoditySerializer
from FavouritesService.models import Favourites_detail
from rest_framework import serializers

class Favourites_detailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourites_detail
        fields = "__all__"