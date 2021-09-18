from django.shortcuts import render


# Create your views here.
def home_page(request):
    context: dict = {}
    return render(request=request, template_name='lists/index.html', context=context)
