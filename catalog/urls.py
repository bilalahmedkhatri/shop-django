from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . views import HomeView, checkout, ItemDetailView

app_name = "catalog"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("checkout/", checkout, name="Checkout"),
    path("product/<slug>/", ItemDetailView.as_view(), name="product"),
    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
