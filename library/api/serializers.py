from rest_framework import serializers
from django.contrib.auth.models import User
from books.models import Book

from rest_framework.authtoken.models import Token
book_detail_url = serializers.HyperlinkedIdentityField(view_name='detail')

class BookCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model=Book
		fields=('title','subtitle','isbn')


class BookListSerializer(serializers.ModelSerializer):
	url=book_detail_url
	username = serializers.CharField(source='author.username')
	class Meta:
		model=Book
		fields=('url','id','title','subtitle','username','isbn')

class UserSerializer(serializers.ModelSerializer):
	token=serializers.SerializerMethodField()
	class Meta:
		model=User
		fields=('username','email','password','token')



	def create(self, validated_data):
		player = User.objects.create_user(**validated_data)
		token = Token.objects.create(user=player)
		return player

	def get_token(self,obj):
		return Token.objects.get(user=obj).key
