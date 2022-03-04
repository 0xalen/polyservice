from django.urls import path
from . import views

app_name = 'providers'
urlpatterns = [
    path('provider/detail/<int:pk>', views.ProviderInformationView.as_view(), name='provider_detail'),
    path('provider/delete/<int:pk>', views.ProviderInformationView.as_view(), name='provider_delete'),
    path('provider/update/<int:pk>', views.ProviderInformationView.as_view(), name='provider_update'),
    path('provider/create', views.ProviderInformationView.as_view(), name='provider_creation'),

    path('providers/list', views.ProviderListView.as_view(), name='provider_list'),
]
