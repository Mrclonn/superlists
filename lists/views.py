from django.http import HttpResponse

# Create your views here.
def home_page(request):
	''' домашная страница '''
	return HttpResponse('<html><title>To-Do lists</title></html>')