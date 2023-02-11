from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as auth_views
from .views import *

urlpatterns = [
    path('', project),
    path('step/', step),
    path('step/<int:id>/', exac_step),
    path('astep/<int:id>/', aStep),
    path('addstep/<int:id>/', add_step),
    path('moshtrayat/<int:id>/', moshtrayat),
    path('<int:id>/', exac_proj),
    path('project_users/<int:id>/', project_users),
    path('generate-token/', auth_views.obtain_auth_token)
    # path('<int:id>/', meeting_Update),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = format_suffix_patterns(urlpatterns)
