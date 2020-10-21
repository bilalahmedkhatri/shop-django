from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . views import home, checkout, product

urlpatterns = [
    path("", home, name="home"),
    path("checkout/", checkout, name="Checkout"),
    path("product/", product, name="Product"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
