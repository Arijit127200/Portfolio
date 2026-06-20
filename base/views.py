from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings
from .models import Contact


def home(request):
    return render(request, 'home.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        content = request.POST.get('content')

        # Save to database
        Contact.objects.create(
            name=name,
            email=email,
            number=number,
            content=content
        )

        # Send email to you
        EmailMessage(
            subject=f"New Portfolio Contact - {name}",
            body=f"""
Name: {name}
Email: {email}
Phone: {number}

Message:
{content}
            """,
            from_email=settings.EMAIL_HOST_USER,
            to=['arijitdatta005@gmail.com'],
            reply_to=[email]
        ).send()

        return HttpResponse("Message sent successfully!")

    return render(request, 'home.html')