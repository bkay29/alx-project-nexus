from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# URLS will point to:
# /api/auth/login/  -> TokenObtainPairView
# /api/auth/refresh/ -> TokenRefreshView