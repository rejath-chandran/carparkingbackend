import json
import razorpay


from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions

from .models import Booking
from api.slot.models import Slot
from api.slot.views import timedate


def verify_signature(response_data):
        client = razorpay.Client(auth=('rzp_test_01ckBeGNiKSNAv','IHurDFKml1nituLVwT6xtaMH'))
        return client.utility.verify_payment_signature(response_data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def start_payment(request):
    
    price = request.data['price']
    # vno= request.data['vno']
    # slot= request.data['slot']
    # date= request.data['date']
    # start= request.data['start']
    # end= request.data['end']
    # phone= request.data['phone']
    # s,e=timedate(date,start,end)
    
    client = razorpay.Client(auth=('rzp_test_01ckBeGNiKSNAv','IHurDFKml1nituLVwT6xtaMH'))

    
    payment = client.order.create({"amount": int(price) * 100, 
                                   "currency": "INR", 
                                   "payment_capture": "0"})

    # ss=Slot.objects.get(id=slot)
    # book = Booking.objects.create(slot=ss,
    #                               vehicle_no=vno,
    #                               price=price,
    #                               start=s,
    #                               end=e,
    #                               phone=phone,
    #                              order_payment_id=payment['id'])
    data = {
        "payment": payment,
    }
    return Response(data)




@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def handle_payment_success(request):
    
    res = json.loads(request.data["response"])
    ord_id = ""
    raz_pay_id = ""
    raz_signature = ""


    for key in res.keys():
        if key == 'razorpay_order_id':
            ord_id = res[key]
        elif key == 'razorpay_payment_id':
            raz_pay_id = res[key]
        elif key == 'razorpay_signature':
            raz_signature = res[key]

    data = {
        'razorpay_order_id': ord_id,
        'razorpay_payment_id': raz_pay_id,
        'razorpay_signature': raz_signature
    }

    
    client = razorpay.Client(auth=('rzp_test_01ckBeGNiKSNAv','IHurDFKml1nituLVwT6xtaMH'))

    
    if not verify_signature(data):
        res_data = {
        'message': 'payment successfully received!'
                 }
        print("sucesss")
        return Response(res_data)
        

    
    print("faileddd")
    return Response({'error': 'Something went wrong'})

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def add_bookin(request):
    price = request.data['price']
    vno= request.data['vno']
    slot= request.data['slot']
    date= request.data['date']
    start= request.data['start']
    end= request.data['end']
    phone= request.data['phone']
    s,e=timedate(date,start,end)
    ss=Slot.objects.get(id=slot)
    book = Booking.objects.create(slot=ss,
                                  vehicle_no=vno,
                                  price=price,
                                  start=s,
                                  end=e,
                                  phone=phone)
    return Response({"sucess":'true'})