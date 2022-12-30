from versionedPagos.v2 import api
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'v2/pagos', api.PagoViewSet, 'pagos')
router.register(r'v2/services', api.ServicesViewSet, 'servicios')
router.register(r'v2/payment_user', api.PaymentUserViewSet, 'payment_user')
router.register(r'v2/expired_payments', api.ExpiredPaymentsViewSet, 'expired_payments')

urlpatterns = router.urls