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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path
from django.urls import include, path
from django.views.generic import RedirectView
from rest_framework import generics, permissions, serializers,routers
from rest_framework import urls
from rest_framework.permissions import AllowAny
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

from health.views import HealthBpViewSet,HealthWeightViewSet
from password.views import PasswordViewSet, PasswordHeaderViewSet
from private_link.views import PrivateLinkViewSet
from webtoon.views import WebtoonViewSet

#router.register(r'letters', LetterViewSet)
# from rest_framework_swagger.views import get_swagger_view
#schema_view = get_swagger_view(title='Pastebin API')
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_swagger.views import get_swagger_view


router = routers.DefaultRouter()
router.register(r'webtoon', WebtoonViewSet)
router.register(r'private_link', PrivateLinkViewSet)
router.register(r'password', PasswordViewSet)
router.register(r'password_header', PasswordHeaderViewSet)
router.register(r'health_bp', HealthBpViewSet)
router.register(r'health_weight', HealthWeightViewSet)


print(router.urls)
schema_url_patterns = [
    path('', include('webtoon.urls')),
    ]

schema_view_v1 = get_schema_view(
    openapi.Info(
        title="Open API",
        default_version='v1',
        description="시스템 API",
        terms_of_service="https://www.google.com/policies/terms/",
    ),
    public=True,
    permission_classes=(AllowAny,),
    patterns=    router.urls
    ,
)
from rest_framework.documentation import include_docs_urls
schema_view = get_swagger_view(title='Pastebin API')
docs_view = include_docs_urls(
    title='drf API',
    description='API document'
)

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),

    path('api/token/', obtain_jwt_token),
    path('api/token/verify/', verify_jwt_token),
    path('api/token/refresh/', refresh_jwt_token),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # path('docs/', docs_view),
    # path('swagger2/', schema_view),

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
    path('diary/', include(('diary.urls','diary'),namespace='diary')),
    path('words_puzzle/', include(('words_puzzle.urls','words_puzzle'),namespace='words_puzzle')),
    #

]
print('urlpatterns',urlpatterns)