import csv
import os

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import UrlAddressForm, CSVFileForm
from .models import UrlAddress, CSVFile
from .utils import id_generator, handle_uploaded_file
from django.conf import settings
from django.contrib.auth.decorators import login_required

# @login_required
def home(request):    
    savedUrls = UrlAddress.objects.all()
    if request.method == 'POST':
        form = UrlAddressForm(request.POST or None)
        csvform = CSVFileForm(request.POST, request.FILES)
        if csvform.is_valid():                        
            myFile = CSVFile.objects.create()
            myFile.csvfile = request.FILES['csvfile']
            myFile.save()
            
            operationFile = CSVFile.objects.all()
            path = str(operationFile[0].csvfile.path)
                        
            try:
                with open(path) as f:
                    reader = csv.reader(f, delimiter=' ', quotechar='|')
                    for row in reader:                    
                        changed_url = "http://127.0.0.1:8000/urldispatcher/" + id_generator()
                        url = UrlAddress.objects.create(original_url=', '.join(row), changed_url=changed_url)
                        url.save()
                    f.close()
            except:
                os.remove(path)
                myFile.delete()
                messages.info(request, "Podany plik musi być formatu .csv. Spróbuj ponownie.")
                
                return HttpResponseRedirect('/urlcutter')    

            
            try:
                os.remove(path)                
            except:
                pass                                    
                
            myFile.delete()
            return HttpResponseRedirect('/urlcutter')
        elif form.is_valid():
            changed_url = "http://127.0.0.1:8000/urldispatcher/" + id_generator()
            url = UrlAddress.objects.create(original_url=form.cleaned_data.get("original_url"), changed_url=changed_url)     
            url.save()
            return HttpResponseRedirect('/urlcutter')
    else:
        if not request.user.is_authenticated:
            return HttpResponseRedirect("/")
        else:
            form = UrlAddressForm()
            csvform = CSVFileForm()                            

    context = {
        "form": form,        
        "urls": savedUrls,
        "csvform": csvform,
    }        
    return render(request, 'home/home.html', context)

def urlDispatcher(request, slug):    
    inURL = "http://127.0.0.1:8000/urldispatcher/" + slug
    unitsURL = UrlAddress.objects.filter(changed_url=inURL)
    unitURL = unitsURL[0]
    return redirect(unitURL.original_url)

def urlExporter(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['Adres pierwotny', 'Adres skrócony'])

    for unit in UrlAddress.objects.all().values_list('original_url', 'changed_url'):
        writer.writerow(unit)

    response['Content-Disposition'] = 'attachment; filename="ExportURLCutter.csv"'


    return response #HttpResponseRedirect('/urlcutter') 


