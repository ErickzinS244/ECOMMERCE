from django.shortcuts import render

def index(request): #vai fazer uma requisição ao servidor
    return render(request,'index.html')#trazendo a pagina ao html

def contato(request):
    return render(request,'contato.html')

def produto(request):
    return render(request,'produto.html')
