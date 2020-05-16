from django.conf import settings
from django.shortcuts import redirect
from django.views.generic.edit import FormView
# from django.views import For
from cas_server.forms import LoginForm

login_view_template_name = 'cas_server/login.html'


class LoginView(FormView):

    template_name = login_view_template_name
    form_class = LoginForm

    def get_form_kwargs(self):

        kwargs = super(LoginView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get(self, request, *args, **kwargs):
        print('--', dir(self))
        print('***', request)
        print('>>>>', args)
        print(kwargs)
        return super(LoginView, self).get(request, *args, **kwargs)

    def form_valid(self, form):

        return redirect('cas_login')
