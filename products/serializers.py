from rest_framework.serializers import ModelSerializer
from .models import Product, ProductGroup


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id',
                  'name',
                  'price',
                  'is_active',
                  'product_group',
                  )


class ProductGroupModelSerializer(ModelSerializer):
    class Meta:
        model = ProductGroup
        fields = ('id',
                  'group_name',
                  'pub_date',
                  )