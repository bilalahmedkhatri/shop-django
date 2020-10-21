# Main urls
from django.contrib import admin
from django.urls import path, include
# from catalog import urls                      //Working fine

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home, name="Home"),              //working fine
    path("", include('catalog.urls'))
]
