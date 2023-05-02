from django.urls import path,include
from .views import  personViewSet
from rest_framework import routers
from aplicacion.usuarios import views
#from .views import  personAPIView


router= routers.DefaultRouter()
router.register(r'crud',views.personViewSet)
urlpatterns = [
    path('',include(router.urls))

  
    #endpoint crear
    #path('CrearServicios/',personList.as_view()),

   # path('ListarServicios/',personAPIView.as_view()),


   

   
]