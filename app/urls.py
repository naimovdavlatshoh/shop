from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('sign-in', views.sign_in, name='sign_in'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('sign-out', views.sign_out, name='sign_out'),
    path('search/',views.search,name='search' ),


    path('product/<int:id>', views.product_detail, name='product_detail'),

    path('favourite/', views.favourite, name='favourite'),
    path('add-favourite/', views.add_favourite, name ='add_favourite'),

    path('cart/', views.cart, name='cart'),
    path('addToCart/', views.addToCart, name='addToCart'),
    path('cartPlus/', views.cartPlus, name='cartPlus'),
    path('cartMinus/', views.cartMinus, name='cartMinus'),

    path('new-order/', views.new_order, name='new_order'),
    path('order-detail/<int:id>/', views.order_detail, name='order_detail'),


    path('settings/index.html', views.settings, name='settings'),


    # Admin panel
    path('user/product', views.admin_product, name='admin_product'),
    path('user/product-image/<int:id>/', views.admin_product_image_edit, name='admin_product_image_edit'),

    path('user/product-color/<int:id>', views.admin_product_detail, name='admin_product_detail'),
    path('user/create/product', views.product_create, name='product_create'),
    
    # Product Color 
    path('user/create/productColor/<int:id>/', views.productColor_create, name='productColor_create'),
    path('user/delete/productColor/<int:id>/', views.productColor_delete, name='productColor_delete'),

    # Product Color size
    path('user/create/productColorSize/<int:id>/', views.productColorSize_create, name='productColorSize_create'),
    path('user/delete/productColorSize/', views.productColorSize_delete, name='productColorSize_delete'),
    path('user/edit/productColorSize/', views.productColorSize_edit, name='productColorSize_edit'),


    # Product Color Size Gallery

    path('user/gallery/productColor/<int:id>/', views.productColor_gallery, name='productColor_gallery'),
    path('user/gallery/productColor/<int:id>/create', views.productColor_gallery_create, name='productColor_gallery_create'),
    path('user/gallery/productColor/remove', views.productColor_gallery_remove, name='productColor_gallery_remove'),

    # Storage
    path('storage/', views.storage, name='storage'),
    path('storage-detail/<int:id>/', views.storage_detail, name='storage_detail'),
    path('storage/<int:id>/', views.storage_reload, name='storage_reload'),



    path('personal/', views.personal, name='personal'),
    path('moveEditPersonal/', views.moveEditPersonal, name ='moveEditPersonal'),
    path('editpersonal/', views.editPersonal, name ='editPersonal'),
    path('user/', views.user, name ='user'),
    path('category/', views.category, name ='category'),
    path('category-detail/<int:id>/', views.category_detail, name='category_detail'),





    
]
