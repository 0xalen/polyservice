from django.urls import path
from . import views

app_name = 'providers'
urlpatterns = [
    path('provider/detail', views.ProviderInformationView.as_view(), name='provider_detail'),
    path('provider/detail/<int:pk>', views.ProviderInformationView.as_view(), name='provider_detail'),
    path('provider/update/<int:pk>', views.ProviderInformationView.as_view(), name='provider_update'),
    path('provider/insert/<int:pk>', views.ProviderInformationView.as_view(), name='provider_insertion'),
    path('provider/create/<int:pk>', views.ProviderInformationView.as_view(), name='provider_creation'),

    path('providers/list', views.ProviderListView.as_view(), name='provider_list'),
]
