from rest_framework.decorators import api_view
from rest_framework.request import Request, HttpRequest
from rest_framework.response import Response
from rest_framework import status

from .models import Color
from .models import CarModel
from .models import Product
from .models import Manufacturer
from .serializers.color_serializer  import ColorSerializer
from .serializers.model_serializer  import ModelSerializer
from .serializers.manufactuer_serializer import ManufacturerSerializer
from .serializers.product_serializer  import ProductSerializer
from uuid import UUID

from django.db.models import Q


@api_view(['GET', 'POST','PUT','DELETE'])
def color(request: Request | HttpRequest, id: UUID = None):
    if request.method == 'GET':
        if id is None:
            query = Color.objects.all()
            serializer = ColorSerializer(query, many=True)
            return Response(serializer.data)
        else:
            try:
                query = Color.objects.get(pk=id)
                serializer = ColorSerializer(query)
                return Response(serializer.data)
            except Color.DoesNotExist:
                return Response(
                     data={"message": "this Color does not exist"},
                     status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        serializer = ColorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED
                )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    elif request.method == 'PUT':
            try:
                query = Color.objects.get(pk=id)
                serializer = ColorSerializer(instance=query,data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(data= serializer.data)
                return Response(serializer.data)
            except Color.DoesNotExist:
                return Response(
                     data={"message": "this Color does not exist"},
                     status=status.HTTP_404_NOT_FOUND)
    else:
            try:
                query = Color.objects.get(pk=id)
                query.is_deleted=True
                query.save()
                return Response({
                     "message":"successfully deleted"
                })
            except Color.DoesNotExist:
                return Response(
                     data={"message": "this Color does not exist"},
                     status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST','PUT','DELETE'])
def model(request: Request | HttpRequest, id: UUID = None):
    if request.method == 'GET':
        if id is None:
            query = CarModel.objects.all()
            serializer = ModelSerializer(query, many=True)
            return Response(serializer.data)
        else:
            try:
                query = CarModel.objects.get(pk=id)
                serializer = ModelSerializer(query)
                return Response(serializer.data)
            except CarModel.DoesNotExist:
                return Response(
                     data={"message": "this Model does not exist"},
                     status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        serializer = ModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED
                )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    elif request.method == 'PUT':
            try:
                query = CarModel.objects.get(pk=id)
                serializer = ModelSerializer(instance=query,data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(data= serializer.data)
                return Response(serializer.data)
            except CarModel.DoesNotExist:
                return Response(
                     data={"message": "this Model does not exist"},
                     status=status.HTTP_404_NOT_FOUND)
    else:
            try:
                query = CarModel.objects.get(pk=id)
                query.is_deleted=True
                query.save()
                return Response({
                     "message":"successfully deleted"
                })
            except CarModel.DoesNotExist:
                return Response(
                     data={"message": "this Model does not exist"},
                     status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST','PUT','DELETE'])
def manufacturer(request: Request | HttpRequest, id: UUID = None):
    if request.method == 'GET':
        if id is None:
            query = Manufacturer.objects.all()
            serializer = ManufacturerSerializer(query, many=True)
            return Response(serializer.data)
        else:
            try:
                query = Manufacturer.objects.get(pk=id)
                serializer = ManufacturerSerializer(query)
                return Response(serializer.data)
            except Manufacturer.DoesNotExist:
                return Response(
                     data={"message": "this manufacturer does not exist"},
                     status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        serializer = ManufacturerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED
                )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    elif request.method == 'PUT':
            try:
                query = Manufacturer.objects.get(pk=id)
                serializer = ManufacturerSerializer(instance=query,data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(data= serializer.data)
                return Response(serializer.data)
            except Manufacturer.DoesNotExist:
                return Response(
                     data={"message": "this manufacturer does not exist"},
                     status=status.HTTP_404_NOT_FOUND)
    else:
            try:
                query = Manufacturer.objects.get(pk=id)
                query.is_deleted=True
                query.save()
                return Response({
                     "message":"successfully deleted"
                })
            except Manufacturer.DoesNotExist:
                return Response(
                     data={"message": "this manufacturer does not exist"},
                     status=status.HTTP_404_NOT_FOUND)           
@api_view(['GET', 'POST','PUT','DELETE'])
def product(request: Request | HttpRequest, id: UUID = None):
    if request.method == 'GET':
        if id is None:
            query = Product.objects.all()
            print(query.query)
            serializer = ProductSerializer(query, many=True)
            return Response(serializer.data)
        else:
            try:
                query = Product.objects.get(pk=id)
                serializer = ProductSerializer(query)
                return Response(serializer.data)
            except Product.DoesNotExist:
                return Response(
                     data={"message": "this Product does not exist"},
                     status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED
                )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    elif request.method == 'PUT':
            try:
                query = Product.objects.get(pk=id)
                serializer = ProductSerializer(instance=query,data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(data= serializer.data)
                return Response(serializer.data)
            except Product.DoesNotExist:
                return Response(
                     data={"message": "this Product does not exist"},
                     status=status.HTTP_404_NOT_FOUND)
    else:
            try:
                query = Product.objects.get(pk=id)
                query.is_deleted=True
                query.save()
                return Response({
                     "message":"successfully deleted"
                })
            except Product.DoesNotExist:
                return Response(
                     data={"message": "this Product does not exist"},
                     status=status.HTTP_404_NOT_FOUND)
'''
@api_view(['GET'])
def filterApi(request:HttpRequest|Request)->Response:
     query= Product.objects.filter(
     ).order_by('-price')

     #serializer= manufacturerSerializer(query, many= True)
     serializer= ProductSerializer(query, many= True)


     return Response(serializer.data)
'''

@api_view(['GET'])
def filterApi(request: HttpRequest | Request) -> Response:
    queryset = Product.objects.filter(is_deleted=False, is_sold=False)

    manufacturer_id = request.GET.get('manufacturer')
    model_id = request.GET.get('model')
    color_id = request.GET.get('color')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    is_new = request.GET.get('is_new')

    if manufacturer_id:
        queryset = queryset.filter(carModel__manufacturer__id=manufacturer_id)
    if model_id:
        queryset = queryset.filter(carModel__id=model_id)
    if color_id:
        queryset = queryset.filter(color__id=color_id)
    if min_price:
        queryset = queryset.filter(price__gte=min_price)
    if max_price:
        queryset = queryset.filter(price__lte=max_price)
    if is_new in ['true', 'false']:
        queryset = queryset.filter(is_new=(is_new == 'true'))

    serializer = ProductSerializer(queryset.order_by('-price'), many=True)
    return Response(serializer.data)
