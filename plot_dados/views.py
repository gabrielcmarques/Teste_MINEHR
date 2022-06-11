from django.shortcuts import render


def plot_dados(request):
    nome = 'Gabriel'
    context = {'nome': nome}
    return render(request, 'plot_dados/homepage.html' , context)
