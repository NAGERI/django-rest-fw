# from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Product
from products.serializers import ProductSerializer

@api_view(["GET"])
def api_home(request, *args, **kwargs):
  instance = Product.objects.all().order_by("?").first()
  data = {}

  if instance:
    data = ProductSerializer(instance).data
  '''
  if instance:
    data['id'] = model_data.id
    data['title'] = model_data.title
    data['content'] = model_data.content
    data['price'] = model_data.price
    data['sale_price'] = model_data.sale_price
  
     The above is serialization,
     A model instance being turned into a python dictionary 
    '''
  return Response(data)