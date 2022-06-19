from django.urls import path, include
from rest_framework.routers import SimpleRouter

# from products.views import BrendListView
from products.views import ProductListView

router = SimpleRouter()
# router.register('brend', BrendListView)
router.register('product', ProductListView)

urlpatterns = [
    path('', include(router.urls)),
]
