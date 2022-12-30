from pagos.models import Payments
from rest_framework import viewsets
from pagos.serializers import PaymentSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from pagos.pagination import StandardResultsSetPagination
from rest_framework import viewsets, filters 

class PagoViewSet(viewsets.ModelViewSet):
    queryset = Payments.objects.get_queryset().order_by('id')
    serializer_class = PaymentSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    permission_classes = [AllowAny]

    search_fields = ['usuario__id', 'fecha_pago', 'servicio']
    throttle_scope = 'pagos'