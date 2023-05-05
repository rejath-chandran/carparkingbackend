from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from .models import Categorie


@api_view(['GET','POST'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
def gettype(request):
    if request.method=='GET':
       data=[]
       c=Categorie.objects.all()
       for i in c:
           data.append({"name":i.name,"price":i.price})
       return Response(data)
