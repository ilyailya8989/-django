from django.urls import path

from jobapp import views

urlpatterns = [
    path('osnova', views.osnova, name='osnova'),
    path('osnova/add', views.add_cat, name='osnova_add'),
    path('osnova/del/<int:info_id>', views.del_cat, name='osnova_del'),
    path('category/edit/<int:category_id>', views.change_cat_page, name="change_category_page"),
    path('osnova/change/<int:info_id>', views.change_cat, name='osnova_change'),
    path('info_kategory/<int:info_id>', views.infoKategory, name='info_category')
]