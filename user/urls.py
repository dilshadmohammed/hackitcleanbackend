from django.urls import path
from .views import GetAcessToken, UserAuthAPI, UserLogoutAPI, UserRegisterAPI, BookingView,UserDetails
urlpatterns = [
    path('register/', UserRegisterAPI.as_view(), name='user-register'),
    path('auth/', UserAuthAPI.as_view(), name='user-auth'),
    path('get-access-token/', GetAcessToken.as_view(), name='user-auth'),
    path('getuser/',UserDetails.as_view(),name='user-details'),
    path('logout/', UserLogoutAPI.as_view(), name='user-auth'),
    path('booking/', BookingView.as_view(), name='create-booking'),
    path('booking/<uuid:pk>/', BookingView.as_view(), name='update-booking')
]