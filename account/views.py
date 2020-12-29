from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate, get_user_model
from django.contrib import messages

from .forms import LoginForm

def login_view(request):    
    if request.method == 'POST':
        form = LoginForm(request.POST or None)        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            # isConfirmed = EmailConfirmed.objects.get(user = user).confirmed
            if user is not None:
                login(request, user)
                messages.success(request, "Witaj. Jesteś zalogowany.")
                return HttpResponseRedirect("/urlcutter")
                
                # if isConfirmed:
                #     login(request, user)
                #     messages.success(request, "Witaj. Jesteś zalogowany.")
                #     return HttpResponseRedirect("/catalog-her")
                # else:
                #     messages.info(request, "Twoje konto jest nieaktywne. Sprawdź swój email, aby je aktywować.")
            else:
                messages.info(request, "Użytkownik nie istnieje. Sprawdź nazwe/hasło.")

            # if isConfirmed:
            #     login(request, user)
            #     messages.success(request, "Witaj. Jesteś zalogowany.")
            # else:
            #     messages.info(request, "Twoje konto jest nieaktywne. Sprawdź swój email, aby je aktywować.")
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect("/urlcutter")
        else:
            form = LoginForm()

    context = {
        "form": form,         
    }
    return render(request, "account/login.html", context)



def logout_view(request):
    logout(request)
    messages.success(request, "Zostałeś wylogowany.")

    return HttpResponseRedirect("/")

