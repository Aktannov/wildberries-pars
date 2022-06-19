from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from products.models import Product
from products.permissions import IsAdmin
from products.serializer import ProductSerializer
from .filters import ProductFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
# from chromedriver.seleniumform_chrome import get_parse


#
# class BrendListView(ModelViewSet):
#     queryset = Brend.objects.all()
#     serializer_class = BrendSerializer
#
#     def get_permissions(self):
#         if self.action == 'retrieve':
#             return [AllowAny()]
#         else:
#             return [IsAdmin()]


class ProductListView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    # filterset_class = ProductFilter
    # search_fields = ['articul']
    # ordering_fields = ['name']

    def get_permissions(self):
        if self.action == 'retrieve':
            return [AllowAny()]
        else:
            return [IsAdmin()]

