from django.core.mail import send_mail
from authentication.models import CustomUser
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import OTP
import random

class RequestOTPView(views.APIView):
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def post(self, request):
        email = request.data.get('email')
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        otp_code = str(random.randint(100000, 999999))  # Generate a 6-digit OTP
        otp = OTP.objects.create(user=user, otp_code=otp_code)

        # Send OTP email
        send_mail(
            'Your OTP Code',
            f'Your OTP code is {otp_code}.',
            'from@example.com',  # Replace with sender's email
            [email],
            fail_silently=False,
        )

        return Response({'message': 'OTP sent successfully'}, status=status.HTTP_200_OK)

class VerifyOTPView(views.APIView):
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def post(self, request):
        email = request.data.get('email')
        otp_code = request.data.get('otp_code')
        
        try:
            user = CustomUser.objects.get(email=email)
            otp = OTP.objects.filter(user=user, otp_code=otp_code, is_verified=False).first()
            
            if not otp:
                return Response({'error': 'Invalid or expired OTP'}, status=status.HTTP_400_BAD_REQUEST)
            
            otp.is_verified = True
            otp.save()
            
            return Response({'message': 'OTP verified successfully'}, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
