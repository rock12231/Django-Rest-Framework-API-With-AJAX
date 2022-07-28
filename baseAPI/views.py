from baseAPI.models import Emp
from baseAPI.serializers import EmpSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class EmpList(APIView):

    def get(self, request, format=None):
        snippets = Emp.objects.all()
        serializer = EmpSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmpSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.bulk_create(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmpDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Emp.objects.get(pk=pk)
        except Emp.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        emp = self.get_object(pk)
        serializer = EmpSerializer(emp)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        emp = self.get_object(pk)
        serializer = EmpSerializer(emp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        emp = self.get_object(pk)
        emp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)