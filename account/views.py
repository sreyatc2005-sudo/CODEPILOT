from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

from account.serializers import UserSerializer


class AdminCreateView(APIView):

    def post(self,request):

        form_data = request.data

        serializer_instance = UserSerializer(data=form_data)

       

