from django import forms
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _


class LoginForm(forms.Form):
    """Standard username and password authentication form."""
    username = forms.CharField(label=_("Username"),
                               error_messages={'required':
                                               _("Please enter your username")})
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput,
                               error_messages={'required':
                                               _("Please enter your password")})

    def __init__(self, request, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            try:
                self.user = authenticate(
                    request=self.request, username=username, password=password)
            except Exception:
                error_msg = _('Internal error while authenticating user')
                raise forms.ValidationError(error_msg)

            if self.user is None:
                error_msg = _('The username or password is not correct')
                raise forms.ValidationError(error_msg)
            else:
                if not self.user.is_active:
                    error_msg = _('This user account is disabled')
                    raise forms.ValidationError(error_msg)

        return self.cleaned_data
