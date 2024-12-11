from rest_framework.routers import DefaultRouter

from product.views import ProductAPIViewSet
from product.apps import ProductConfig

app_name = ProductConfig.name

router = DefaultRouter()
router.register(r'product', ProductAPIViewSet)


urlpatterns =[] + router.urls
