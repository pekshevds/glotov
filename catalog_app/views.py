from rest_framework import authentication
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpRequest
from django.core.paginator import Paginator
from catalog_app.models import Manufacturer, Good, Category
from catalog_app.serializers import (
    ManufacturerSerializer,
    GoodSerializer,
    CategorySerializer,
    UploadGoodSerializer,
)
from catalog_app.services.good import (
    fetch_goods_queryset_by_name_or_article,
    fetch_goods_queryset_by_group,
)
from catalog_app.commons import fetch_goods_by_filters, fetch_filters
# from catalog_app.services.category import fetch_menu_by_category


class ManufacturerView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest) -> Response:
        id = request.GET.get("id")
        if id:
            queryset = Manufacturer.objects.filter(id=id)
            serializer = ManufacturerSerializer(queryset, many=True)
        else:
            queryset = Manufacturer.objects.all()
            serializer = ManufacturerSerializer(queryset, many=True)
        response = {
            "data": serializer.data,
            "count": len(queryset),
            "params": request.GET,
            "success": True,
        }
        return Response(response)


class CategoryView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest) -> Response:
        id = request.GET.get("id")
        if id:
            queryset = Category.objects.filter(id=id)
            serializer = CategorySerializer(queryset, many=True)
        else:
            queryset = Category.objects.all()
            serializer = CategorySerializer(queryset, many=True)
        response = {
            "data": serializer.data,
            "count": len(queryset),
            "params": request.GET,
            "success": True,
        }
        return Response(response)


class GoodView(APIView):
    # authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest) -> Response:
        id = request.GET.get("id", 0)
        if id:
            queryset = Good.objects.filter(id=id)
            good = queryset.first()
            if good.is_group:
                queryset = fetch_goods_queryset_by_group(group=good)
            serializer = GoodSerializer(queryset, many=True)
        else:
            page_number = request.GET.get("page", 1)
            count = request.GET.get("count", 25)
            queryset = None

            search = request.GET.get("search")
            if search:
                queryset = fetch_goods_queryset_by_name_or_article(search)
            else:
                filters = fetch_filters(request=request)
                queryset = fetch_goods_by_filters(filters)
            if queryset is None:
                queryset = Good.objects.all()

            paginator = Paginator(queryset, count)
            serializer = GoodSerializer(paginator.get_page(page_number), many=True)
        response = {
            "data": serializer.data,
            "count": len(queryset),
            "params": request.GET,
            "success": True,
        }
        return Response(response)


class DataView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest) -> Response:
        response = {
            "data": {"menu": None},
            "params": request.GET,
            "success": True,
        }
        return Response(response)


class UploadGoodView(APIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request: HttpRequest) -> Response:
        response = {
            "data": None,
            "count": 0,
            "params": None,
            "success": False,
        }
        data = request.data.get("data")
        if not data:
            return Response(response)
        serializer = UploadGoodSerializer(data=data, many=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response = {
                "data": serializer.data,
                "count": len(serializer.data),
                "params": None,
                "success": True,
            }
        return Response(response)
