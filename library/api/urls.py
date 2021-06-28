from django.urls import path
from .views import (BookLISTAPIView,BookDetailView,
					BookCreateAPIView,BookDeleteAPIView,
					BookUpdateAPIView,RegisterAPIView)
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
	path('', BookLISTAPIView.as_view(), name='home'),
	path('create/',BookCreateAPIView.as_view(),name='create'),
	path('<int:pk>/',BookDetailView.as_view(),name='detail'),
	path('<int:pk>/delete/',BookDeleteAPIView.as_view(),name='delete'),
	path('<int:pk>/edit/',BookUpdateAPIView.as_view(),name='update'),

	#rest auth
	path('register/',RegisterAPIView.as_view(),name='register'),
	path('login/',obtain_auth_token,name='login'),
]
