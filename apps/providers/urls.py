from django.urls import path
from . import views

app_name = 'providers'
urlpatterns = [
    path('provider/detail/<int:pk>', views.ProviderInformationView.as_view(), name='provider_detail'),
    path('provider/delete/<int:pk>', views.ProviderInformationView.as_view(), name='provider_delete'),
    path('provider/update/<int:pk>', views.ProviderInformationView.as_view(), name='provider_update'),
    path('provider/create', views.ProviderInformationView.as_view(), name='provider_create'),
    path('provider/list', views.ProviderListView.as_view(), name='provider_list'),

    path('provider/service_area/detail/<int:pk>', views.ServiceAreaInformationView.as_view(), name='service_area_detail'),
    path('provider/service_area/delete/<int:pk>', views.ServiceAreaInformationView.as_view(), name='service_area_delete'),
    path('provider/service_area/update/<int:pk>', views.ServiceAreaInformationView.as_view(), name='service_area_update'),
    path('provider/service_area/create', views.ServiceAreaInformationView.as_view(), name='service_area_create'),
    path('provider/service_area/list', views.ServiceAreaListView.as_view(), name='service_area_list'),

    path('service_area/', views.FindServiceAreasView.as_view(), name='find_service_areas'),
]
