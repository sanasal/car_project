from rest_framework.decorators import api_view
from rest_framework.request import Request, HttpRequest
from rest_framework.response import Response
from rest_framework import status
from .models import Purchase
from .serializers import PurchaseSerializer
from uuid import UUID


@api_view(['GET', 'POST','PUT','DELETE'])
def purchase(request: Request | HttpRequest, id: UUID = None):
    if request.method == 'GET':
        if id is None:
            query = Purchase.objects.all()
            serializer = PurchaseSerializer(query, many=True)
            return Response(serializer.data)
        else:
            try:
                query = Purchase.objects.get(pk=id)
                serializer = PurchaseSerializer(query)
                return Response(serializer.data)
            except Purchase.DoesNotExist:
                return Response(
                     data={"message": "this Purchase does not exist"},
                     status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        serializer = PurchaseSerializer(data=request.data)
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
                query = Purchase.objects.get(pk=id)
                serializer = PurchaseSerializer(instance=query,data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(data= serializer.data)
                return Response(serializer.data)
            except Purchase.DoesNotExist:
                return Response(
                     data={"message": "this Purchase does not exist"},
                     status=status.HTTP_404_NOT_FOUND)
    else:
            try:
                query = Purchase.objects.get(pk=id)
                query.is_deleted=True
                query.save()
                return Response({
                     "message":"successfully deleted"
                })
            except Purchase.DoesNotExist:
                return Response(
                     data={"message": "this Purchase does not exist"},
                     status=status.HTTP_404_NOT_FOUND)