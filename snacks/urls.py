from django.urls import path
from .views import HomePageView, AboutPageView, SnacksListView, SnackDetailsView

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('about',AboutPageView.as_view(),name='about'),
    path('snacks',SnacksListView.as_view(), name="snacks"),
    path('<int:pk>/',SnackDetailsView.as_view(), name="snack_detail")
]