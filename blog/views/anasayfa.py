from django.shortcuts import render

def anasayfa(request):
    context = {
        'isim':'Hasan Topan'
    }
    return render(request, 'pages/anasayfa.html', context=context)

    