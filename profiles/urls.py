from django.urls import path
from profiles.views import ProfilesListView, ProfilesCreateView, ProfilesUpdateView, ProfilesDeleteView

app_name = 'profiles'

urlpatterns = [
    path('add_profile/', ProfilesCreateView.as_view(), name='add_profile'),
    path('', ProfilesListView.as_view(), name='profile'),
    path('delete_profile/<int:pk>', ProfilesDeleteView.as_view(), name='delete_profile'),
    path('update_profile/<int:pk>', ProfilesUpdateView.as_view(), name='update_profile'),
]