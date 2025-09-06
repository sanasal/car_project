from rest_framework.decorators import api_view
from rest_framework.request import Request, HttpRequest
from rest_framework.response import Response
from rest_framework import status
from .models import Currency
from .models import Payment
from .serializers.currency_serializer  import CurrencySerializer
from .serializers.payment_serializer  import PaymentSerializer
from uuid import UUID


@api_view(['GET', 'POST','PUT','DELETE'])
def currency(request: Request | HttpRequest, id: UUID = None):
    if request.method == 'GET':
        if id is None:
            query = Currency.objects.all()
            serializer = CurrencySerializer(query, many=True)
            return Response(serializer.data)
        else:
            try:
                query = Currency.objects.get(pk=id)
                serializer = CurrencySerializer(query)
                return Response(serializer.data)
            except Currency.DoesNotExist:
                return Response(
                     data={"message": "this Currency does not exist"},
                     status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        serializer = CurrencySerializer(data=request.data)
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
                query = Currency.objects.get(pk=id)
                serializer = CurrencySerializer(instance=query,data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(data= serializer.data)
                return Response(serializer.data)
            except Currency.DoesNotExist:
                return Response(
                     data={"message": "this Currency does not exist"},
                     status=status.HTTP_404_NOT_FOUND)
    else:
            try:
                query = Currency.objects.get(pk=id)
                query.is_deleted=True
                query.save()
                return Response({
                     "message":"successfully deleted"
                })
            except Currency.DoesNotExist:
                return Response(
                     data={"message": "this Currency does not exist"},
                     status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST','PUT','DELETE'])
def payment(request: Request | HttpRequest, id: UUID = None):
    if request.method == 'GET':
        if id is None:
            query = Payment.objects.all()
            serializer = PaymentSerializer(query, many=True)
            return Response(serializer.data)
        else:
            try:
                query = Payment.objects.get(pk=id)
                serializer = PaymentSerializer(query)
                return Response(serializer.data)
            except Payment.DoesNotExist:
                return Response(
                     data={"message": "this Payment does not exist"},
                     status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        serializer = PaymentSerializer(data=request.data)
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
                query = Payment.objects.get(pk=id)
                serializer = PaymentSerializer(instance=query,data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(data= serializer.data)
                return Response(serializer.data)
            except Payment.DoesNotExist:
                return Response(
                     data={"message": "this Payment does not exist"},
                     status=status.HTTP_404_NOT_FOUND)
    else:
            try:
                query = Payment.objects.get(pk=id)
                query.is_deleted=True
                query.save()
                return Response({
                     "message":"successfully deleted"
                })
            except Payment.DoesNotExist:
                return Response(
                     data={"message": "this Payment does not exist"},
                     status=status.HTTP_404_NOT_FOUND)


