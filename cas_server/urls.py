from django.urls import path

from cas_server.views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='cas_login'),
    # path('logout/', LogoutView.as_view(), name='cas_logout'),
    # path('validate/', ValidateView.as_view(), name='cas_validate'),
]
