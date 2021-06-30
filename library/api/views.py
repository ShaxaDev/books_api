from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response  import Response
from rest_framework import generics
from rest_framework.permissions import (
		AllowAny,
		IsAdminUser,
		IsAuthenticated,
		IsAuthenticatedOrReadOnly,
)
from .permissions import IsOwnerOrReadOnly
from rest_framework.filters import (
	SearchFilter,
	OrderingFilter,
)
from .my_filters import IsOwnerFilterBackend

from books.models import Book
from .serializers import BookListSerializer,BookCreateSerializer,UserSerializer

from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination
from .paginations import PostPaginationCustom

class BookLISTAPIView(generics.ListAPIView):
	queryset=Book.objects.all()
	serializer_class = BookListSerializer
	permission_classes=[IsAuthenticated]
	filter_backends = [SearchFilter,OrderingFilter,IsOwnerFilterBackend]
	search_fields=['title','author__username','subtitle']
	pagination_class=PostPaginationCustom

class BookDetailView(generics.RetrieveAPIView):
	queryset=Book.objects.all()
	serializer_class=BookListSerializer


class BookUpdateAPIView(generics.RetrieveUpdateAPIView):
	queryset=Book.objects.all()
	serializer_class=BookCreateSerializer
	permission_classes=[IsOwnerOrReadOnly]

	def perform_create(self,serializer):
		serializer.save(author=self.request.user)

class BookDeleteAPIView(generics.DestroyAPIView):
	queryset=Book.objects.all()
	serializer_class=BookListSerializer

class BookCreateAPIView(generics.CreateAPIView):
	queryset=Book.objects.all()
	serializer_class=BookCreateSerializer

	def get(self,request):
		return Response({"message":'book yarating'})

	def perform_create(self,serializer):
		serializer.save(author=self.request.user)

class RegisterAPIView(generics.CreateAPIView):
	queryset=User.objects.all()
	serializer_class=UserSerializer
	permission_classes=[IsAuthenticatedOrReadOnly]

	def get(self,request):
		return Response({'msg':'register page'})


	def perform_create(self,serializer):
		u=serializer.save()
		data={
			'username':u.username,
			'token':Token.objects.get(user=u).key
			 }
		return Response(data)
	# def post(self,request):
	# 	d=UserSerializer(data=request.data)
	# 	manba={}
	# 	if d.is_valid():
	# 		u=d.save()
	# 		manba['username']=u.username
	# 		manba['token']=Token.objects.get(user=u).key
	# 		return Response(manba)
	# 	return Response(d.errors)
