from django_ratelimit.decorators import ratelimit
from django.utils.decorators import method_decorator
from rest_framework_simplejwt.views import TokenObtainPairView

@method_decorator(ratelimit(key="ip", rate="5/m", block=True), name="post")
class LoginView(TokenObtainPairView):
    pass