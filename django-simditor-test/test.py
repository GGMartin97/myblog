from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from simditor.views import upload_handler


class ImageUploadView(generic.View):
    """ImageUploadView."""

    http_method_names = ['post']

    def post(self, request, **kwargs):
        """Post."""
        return upload_handler(request)


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='simditor-form'),
    url(r'^simditor/upload', csrf_exempt(ImageUploadView.as_view())),
]





# IndexView
from django import forms

from django.views import generic

from simditor.fields import RichTextFormField
try:
    from django.urls import reverse
except ImportError:  # Django < 2.0
    from django.core.urlresolvers import reverse


class SimditorForm(forms.Form):
    content = RichTextFormField()


class IndexView(generic.FormView):
    form_class = SimditorForm

    template_name = 'index.html'

    def get_success_url(self):
        return reverse('simditor-form')





 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <form method="post" action="./">
        {% csrf_token %}
        {{ form.media }}
        {{ form.as_p }}
        <p><input type="submit" value="post"></p>
    </form>
</body>
</html>