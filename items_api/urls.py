from django.urls import path
from . import views

urlpatterns = [
    # path('api/items', views.ItemList.as_view(), name='item_list'), # api/items will be routed to the ItemList view for handling
    # path('api/items/<int:pk>', views.ItemDetail.as_view(), name='item_detail'), # api/items will be routed to the ItemDetail view for handling
     path('', views.ItemList.as_view(), name='item_list'), # api/items will be routed to the ItemList view for handling
     path('<int:pk>', views.ItemDetail.as_view(), name='item_detail'), # api/items will be routed to the ItemDetail view for handling
]
