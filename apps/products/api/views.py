import sentry_sdk
from django.core.exceptions import FieldError
from django.db.models import Q
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import ProductSerializer
from ..models import Product


class ProductsView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    serializer_class = ProductSerializer

    def get_queryset(self):
        order = self.request.query_params.get('order', 'tile')
        filter = self.request.query_params.get('filter', None)
        try:
            if filter:
                products = Product.objects.order_by(order, ).filter(Q(title__icontains=filter) | Q(description__icontains=filter))
            else:
                products = Product.objects.order_by(order, ).all()
        except FieldError as e:
            products = Product.objects.order_by('title').all()
            sentry_sdk.capture_exception(e)

        return products

    def list(self, request, *args):
        objs = self.get_queryset()
        products_serialized = self.get_serializer(instance=objs, many=True)
        data = products_serialized.data
        return Response({"data": data}, status.HTTP_200_OK)
