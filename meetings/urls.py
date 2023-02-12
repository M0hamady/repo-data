from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *

urlpatterns = [
    path('', meeting),
    path('<int:id>/', meeting_Update),
    path('num/<int:id>/', get_exact_meating),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = format_suffix_patterns(urlpatterns)
