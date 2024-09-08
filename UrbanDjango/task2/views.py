from django.shortcuts import render


def shab_class(request):
    return render(request, 'class_template.html')


def shab_func(request):
    return render(request, 'func_template.html')

def shab_main(request):
    return render(request, 'main_template.html')