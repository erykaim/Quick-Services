from django.shortcuts import render
from .models import persona 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MipersonaSerializer
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication
from rest_framework import  viewsets



from rest_framework.authentication import TokenAuthentication


#class personAPIView(APIView):
 # authentication_classes = [SessionAuthentication]

  #def post(self, request):

      #serializer = MipersonaSerializer(data=request.data)
      #if serializer.is_valid():
       # serializer.save()
        #return Response(serializer.data, status=status.HTTP_201_CREATED)
      #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#crear
#esta clase dispone de todos los metodos
class personViewSet(viewsets.ModelViewSet):

#class personList(generics.ListCreateAPIView):

   authentication_classes = [SessionAuthentication]

   queryset = persona.objects.all()
   serializer_class = MipersonaSerializer


   




    




#client = APIClient()
#client.login(username='myuser', password='mypassword')

#response = client.get('/my-url/')


 