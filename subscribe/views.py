from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
from .forms import Subscribe
s = Subscribe()



from django.conf import settings
from django.core.mail import message, send_mail,send_mass_mail,EmailMessage

# Create your views here.
#DataFlair #Send Email
def subscribe_email(request):
    print("in subscribe email")
    sub = Subscribe()
    # print(sub)
    # return HttpResponse("Hi")
    if request.method == 'POST':
        sub = Subscribe(request.POST)
        subject1 = 'Welcome to DataFlair'
        message1 = 'Hope you are enjoying your Django Tutorials'
        recepient = request.POST["email"].strip()
        print(recepient)
        if ";" in recepient:
            final_rec_list = recepient.split(";")
        else:
            final_rec_list = [recepient]
        print(final_rec_list, "final_rec_list")
        # if final_rec_list:
        #     Msg = EmailMessage(subject=subject1,body=message1,from_email=settings.EMAIL_HOST_USER,to=final_rec_list)
        #     Msg.attach_file(r"E:\aniket mate\Aniket_Django\database info.txt")
        #     Msg.send(fail_silently=False)

        send_mail(subject=subject1, message=message1, from_email=settings.EMAIL_HOST_USER,recipient_list=final_rec_list)
        # send_mail(subject, 
        #     message, settings.EMAIL_HOST_USER, [recepient], fail_silently = False)
        # return HttpResponse("hello")
        return render(request, 'success.html', {'recepient': final_rec_list})
    return render(request, 'index.html', {'form1':sub})



# print(s)

# print("abcd")