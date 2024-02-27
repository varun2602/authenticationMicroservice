from rest_framework.authentication import BaseAuthentication 
from rest_framework.exceptions import AuthenticationFailed 
from jose import jwt
import jose

class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return False
        token = auth_header.split()[1]
        try:
            decoded_token = jwt.decode(token=token, key="vk", algorithms=['HS256'])
            return (decoded_token["user_id"], token)
        except jose.exceptions.JWSSignatureError:
            return False
        
        