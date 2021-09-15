from django.http import HttpResponse


# Create your views here.
def home_page(request):
    html_response: str = "<html><body>HomePage</body></html>"
    return HttpResponse(html_response)
