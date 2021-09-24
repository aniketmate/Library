from Book.models import Book
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse,JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from subscribe.forms import Subscribe
from Book.model_enum import Math,Name



# Create your views here.

# def func(request):
#     return render(request,"base.html")

    # print(request)
    # print("----------------in function--------------------")
    # return HttpResponse("Hi Welcome To The Page")
    # return JsonResponse({"key":"value"})
from datetime import date

def homepage(request):
    # return HttpResponse("Hi Welcome To The Page")
    if request.method == "POST":
        data = request.POST
        if not data.get("id"):
            if data["ispub"] == "Yes":   
                Book.objects.create(name = data["nm"],
                qty = data["qty"],
                price = data["price"],
                is_published = True,
                published_date = date.today())
            elif data["ispub"] == "No":
                Book.objects.create(name = data["nm"],
                qty = data["qty"],
                price = data["price"])
                
            # if request.method == 'POST':
                # sub = Subscribe(request.POST)
                subject1 =  f"Book created with id:-{id}"
                message1 = str( Book.objects.get(name = data["nm"],
                qty = data["qty"],
                price = data["price"]))
                recepient = request.POST["email"]
    
            # if ";" in recepient:
            #     final_rec_list = recepient.split(";")
            # else:
            #     final_rec_list = [recepient]

            # send_mail(subject=subject1, message=message1, from_email=settings.EMAIL_HOST_USER,recipient_list=["aniket27061988@gmail.com"])
                
        else:
            bid = data.get("id")
            book_obj = Book.objects.get(id=bid)
            book_obj.name = data["nm"]
            book_obj.qty = data["qty"]
            book_obj.price = data["price"]
            if data["ispub"] == "Yes":   
                if book_obj.is_published:
                    pass
                else:
                    book_obj.is_published = True
                    book_obj.published_date = date.today()
            elif data["ispub"] == "No":
                   if book_obj.is_published == True:
                       pass
            book_obj.save()
                

            
        # return render(request, 'index.html', {'form1':sub})     
            
            # return render(request, 'index.html', {'form1':sub})     

        return redirect("home")

    else:
        return render(request,"home.html")


def get_books(request):
   books = Book.objects.all()
   return render(request, template_name="books.html",context={"all_books":books})
    
def delete_book(request,id):
    # print(id,"delete book id")
    Book.objects.get(id=id).delete()
    subject1 =  f"Book id deleted {id}"
    message1 =  "Book Hard deleted successfully"
    send_mail(subject=subject1, message=message1, from_email=settings.EMAIL_HOST_USER,recipient_list=["abhijeet_mate@ymail.com"])

    return redirect('showbook')

def update_book(request,id):
    subject1 =  "Book udated successfully"
    message1 = f"Book id updated:- {id}"
    send_mail(subject=subject1, message=message1, from_email=settings.EMAIL_HOST_USER,recipient_list=["aniket27061988@gmail.com"])
    return render(request,"home.html",context={"single_book": book_obj})


def soft_delete(request, id):
    book_obj = Book.objects.get(id=id)
    book_obj.is_deleted = "Y"
    book_obj.save()
    subject1 =  f"Book id deleted {id}"
    message1 =  "Book Soft deleted successfully"
    send_mail(subject=subject1, message=message1, from_email=settings.EMAIL_HOST_USER,recipient_list=["aniket27061988@gmail.com"])
    return redirect("showbook")

def active_books(request):
    # all_active_books = Book.objects.filter(is_deleted = "N")
    all_active_books = Book.active_books.all()
    return render(request, template_name="books.html",context={"all_books":all_active_books})

def in_active_books(request):
    # all_inactive_books = Book.objects.filter(is_deleted = "Y")
    all_inactive_books = Book.inactive_books.all()
    return render(request, template_name="books.html",context={"all_books":all_inactive_books, "book_status": "Inactive"})

def restore_book(request,id):
    book_obj = Book.objects.get(id=id)
    book_obj.is_deleted = "N"
    book_obj.save()
    subject1 =  "Book restored successfully"
    message1 =  f"Book id restored {id}"
    send_mail(subject=subject1, message=message1, from_email=settings.EMAIL_HOST_USER,recipient_list=["aniket27061988@gmail.com"])
    return redirect("showbook")
    
# Book.objects.create(name=Name.BOOK_NAME1.value,qty=,price=) 
    

    