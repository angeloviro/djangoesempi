from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('type_vehicles/', views.Type_VehiclesListView.as_view(), name='type_vehicles'),
   path('type_vehicle/<int:pk>', views.Type_VehicleDetailView.as_view(), name='type_vehicle-detail'),
   path('path_offers/', views.Path_OfferListView.as_view(), name='path_offers'),
   path('path_offer/<int:pk>', views.Path_OfferDetailView.as_view(), name='path_offer-detail'),
   path('user/<int:pk>', views.UserDetailView.as_view(), name='user-detail'),
   path('vehicle/<int:pk>', views.VehicleDetailView.as_view(), name='vehicle-detail'),
]