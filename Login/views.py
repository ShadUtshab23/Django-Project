from django.template.loader import get_template
from django.http import HttpResponseServerError
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'myproject/Login/templates/login.html'  # Update the template path accordingly

    def form_valid(self, form):
        try:
            template = get_template(self.template_name)
        except Exception as e:
            return HttpResponseServerError(f"Error loading template: {str(e)}")

        # Continue with your code
