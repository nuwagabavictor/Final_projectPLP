

# from django.contrib.auth.hashers import check_password

# from django.contrib.auth.backends import ModelBackend
# from .models import user

# from django.contrib.auth.backends import BaseBackend
# from django.contrib.auth import get_user_model

# User = get_user_model()  

# class EmailBackend(BaseBackend):
#     def authenticate(self, request, email=None, password=None, **kwargs):
#         try:
#             # Fetch user by email (or use your custom email field if needed)
#             user = User.objects.get(email=email)
#         except User.DoesNotExist:
#             return None

#         # Ensure the retrieved object is a User and has the `check_password` method
#         if user and user.check_password(password):
#             return user
#         return None

#     def get_user(self, user_id):
#         try:
#             return User.objects.get(pk=user_id)
#         except User.DoesNotExist:
#             return None
