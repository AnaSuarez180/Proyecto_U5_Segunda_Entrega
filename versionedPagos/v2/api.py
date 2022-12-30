from pagos.models import Payments, Services, PaymentUser, ExpiredPayments
from rest_framework import viewsets
from versionedPagos.v2.serializers import PaymentSerializer, ServiceSerializer, PaymentUserSerializer, ExpiredPaymentsSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from pagos.pagination import StandardResultsSetPagination
from rest_framework import viewsets, filters 

class PagoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para ver pagos.
    """
    queryset = Payments.objects.get_queryset().order_by('id')
    serializer_class = PaymentSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    permission_classes = [AllowAny]

    search_fields = ['usuario__id', 'fecha_pago', 'servicio']
    throttle_scope = 'pagos'

class ServicesViewSet(viewsets.ModelViewSet):
    """
    ViewSet para ver servicios.
    """
    queryset = Services.objects.get_queryset().order_by('id')
    serializer_class = ServiceSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    permission_classes = [AllowAny]

    throttle_scope = 'pagos'

class PaymentUserViewSet(viewsets.ModelViewSet):
    """
    ViewSet para ver a los Payment Users.
    """
    queryset = PaymentUser.objects.get_queryset().order_by('id')
    serializer_class = PaymentUserSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    permission_classes = [AllowAny]

    search_fields = ['payment_date', 'expiration_date']
    throttle_scope = 'pagos'

class ExpiredPaymentsViewSet(viewsets.ModelViewSet):
    """
    ViewSet para ver los pagos expirados.
    """
    queryset = ExpiredPayments.objects.get_queryset().order_by('id')
    serializer_class = ExpiredPaymentsSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    permission_classes = [AllowAny]
    
    throttle_scope = 'pagos'