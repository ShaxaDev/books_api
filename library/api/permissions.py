from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
	message='faqat author uchun'
	# my_methods=['GET','PUT']
	#
	# def has_permission(self,request,view):
	# 	if request.method in self.my_methods:
	# 		return True
	# 	return False

	def has_object_permission(self, request, view, obj):
		if request.user.is_superuser:
			return True

		return obj.author == request.user
