"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.documentation import include_docs_urls
import rest_framework_swagger
# from rest_framework_swagger.views import get_swagger_view

# schema_view = get_swagger_view(title='Ecommerce API')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include_docs_urls(title='Ecommerce API')),
    # url(r'^$', schema_view),
    url(r'^auth/', include('authentication.urls', namespace='auth')),
    url(r'^items/', include('items.urls', namespace='items')),
    url(r'^carts/', include('carts.urls', namespace='carts')),
    url(r'^billings/', include('billings.urls', namespace='billings')),
]
