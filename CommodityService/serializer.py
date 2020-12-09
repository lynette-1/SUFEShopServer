from rest_framework import serializers
from .models import Commodity, CommodityApplication, BrowserHisory

class CommoditySerializer(serializers.Serializer):
    commodity_id = serializers.IntegerField(read_only=True,label='商品编号')
    commodity_name = serializers.CharField(label='商品名称')
    commodity_type = serializers.CharField(label='商品类别')
    commodity_picture =serializers.ImageField(label='图片')
    price = serializers.DecimalField(label='价格')
    detail = serializers.CharField(label='详细描述')
    on_shelf_time = serializers.DateTimeField(label='上架时间')
    if_delete = serializers.BooleanField(label='是否删除')
# commodity_id = models.AutoField(primary_key=True)
# commodity_name = models.CharField(max_length=50)
# commodity_type = models.CharField( max_length=20)
# commodity_picture = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
# price = models.DecimalField(max_digits=5, decimal_places=2)
# detail = models.TextField()
# on_shelf_time = models.DateTimeField(auto_now=False, auto_now_add=True)
# if_delete = models.BooleanField(default=False)
    def create(self,validated_data):
        return Commodity.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.commodity_name = validated_data.get('commodity_name',instance.commodity_name)
        instance.commodity_type = validated_data.get('commodity_type',instance.commodity_type)
        instance.commodity_picture = validated_data.get('commodity_picture',instance.commodity_picture)
        instance.price =validated_data.get('price',instance.price)
        instance.detail = validated_data.get('detail',instance.detail)
        instance.if_delete = validated_data.get('if_delete',instance.if_delete)
        instance.save()
        return instance

class CommodityApplicationSerializer(serializers.Serializer):
    APPLICATION_STATE_CHOICES = (
        ('TO_BE_REVIEWED','待审核'),
        ('APPROVED','审核通过'),
        ('REJECTED','审核未通过'),
    )
    user = serializers.CharField(label='申请人')
    commodity = serializers.IntegerField(label='商品')
    apply_time = serializers.DateTimeField(label='申请时间')
    application_state = serializers.ChoiceField(label='申请状态',choices=APPLICATION_STATE_CHOICES )
    auditor = serializers.CharField(label='审核人')
    audit_time = serializers.DateTimeField(label='审核时间')
    if_delete = serializers.BooleanField(label='是否删除')
# application_id = models.AutoField(primary_key=True)
# user = models.ForeignKey("UserService.User",to_field='user_id',on_delete=models.CASCADE)
# Commodity = models.ForeignKey("Commodity",to_field='commodity_id',on_delete=models.CASCADE)
# apply_time = models.DateTimeField(auto_now=False, auto_now_add=True)
# application_state = models.CharField(choices=APPLICATION_STATE_CHOICES)
# auditor = models.ForeignKey("UserService.User",to_field='user_id',on_delete=models.CASCADE)
# audit_time = models.DateTimeField(auto_now=True, auto_now_add=False)
# if_delete = models.BooleanField(default=False)
    def create(self,validated_data):
        return CommodityApplication.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.commodity = validated_data.get('commodity',instance.commodity)
        instance.application_state = validated_data.get('application_state',instance.application_state)
        instance.auditor = validated_data.get('auditor',instance.auditor)
        instance.audit_time = validated_data.get('audit_time',instance.audit_time)
        instance.if_delete = validated_data.get('if_delete',instance.if_delete)
        instance.save()
        return instance

class BrowserHisorySerializer(serializers.Serializer):
    commodity = serializers.IntegerField(label='商品')
    user =serializers.CharField(label='用户')

    def create(self,validated_data):
        return BrowserHisory.objects.creat(**validated_data)

    def update(self,instance,validated_data):
        instance.if_delete = validated_data.get('if_delete',instance.if_delete)
        instance.save()
        return instance
#browser_history_id = models.AutoField(primary_key=True)
# commodity = models.ForeignKey("Commodity",to_field='commodity_id',on_delete=models.CASCADE)
# user = models.ForeignKey("UserService.User",to_field='user_id', on_delete=models.CASCADE)
# browse_time = models.DateTimeField(auto_now=False, auto_now_add=True)
# if_delete = models.BooleanField(default=False)


# 这部分奸商
class CommodityDetailSerializer(serializers.Serializer):
    commodity_id = serializers.IntegerField(read_only=True,label='商品编号')
    commodity_name = serializers.CharField(label='商品名称')
    commodity_type = serializers.CharField(label='商品类别')
    commodity_picture =serializers.ImageField(label='图片')
    price = serializers.DecimalField(label='价格')
    detail = serializers.CharField(label='详细描述')
    on_shelf_time = serializers.DateTimeField(label='上架时间')

    def create(self,validated_data):
        return Commodity.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.commodity_name = validated_data.get('commodity_name',instance.commodity_name)
        instance.commodity_type = validated_data.get('commodity_type',instance.commodity_type)
        instance.commodity_picture = validated_data.get('commodity_picture',instance.commodity_picture)
        instance.price = validated_data.get('price',instance.price)
        instance.detail = validated_data.get('detail',instance.detail)
        instance.save()
        return instance
