
from api.booking.models import Booking
from django.db.models import Q
import datetime
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from api.slot.models import Slot


def timedate(sd,st,et):
            date=[]
            for i in sd.split('-'):
                 date.append(int(i))
            y,m,d=date
            stime=[]
            for i in st.split(':'):
                stime.append(int(i))
            sh,sm=stime
            etime=[]
            for i in et.split(':'):
                 etime.append(int(i))
            eh,em=etime
            start_time_date= datetime.datetime(y,m,d,sh,sm)
            end_time_date= datetime.datetime(y,m,d,eh,em)
            return (start_time_date,end_time_date)


@api_view(['GET','POST'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
def getme(request):
      if request.method=='POST':
            status=[]
            sd= request.data['date']
            st= request.data['start']
            et= request.data['end']
            s,e=timedate(sd,st,et)
            b=Booking.objects.values('slot').filter(Q(start__lte=s,end__gt=s)|Q(start__lte=e, end__gt=e) )
            a=Slot.objects.all()
            booked=[]
            for i in b:
                  booked.append(i['slot'])
            print(booked)
            for i in a:
                 if i.id in booked:
                       status.append({"id":i.id,"name":i.name,"status":False})
                 else:
                        status.append({"id":i.id,"name":i.name,"status":True})
            return Response(status)
      b=Booking.objects.all()
      
      return Response({'metho':'GET'})