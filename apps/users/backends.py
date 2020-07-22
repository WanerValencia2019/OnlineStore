from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.db.models import Q


UserModel = get_user_model()


class EmailUsernameBackend(BaseBackend):
    
    def authenticate(self, request, username=None, password=None, **kwargs):
        print('email and backends custom')
        try:
            user = UserModel.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user        
        except UserModel.DoesNotExist:
                return None
        

    def get_user(self, user_id):
        try:
            user = UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None

        return user if user.is_active else None