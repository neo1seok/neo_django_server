"""neo_django_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.urls import include, path
from django.views.generic import RedirectView
from rest_framework import generics, permissions, serializers,routers
from rest_framework import urls


from webtoon.views import WebtoonViewSet

router = routers.DefaultRouter()
router.register(r'webtoon', WebtoonViewSet)
#router.register(r'letters', LetterViewSet)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('', RedirectView.as_view(url='/main'),name='main'),
    #path('login/', RedirectView.as_view(url='/admin/login'),name='login'),

    path('access/', include(('access.urls','access'),namespace='access')),
    #path('', include('password.urls')),
    path('main/', include(('main.urls','main'),namespace='main')),
    path('password/', include(('password.urls','password'),namespace='password')),
    path('health/', include(('health.urls','health'),namespace='health')),
    path('webtoon/', include(('webtoon.urls','webtoon'),namespace='webtoon')),
    path('private_link/', include(('private_link.urls','private_link'),namespace='private_link')),
    path('jcsg_novel/', include(('jcsg.urls','jcsg'),namespace='jcsg')),

]
print('urlpatterns',urlpatterns)