from django.shortcuts import render
from .models import users
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def generate_random_number():
    return str(random.randint(10000000, 99999999))

def send_email(receiver_email, subject, body):
    sender_email = "thecodeofdavinci@gmail.com"  # Replace with your email
    sender_password = "qdbf pklb ommj klgj "  # Replace with your email password

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())





#Django only <----------------------------------------------------------------------------------------------------------------------->

def cadpage(request):
    return render(request,'users/login.html')

def loginpage(request):
    return render(request, 'users/loginpage.html')

def cad_user(request):
    exist_user = users.objects.filter(email=request.POST.get('email')).first()
    if exist_user:
        return render(request, 'users/login.html', {'registered_user': 'Email já cadastrado'})
    else:
        new_user = users()
        random_number = generate_random_number()
        new_user.email = request.POST.get('email')
        new_user.password = request.POST.get('password')
        new_user.verified = 0
        new_user.code = random_number
        new_user.save()



    # users.objects.filter(email="joaopedrogoncalvesdeoliveirasi@gmail.com").delete() # to delete a row using django
    # users.objects.filter(email='').update(password='') to update a column using django

    context = {
        'email': request.POST.get('email'),
        'password': request.POST.get('password')
    } # Receiving the email and passing to the render so it will be on the input inside of the form on the other page
    email_address = f"{request.POST.get('email')}"  # Replace with the recipient's email address
    email_subject = "Verificação do email"
    email_body = f"Este é o seu código para verificar o seu email: {random_number}"
    send_email(email_address, email_subject, email_body)
    return render(request,'users/verifyemail.html', context)

def homepage(request):

    reference_user = users.objects.filter(email=request.POST.get('email')).first()

    if reference_user:
        if reference_user.verified == 0 and reference_user.password != request.POST.get('password'):
            if int(request.POST.get('verified_code')) == reference_user.code:
                users.objects.filter(email=request.POST.get('email')).update(verified=1)
                return render(request,'users/homepage.html')
            else:
                users.objects.filter(email=request.POST.get('email')).delete()
                return render(request, 'users/login.html', {'registered_user': 'Código de verificação incorreto, cadastre novamente'})
        else:
            return render(request,'users/homepage.html')
    else:
        return render(request, 'users/login.html', {'registered_user': 'Email não cadastrado'})
