import json
import decimal
import datetime
from django.utils.decorators import method_decorator
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Order


def myconverter(o):
    if isinstance(o, datetime.date):
        return o.__str__()
    if isinstance(o, decimal.Decimal):
        return o.__str__()


class OrderView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(OrderView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        order_queryset = Order.objects.prefetch_related()
        order_list = list()

        for o in order_queryset:
            order_list.append(o)

        order_list = json.dumps(order_list, default=myconverter)

        return JsonResponse(order_list, safe=False)

    def post(self, request):
        try:
            data = json.loads(request.body.decode("UTF-8"))
            Order.objects.create(**data)
            response = {
                'status': 200,
                'type': '+OK',
                'message': 'Successfully Order data recorded',
            }
        except Exception as error:
            response = {
                'status': 500,
                'type': '-ERR',
                'message': 'Internal Server Error',
            }
        return JsonResponse(response, status=response.get('status'))
