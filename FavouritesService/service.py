from UserService.models import User
from CommodityService.models import Commodity
from FavouritesService.models import Favourites_detail

class FavouritesService():
    @staticmethod
    def getFavourites(user):
        return Favourites_detail.objects.filter(user=user, if_delete=False)

    @staticmethod
    def deleteCommodityFromFavourites(favourites_detail_id):
        return Favourites_detail.objects.update(favourites_detail_id,{'if_delete':'True'})

    @staticmethod
    def insertCommodity(validated_data):
        favouritesdetaildata = validated_data['user','commodity']
        Favourites_detail.objects.create(favouritesdetaildata)
