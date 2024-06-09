from django.shortcuts import render, get_object_or_404, redirect

from jobapp.models import Category, Post


# Create your views here.
def osnova(request):
    ctx={
        'data': Category.objects.all()
    }
    return render(request, 'jobapp/osnova.html', context=ctx)


def infoKategory(request, info_id):

    post = Post.objects.filter(id=info_id)
    ctx={
        'info': post
    }
    return render(request, 'jobapp/info_kategory.html', context=ctx)


def add_cat(request):
    print(request.POST.get('product_name'))
    category = Category()
    category.name = request.POST.get('product_name')
    category.save()
    return redirect('osnova')


def del_cat(request, info_id):
    cat = Category.objects.get(id=info_id)
    cat.delete()
    return redirect('osnova')



def change_cat_page(requesdt, category_id):
    category = Category.objects.get(pk=category_id)
    ctx = {
        'category':category
    }
    return render(requesdt, 'jobapp/category_edit.html', context=ctx)




def change_cat(request, info_id):
    category = Category.objects.get(id=info_id)
    category.name = request.POST.get('category_name')
    category.save()
    return redirect('osnova')