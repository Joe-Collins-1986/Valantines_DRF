from django.urls import path
from partnerprofile import views

urlpatterns = [
    path('', views.PartnerProfileList.as_view()),   # Views have to be added!
    path('<int:pk>/', views.PartnerProfileDetail.as_view()), # Views have to be added!
]
