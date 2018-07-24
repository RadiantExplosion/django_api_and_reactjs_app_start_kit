from django.shortcuts import render

# Create your views here.
from talent.models import Talent
from authentication.models import User
from talent.serializers import TalentSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class TalentDetail(APIView):
    """
    Retrieve, update or delete a talent.
    """
    def get_object(self, pk):
        try:
            user = User.objects.get(pk=pk)
            talent = Talent.objects.get(user=user.id)
            return talent
        except Talent.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        talent_item = self.get_object(pk)
        serializer = TalentSerializer(talent_item)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        talent_item = self.get_object(pk)
        serializer = TalentSerializer(talent_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        talent_item = self.get_object(pk)
        talent_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
