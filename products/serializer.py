from rest_framework import serializers
from chromedriver.seleniumform_chrome import get_parse
from products.models import Product
# from .models import Product


# class BrendSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Brend
#         fields = '__all__'
#

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        data_dict = get_parse(articul=validated_data.get('articul'))
        user = Product(
            articul=validated_data['articul'],
            name=data_dict.get('product_name'),
            price=data_dict.get('price'),
            discount=data_dict.get('fullprice'),
            brend=data_dict.get('brend'),
            provider=data_dict.get('seler_info'),
        )
        user.save()
        return user













