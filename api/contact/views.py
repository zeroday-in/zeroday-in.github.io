from django.http.response import JsonResponse
from django.views.generic import View
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact

class ContactApi(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if name is None or email is None or message is None:
            return JsonResponse({"message":"Mail not sent", "error": "Insufficient Data"})
        c = Contact(name=name, email=email, message=message)
        c.save()
        subject = f'ZeroDay Contact Response - {name}'
        message = f'{name} responded to our contact form.\n\n - {message} \n\n By {name} - {email}'
        send_mail(subject, message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER, ])
        return HttpResponse("Hello World")