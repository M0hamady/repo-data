from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *
router = routers.DefaultRouter()
router.register('website', Website_index)
router.register('montgat', MontagatView)
urlpatterns = [
    path('', include(router.urls)),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns = format_suffix_patterns(urlpatterns)
