from .models import about ,Category, Txt ,contact
from django.shortcuts import render, get_object_or_404



def home(request):
    categories = Category.objects.all()
    txts = Txt.objects.all()
    context = {
        'categories': categories,
        'txts': txts,
    }
    return render(request, 'home.html', context)



def txt_detail(request, txt_id):
    txt = get_object_or_404(Txt, id=txt_id)
    return render(request, 'txt_detail.html', {'txt': txt})


def about_view(request):
    about_instance = about.objects.first()
    return render(request, 'about.html', {'about': about_instance})


def contact_view(request):
    contact_instance = contact.objects.first()
    return render(request, 'contact.html', {'contact': contact_instance})


def category_list_view(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def category_detail_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Txt.objects.filter(categorry=category)
    return render(request, 'category_detail.html', {'category': category, 'posts': posts})

def post_detail_view(request, txt_id):
    post = get_object_or_404(Txt, id=txt_id)
    return render(request, 'post_detail.html', {'post': post})
