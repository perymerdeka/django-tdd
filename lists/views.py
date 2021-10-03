from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_page(request):
    context: dict = {
        'new_item_text': request.POST.get('item_text', '')
    }
    if request.method == 'POST':
        return HttpResponse(request.POST, ['item_text'])
    return render(request=request, template_name='lists/index.html', context=context)
