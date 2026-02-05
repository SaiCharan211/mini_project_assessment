from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .serializers import *
from .services import *
import json
from .permissions import IsAdmin
from django.http import JsonResponse

@csrf_exempt
@api_view(["POST"])
def login_api(request):
    user = authenticate(
        username=request.data["username"],
        password=request.data["password"]
    )
    if not user:
        return Response({"error": "Invalid credentials"}, status=401)
    login(request, user)
    return Response({"status": "ok"})


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def organizations_api(request):
    if request.method == "GET":
        return Response(OrganizationSerializer(Organization.objects.all(), many=True).data)

    serializer = OrganizationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_order_api(request):
    items = merge_cart_items(request.data["items"])
    contact = Contact.objects.get(id=request.data["contact"])

    order = Order.objects.create(
        order_no=Order.generate_order_no(),
        contact=contact
    )

    order_total = 0
    response_items = []

    for i in items:
        product = Product.objects.get(id=i["product"])
        unit_price = calculate_unit_price(product, i["size_name"])
        line_total = unit_price * i["qty"]
        order_total += line_total

        OrderItem.objects.create(
            order=order,
            product=product,
            size_name=i["size_name"],
            qty=i["qty"],
            unit_price=unit_price,
            line_total=line_total,
            extras=i.get("extras", []),
            customization=i.get("customization", "")
        )

        response_items.append({
            "product": product.name,
            "unit_price": unit_price,
            "qty": i["qty"],
            "line_total": line_total
        })

    return Response({
        "order_no": order.order_no,
        "items": response_items,
        "order_total": order_total
    })


@api_view(["GET"])
@permission_classes([IsAdmin])
def admin_stats(request):
    return Response({
        "orders": Order.objects.count(),
        "revenue": sum(i.line_total for i in OrderItem.objects.all())
    })


@api_view(["GET"])
def health(request):
    return Response({
        "status": "ok",
        "app": "mini_crm",
        "version": "0.1"
    })






@api_view(['GET'])
def api_root(request):
    return Response({
        "login": "/api/auth/login/",
        "organizations": "/api/organizations/",
        "orders": "/api/orders/",
        "admin_stats": "/api/admin/stats/",
    })
    