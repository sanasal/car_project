from rest_framework.decorators import api_view
from rest_framework.request import Request, HttpRequest
from rest_framework.response import Response
from rest_framework import status
from .models import advertisment
from .serializers import advertismentSerializer
from uuid import UUID


@api_view(['GET', 'POST','PUT','DELETE'])
def advertisment(request: Request | HttpRequest, id: UUID = None):
    if request.method == 'GET':
        if id is None:
            query = advertisment.objects.all()
            serializer = advertismentSerializer(query, many=True)
            return Response(serializer.data)
        else:
            try:
                query = advertisment.objects.get(pk=id)
                serializer = advertismentSerializer(query)
                return Response(serializer.data)
            except advertisment.DoesNotExist:
                return Response(
                     data={"message": "this advertisment does not exist"},
                     status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        serializer = advertismentSerializer(data=request.data)
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
                query = advertisment.objects.get(pk=id)
                serializer = advertismentSerializer(instance=query,data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(data= serializer.data)
                return Response(serializer.data)
            except advertisment.DoesNotExist:
                return Response(
                     data={"message": "this advertisment does not exist"},
                     status=status.HTTP_404_NOT_FOUND)
    else:
            try:
                query = advertisment.objects.get(pk=id)
                query.is_deleted=True
                query.save()
                return Response({
                     "message":"successfully deleted"
                })
            except advertisment.DoesNotExist:
                return Response(
                     data={"message": "this advertisment does not exist"},
                     status=status.HTTP_404_NOT_FOUND)