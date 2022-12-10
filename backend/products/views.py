from rest_framework import authentication, generics, mixins, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.http import Http404
from django.shortcuts import get_object_or_404

from .models import Product
from .permissons import IsStaffEditorPermission
from .serializers import ProductSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  authentication_classes = [authentication.SessionAuthentication]
  permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission]
  # The first permission ordered is the first to be matched

  def perform_create(self, serializer):
    title = serializer.validated_data.get('title')
    content = serializer.validated_data.get('content')
    if content is None:
      content = "THis is a single view"
    serializer.save(content=content)
    # Send a django signal
product_list_create_view = ProductListCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

product_detail_view = ProductDetailAPIView.as_view()

class ProductUpdateAPIView(generics.UpdateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'

  def perform_update(self, serializer):
    instance = serializer.save()
    if not instance.content:
     instance. content = instance.title

product_update_view = ProductUpdateAPIView.as_view()

class ProductDestroyAPIView(generics.DestroyAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'

  def perform_destroy(self, instance):
    # logic before delete
    super().perform_destroy(instance)
     
product_delete_view = ProductDestroyAPIView.as_view()

'''
Class based view using mixins
'''
class ProductMixinView(mixins.CreateModelMixin,mixins.ListModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'

  def get(self,request, *args, **kwargs):
    pk = kwargs.get("pk")
    if pk is not None:
      return self.retrieve(request,*args,**kwargs)
    return self.list(request, *args, **kwargs )

  def post(self,request,*args, **kwargs):
    return self.create(request,*args, **kwargs)

product_mixin_view = ProductMixinView.as_view()

@api_view(["GET","POST"])
def product_alt_view(request, pk=None, *args, **kwargs):
  method = request.method
  if method == "GET":
    # detailed view
    if pk is not None:
      obj = get_object_or_404(Product,pk=pk) 
      data = ProductSerializer(obj,many=False).data
      return Response(data)
    # list view
    queryset = Product.objects.all()
    data = ProductSerializer(queryset,many=True).data
    return Response(data)

  if method == "POST":
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      title = serializer.validated_data.get('title')
      content = serializer.validated_data.get('content')
      if content is None:
        content = title
      serializer.save(content=content)
    print(instance)
    return Response(serializer.data)