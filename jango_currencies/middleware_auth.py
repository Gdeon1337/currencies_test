from django.utils.deprecation import MiddlewareMixin
from rest_framework import exceptions
from rest_framework_jwt.serializers import User

from .settings import PATH_AUTH


class AuthMiddleware(MiddlewareMixin):

	def process_request(self, request):
		if request.path in PATH_AUTH:
			try:
				User.objects.get(username=request.user.username)
			except User.DoesNotExist:
				raise exceptions.AuthenticationFailed()
