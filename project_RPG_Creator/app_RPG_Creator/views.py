from django.shortcuts import render
from .models import users
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def generate_random_number():
    return str(random.randint(10000000, 99999999))

def send_email(receiver_email, subject, body):
    sender_email = "thecodeofdavinci@gmail.com" 
    sender_password = "qdbf pklb ommj klgj "  
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())






def cadpage(request):
    return render(request,'users/register.html')

def loginpage(request):
    return render(request, 'users/loginpage.html')

def cad_user(request):
    user_email = request.POST.get('email')
    user_password = request.POST.get('password')

    exist_user = users.objects.filter(email=user_email).first()
    if exist_user:
        return render(request, 'users/login.html', {'registered_user': 'Email já cadastrado'})
    else:
        new_user = users()
        random_number = generate_random_number()
        new_user.email = user_email
        new_user.password = user_password
        new_user.verified = 0
        new_user.code = random_number
        new_user.save()



    # users.objects.filter(email="joaopedrogoncalvesdeoliveirasi@gmail.com").delete() # to delete a row using django
    # users.objects.filter(email='').update(password='') to update a column using django

    context = {
        'email': user_email,
        'password': user_password
    } 
    email_address = f"{user_email}" 
    email_subject = "Verificação do email"
    email_body = f"Este é o seu código para verificar o seu email: {random_number}"
    send_email(email_address, email_subject, email_body)
    return render(request,'users/verifyemail.html', context)

def end_verification(request):
    user_email = request.POST.get('email')

    reference_user = users.objects.filter(email=user_email).first()

    if reference_user:
        if reference_user.verified == 0:
            if int(request.POST.get('verified_code')) == reference_user.code:
                context = {
                    'response':'Email verificado C:'
                }
                users.objects.filter(email=user_email).update(verified=1)
                return render(request, 'users/loginpage.html', context)
            else:
                context = {
                    'registered_user':'Código de verificação incorreto, cadastre novamente'
                }
                users.objects.filter(email=user_email).delete()
                return render(request, 'users/register.html', context)
        else:
            context = {
                    'response':'Email já verificado, se esqueceu a senha, clique em "Esqueceu a senha?" para recupera-la'
            }
            return render(request, 'users/loginpage.html',context)
    else:
        context = {
                    'registered_user':'Email não cadastrado'
        }
        return render(request, 'users/register.html', context)

def homepage(request):
    user_email = request.POST.get('email')
    user_password = request.POST.get('password')

    reference_user = users.objects.filter(email=user_email).first()

    if reference_user:
        if reference_user.email == user_email and reference_user.password == user_password:
            if reference_user.verified == 1:
                return render(request,'users/homepage.html')
            else:
                context = {
                    'registered_user':'Código de verificação incorreto, cadastre novamente'
                }
                users.objects.filter(email=user_email).delete()
                return render(request, 'users/register.html', context)
        else:
            context = {
                'response':'Senha ou Email errado, digite novamente'
            }
            return render(request,'users/loginpage.html',context)
    else:
        return render(request, 'users/register.html', {'registered_user': 'Email não cadastrado'})

def forgot_password(request):
    return render(request, 'users/forgot_password.html')

def request_to_recover_password(request):
    user_email = request.POST.get('email')
    reference_user = users.objects.filter(email=user_email).first()

    if reference_user:
        if reference_user.verified == 1:
            send_email(user_email,'Recuperar senha',f'Ola aqui está a sua senha: {reference_user.password}')
            context = {
                'response':'Acesse o seu email para recuperar a senha'
            }
            return render(request, 'users/loginpage.html', context)
        else:
            context = {
                'response': 'Seu email não foi verificado, refaça o cadastro'
            }
            users.objects.filter(email=user_email).delete()
            return render(request, 'users/forgot_password.html', context)
    else:
        context = {
                'response':'Usuário não cadastrado'
        }
        return render(request, 'users/forgot_password.html', context)