from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from home.models import ContactForm, Contact
from order.models import Shopcart
from product.models import Category, Product


def index(request):
    category = Category.objects.all()
    products = Product.objects.order_by('image')[:5]
    content = Product.objects.all()

    current_user = request.user
    request.session['cart_items'] = Shopcart.objects.filter(user_id=current_user.id).count()
    context = {'page': 'home',
               'category': category,
               'products': products,
               'content': content,


               }
    return render(request, 'index.html', context)


def login_form(request):
    if request.method == "POST":
        next_url = request.POST['next']
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            if next_url:
                return  redirect(next_url)
            else:
                HttpResponse("Home Page")
                return redirect('/')

        # A backend authenticated the credentials
        else:
            context = {'hata': 'Username or password incorect',
            }
            return render(request, "login.html", context)
    else:
        return render(request, "login.html")
    # No backend authenticated the credentials


def join_form(request):
    return None


def login_out(request):
    logout(request)
    return redirect('/')


def show_category(request):
    return None


def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            contactdata=Contact()
            contactdata.name = form.cleaned_data['name']
            contactdata.email = form.cleaned_data['email']
            contactdata.subject = form.cleaned_data['subject']
            contactdata.save()
            messages.success(request, "Your message has been sent ,Thank you for your interest")
            return HttpResponseRedirect('/contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def panel(request):
    return render(request, 'userpanel.html' )