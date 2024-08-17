from django.utils.deprecation import MiddlewareMixin
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.authentication import JWTAuthentication

class TokenRefreshMiddleware(MiddlewareMixin):
    def process_request(self, request):
        auth = JWTAuthentication()
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        
        if auth_header:
            try:
                # Extract the token from the authorization header
                prefix, token = auth_header.split(' ')
                if prefix.lower() == 'bearer':
                    # Try to authenticate with the provided token
                    user, _ = auth.authenticate(request)
                    if user is None:
                        # If authentication fails, attempt to refresh the token
                        refresh_token = request.COOKIES.get('refresh_token')
                        if refresh_token:
                            try:
                                # Create a new refresh token instance
                                token = RefreshToken(refresh_token)
                                new_tokens = token.refresh()
                                # Update the request with the new access token
                                request.META['HTTP_AUTHORIZATION'] = f'Bearer {new_tokens.access_token}'
                                # Optionally, you may also want to update cookies or other storage with new tokens
                            except TokenError:
                                pass
            except (ValueError, IndexError):
                # Handle cases where the authorization header format is incorrect
                pass
        return None
