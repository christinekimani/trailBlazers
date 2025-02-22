from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    # Render an HTML template for the home page
    return render(request, 'home/index.html')
def about_us(request):
    return render(request, 'home/about_us.html')

def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        ContactMessage.objects.create(name=name, email=email, subject=subject, message=message)
        messages.success(request, "Your message has been sent!")
        return redirect('contact_us')
    return render(request, 'home/contact_us.html')

def map_view(request):
    return render(request, 'home/gallery.html')
