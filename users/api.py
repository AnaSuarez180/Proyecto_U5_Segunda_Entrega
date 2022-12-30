from django.contrib.auth import authenticate
from rest_framework import viewsets, generics
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.mixins import (
    ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin)
from users.serializers import (UserSerializer, SignUpSerializer, GetUserSerializer)
from users.models import User
from users.tokens import create_jwt_pair_for_user

class UserViewSet(
    CreateModelMixin,
    ListModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    throttle_scope = 'otro'

    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class UserViewSetOne(
    UpdateModelMixin,
    RetrieveModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'username'

    throttle_scope = 'otro'

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer

    throttle_scope = 'otro'

    def post(self, request: Request):
        data = request.data
        ser = self.serializer_class(data=data)

        if ser.is_valid():
            ser.save()
            response = {'message': 'El usuario se creó correctamente.', 'data': ser.data}
            return Response(data=response, status=201)
        
        return Response(ser.errors, status=400)

class LoginView(APIView):

    throttle_scope = 'otro'

    def post(self, request: Request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)
        if user is not None:
            tokens = create_jwt_pair_for_user(user)
            idUser = User.objects.get(email=email)
            resp = {
                'message': 'Logeado correctamente',
                'id': idUser.id,
                'email': email,
                'tokens': tokens
            }
            return Response(data= resp, status=200)
        else:
            return Response({'message': 'Correo inválido o contraseña incorrecta.'})

    def get(self, request: Request):
        resp = {'user': f'{request.user}', 'auth': str(request.auth)}
        return Response(data= resp, status=200)

class GetUser(viewsets.ReadOnlyModelViewSet):
    serializer_class = GetUserSerializer
    queryset = User.objects.all()

    throttle_scope = 'otro'