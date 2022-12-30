from pagos import api
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'v1/pagos', api.PagoViewSet, 'pagos')

urlpatterns = router.urls