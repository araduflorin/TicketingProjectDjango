from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from ldap_user import get_LDAP_user


class AuthenticationBackend(ModelBackend):

    def authenticate_ldap_user(self, request, username=None, password=None, **kwargs):

        # Get credentials from the query strings
        username = request.GET.get('username')
        password = request.GET.get('password')

        # Check that the user can authenticate in the LDAP using its username and password
        if get_LDAP_user(username, password) is None:
            return None

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = User(username=username)
            user.is_staff = True
            user.save()
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None