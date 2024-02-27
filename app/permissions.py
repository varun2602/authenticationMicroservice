from rest_framework.permissions import BasePermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.request import Request
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from django.utils.translation import gettext_lazy as _
from jose import jwt
import jose
from rest_framework_simplejwt.authentication import api_settings

class IsTeacher(BasePermission):
    """
    Custom permission to check if the user is authenticated using JWT tokens.
    """

    def has_permission(self, request: Request, view):
        
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return False
        token = auth_header.split()[1]
        try:
            decoded_token = jwt.decode(token=token, key="vk", algorithms=['HS256'])
            if decoded_token["role"] == 3:
                return True
            return False
        except jose.exceptions.JWSSignatureError:
            return False
        
        
        # header = request.META
        # authorization_header = header.get('HTTP_AUTHORIZATION')
        # parts = authorization_header.split()
        # if len(parts) == 0:
            
        #     # Empty AUTHORIZATION header sent
        #     return None


        # if len(parts) != 2:
        #     raise AuthenticationFailed(
        #         _("Authorization header must contain two space-delimited values"),
        #         code="bad_authorization_header",
        #     )

        # token_header = parts[1]
        # jwt_token = str(token_header)[2:-1]
        # decoded_token = jwt.decode(jwt_token,key = "vk",  algorithms=['HS256'])
        # if decoded_token["role"] == 3:
        #     return True 
        # return False
       
