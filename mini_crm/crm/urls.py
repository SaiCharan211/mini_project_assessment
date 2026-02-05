from django.urls import path
from .views import *


urlpatterns = [
    path("", api_root),  # 👈 THIS IS THE MISSING PIECE
    path("auth/login/", login_api),
    path("organizations/", organizations_api),
    path("orders/", create_order_api),
    path("admin/stats/", admin_stats),
]
