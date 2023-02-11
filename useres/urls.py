from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *

urlpatterns = [
    path('', users),
    path('all-user/', users2), # will add permisions
    path('is-admin/', is_admin),
    path('login/', login),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('user/', user, name='auth'),
    path('UpdateProfileView/', ProfileView, name='UpdateProfileView'),
    path('main-users/', main_users, name='auth'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns = format_suffix_patterns(urlpatterns)
