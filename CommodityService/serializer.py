from rest_framework import serializers
from .models import Commodity,CommodityApplication,BrowserHisory

class CommoditySerializer(serializers.Serializer):
    commodity_id = serializers.IntegerField(read_only=True)
    commodity_name = serializers.CharField()
    commodity_type = serializers.CharField()
    commodity_picture =serializers.ImageField()
    price = serializers.DecimalField()
    detail = serializers.CharField()
    on_shelf_time = serializers.DateTimeField()
    if_delete = serializers.BooleanField()
# commodity_id = models.AutoField(primary_key=True)
# commodity_name = models.CharField(max_length=50)
# commodity_type = models.CharField( max_length=20)
# commodity_picture = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
# price = models.DecimalField(max_digits=5, decimal_places=2)
# detail = models.TextField()
# on_shelf_time = models.DateTimeField(auto_now=False, auto_now_add=True)
# if_delete = models.BooleanField(default=False)
    def create(self,validated_data):
        Commodity.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.commodity_name = validated_data.get('commodity_name',instance.commodity_name)
        instance.commodity_type = validated_data.get('commodity_type',instance.commodity_type)
        instance.commodity_picture = validated_data.get('commodity_picture',instance.commodity_picture)
        instance.price =validated_data.get('price',instance.price)
        instance.detail = validated_data.get('detail',instance.detail)
        instance.if_delete = validated_data.get('if_delete',instance.if_delete)


class CommodityApplicationSerializer(serializers.Serializer):
    application_id = serializers.IntegerField(read_only=True)
    user = serializers.CharField()
    Commodity = serializers.IntegerField()
    apply_time = serializers.DateTimeField()
    application_state = serializers.CharField()
    auditor = serializers.CharField()
    audit_time = serializers.DateTimeField()
    if_delete = serializers.BooleanField()
# application_id = models.AutoField(primary_key=True)
# user = models.ForeignKey("UserService.User",to_field='user_id',on_delete=models.CASCADE)
# Commodity = models.ForeignKey("Commodity",to_field='commodity_id',on_delete=models.CASCADE)
# apply_time = models.DateTimeField(auto_now=False, auto_now_add=True)
# application_state = models.CharField(choices=APPLICATION_STATE_CHOICES)
# auditor = models.ForeignKey("UserService.User",to_field='user_id',on_delete=models.CASCADE)
# audit_time = models.DateTimeField(auto_now=True, auto_now_add=False)
# if_delete = models.BooleanField(default=False)
    def create(self,validated_data):
        CommodityApplication.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.application_state = validated_data.get('application_state',instance.application_state)
        instance.auditor = validated_data.get('auditor',instance.auditor)
        instance.audit_time = validated_data.get('audit_time',instance.audit_time)
        instance.if_delete = validated_data.get('if_delete',instance.if_delete)

class BrowserHisorySerializer(serializers.Serializer):
    browser_history_id = serializers.IntegerField(read_only=True)
    commodity = serializers.IntegerField()
    user =serializers.CharField()
    browse_time = serializers.DateTimeField()
    if_delete = serializers.BooleanField()

    def create(self,validated_data):
        return BrowserHisory.objects.creat(**validated_data)
    
    def update(self,instance,validated_data):
        instance.if_delete = validated_data.get('if_delete',instance.if_delete)
#browser_history_id = models.AutoField(primary_key=True)
# commodity = models.ForeignKey("Commodity",to_field='commodity_id',on_delete=models.CASCADE)
# user = models.ForeignKey("UserService.User",to_field='user_id', on_delete=models.CASCADE)
# browse_time = models.DateTimeField(auto_now=False, auto_now_add=True)
# if_delete = models.BooleanField(default=False)