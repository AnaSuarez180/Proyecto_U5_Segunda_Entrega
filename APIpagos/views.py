from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def pagos(request):
    return render(request, 'pagos.html')

def nuevo_pago(request):
    return render(request, 'nuevo_pago.html')

def servicios(request):
    return render(request, 'servicios.html')