from django.shortcuts import render,redirect
from login.models import Login
import random
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from customer.models import Customer

def login(request):
    if request.method == "POST":
        un = request.POST.get("username")
        ps = request.POST.get("password")

        # Check if the user exists
        user = Login.objects.filter(username=un, password=ps).first()

        if user:
            request.session["uid"] = user.u_id  # Store user ID in session
            user_type = user.type

            # Redirect based on user type
            if user_type == "admin":
                return render(request, 'temp/admin.html')
            elif user_type == "customer":
                return render(request, 'temp/customer.html')
            elif user_type == "warden":
                return render(request, 'temp/warden.html')
            elif user_type == "superindentent":
                return render(request, 'temp/suprt.html')
            else:
                context = {
                    'inv': "User type not recognized!"
                }
                return render(request, 'login/login.html', context)
        else:
            # Invalid username or password
            context = {
                'inv': "Incorrect username or password!!!"
            }
            return render(request, 'login/login.html', context)

    return render(request, 'login/login.html')




# #

def forgot_password_request(request):
    if request.method == "POST":
        username = request.POST.get("username")

        try:
            user = Login.objects.get(username=username)
            otp = str(random.randint(100000, 999999))

            # Store OTP and username in session
            request.session['otp'] = otp
            request.session['otp_user'] = username

            # Send OTP via email
            send_mail(
                'Your OTP for Password Reset',
                f'Your OTP is: {otp}',
                'cabcd332@gmail.com',
                [username],  # assuming username is an email
                fail_silently=False,
            )

            return redirect('verify_otp')

        except Login.DoesNotExist:
            return render(request, 'login/forgot_password.html', {'error': "Username not found."})

    return render(request, 'login/forgot_password.html')


def verify_otp(request):
    if request.method == "POST":
        entered_otp = request.POST.get("otp")
        new_password = request.POST.get("new_password")
        saved_otp = request.session.get("otp")
        username = request.session.get("otp_user")

        if entered_otp == saved_otp:
            try:
                user = Login.objects.get(username=username)
                user.password = new_password
                user.save(update_fields=['password'])

                # Clear session
                request.session.pop("otp", None)
                request.session.pop("otp_user", None)

                return redirect('login')
            except Login.DoesNotExist:
                return redirect('forgot_password')
        else:
            return render(request, 'login/verify_otp.html', {'error': "Invalid OTP."})

    return render(request, 'login/verify_otp.html')


