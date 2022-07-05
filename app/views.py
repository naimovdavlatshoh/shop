

from opcode import stack_effect
from django import views
from django.shortcuts import render, redirect,reverse
from django.contrib.auth import authenticate, login, logout
from . models import Brand, Category, Product, Memory, ProductGallery, ProductColor, ProductColorSize, Cart, Order, OrderProduct, Color, Storage, Favourite, View
from users.forms import CustomUserCreationForm
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from users.forms import CustomUserCreationForm
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.db.models import Count, Q


def index(request):
    products = Product.objects.order_by('-id')
    categories = Category.objects.all()
    return render(request, 'pages/index.html',  {'products':products, 'categories':categories})



    


def category_detail(request, id):   
    category = Category.objects.get(id=id)  
    return render(request, 'pages/category-detail.html', {'category':category})



def product_detail(request, id):

    product = Product.objects.get(id=id)
    productColors = product.productcolor_set.all()

    if request.user.is_authenticated:
        if not View.objects.filter(user=request.user).filter(product=product).exists():
            view = View()
            view.product = product
            view.user = request.user
            view.save()


    
    
    
    return render(request, 'pages/product-detail.html', {'productColors':productColors, 'product':product})


def cart(request):
    cart = Cart.objects.filter(user=request.user)
    return render(request, 'pages/cart.html', {'cart':cart})


@csrf_exempt
def cartPlus(request):
    cart_id = request.POST.get('cart_id')
    quantity = request.POST.get('quantity')

    cart = Cart.objects.get(id=cart_id)



    productColorSize = cart.product

    income = sum([storage.quantity for storage in productColorSize.storage_set.filter(storage_type = True)])
    consumption = sum([storage.quantity for storage in productColorSize.storage_set.filter(storage_type = False)])
    count = income - consumption



    if count == cart.quantity:
        return HttpResponse('limited')
    else:
        cart.quantity += 1
        cart.save()
        
        return HttpResponse('added')
    
   

@csrf_exempt
def cartMinus(request):
    cart_id = request.POST.get('cart_id')
    quantity = request.POST.get('quantity')
    
    cart = Cart.objects.get(id=cart_id)

    if quantity == '1':
        cart.delete()
        return HttpResponse('removed')
    else:
        cart.quantity -= 1
        cart.save()
        return HttpResponse('ok')
        

@csrf_exempt
def addToCart(request):
    user = request.user
    data = request.POST.get('product')
    product = ProductColorSize.objects.get(id=data)

    if Cart.objects.filter(user=user).filter(product=product).exists():
        cart = Cart.objects.filter(user=user).get(product=product)
        
        cart.quantity = cart.quantity + 1
        cart.save()
        return HttpResponse('exist')
    else:
        cart = Cart()
        cart.product = product
        cart.quantity = 1
        cart.user = user
        cart.save()
        return HttpResponse('new')


# Auth

def sign_in(request):
    message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
      
        if user is not None :
            login(request, user)
            return redirect('index')
        else:
            message = 'Такого пользователя не существует.'   
            return HttpResponse(message)
           
    else:
        return render(request, 'pages/sign_in.html')


def sign_out(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')


def sign_up(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('index')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():  
            user = form.save()
            login(request, user)
            # messages.success(request, 'Account created successfully')
            return redirect('index')
        else:
            messages = ValidationError(list(form.errors.values()))
            return render(request, 'pages/sign_up.html', {'form':form, 'messages':messages})
           
    else:
        form = CustomUserCreationForm()
        return render(request, 'pages/sign_up.html', {'form':form})


# Order

def new_order(request):
    if request.method == "POST":
        total = request.POST.get('total')
        if Cart.objects.filter(user = request.user).exists():
            order = Order()
            order.user = request.user
            order.total = total
            order.save()
            for item in Cart.objects.filter(user = request.user):
                orderProduct = OrderProduct()
                orderProduct.order = order
                orderProduct.product = item.product
                orderProduct.product_count = item.quantity
                orderProduct.save()

                storage = Storage()
                storage.productColorSize = item.product
                storage.quantity = item.quantity
                storage.save()

        return redirect(reverse('order_detail', kwargs={'id':order.id}))
    

def order_detail(request, id):
    order = Order.objects.get(id=id)
    return render(request, 'pages/order.html', {'order':order})
    

# User

def settings(request):
    return render(request, 'pages/settings/index.html')


def user_data(request):
    return render(request, 'pages/settings/data.html')


# Admin panel

def admin_product_image_edit(request, id):
    if request.method == "POST":
        product = Product.objects.get(id=id)
        if request.POST.get('image') == '':
            product.save()
        else:
            myfile = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            product.image = filename
            product.save()

        return redirect('admin_product')



def admin_product(request):
    products = Product.objects.order_by('-id')
    return render(request, 'pages/admin/product.html', {'products':products})


def admin_product_detail(request, id):
    productColor = ProductColor.objects.get(id=id)
    sizes = Memory.objects.order_by('size')

    colors = Color.objects.order_by('-id')
    return render(request, 'pages/admin/product-detail.html', {'productColor':productColor, 'sizes':sizes, 'colors':colors})


def product_create(request):
    if request.method == 'POST':
        
        category = request.POST.get('category')  
        brand = request.POST.get('brand')  
        title = request.POST.get('title')  
        year = request.POST.get('year')  
        text = request.POST.get('text')  

        colors_id = [int(item) for item in request.POST.getlist('colors[]')]

        product = Product()
        product.title = title
        product.year = year
        product.text = text
        
        product.category = Category.objects.get(id=category)
        product.brand = Brand.objects.get(id=brand)
        if request.POST.get('image') == '':
            product.save()
        else:
            myfile = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            product.image = filename
            product.save()
        

        for color in colors_id:
            productColorItem = ProductColor()
            productColorItem.color = Color.objects.get(id=color)
            productColorItem.product = product
            productColorItem.save()

        
        #     for size in Memory.objects.all():
        #         productColorSize = ProductColorSize()
        #         productColorSize.memory = size
        #         productColorSize.productColor = productColorItem
        #         productColorSize.save()

        #         storage = Storage()
        #         storage.productColorSize = productColorSize
        #         storage.save()


        return redirect('admin_product')
      
    else:
        brands = Brand.objects.order_by('-id')
        categories = Category.objects.order_by('-id')
        colors = Color.objects.order_by('-id')
        return render(request, 'pages/admin/create-product.html',{'brands':brands,'categories':categories, 'colors':colors })


def productColorSize_create(request, id):
    if request.method == 'POST':
        sizeId = request.POST.get('sizeId')
        price = request.POST.get('price')

        memory = Memory.objects.get(id=sizeId)
        productColor = ProductColor.objects.get(id=id)

        productColorSize = ProductColorSize()
        productColorSize.productColor = productColor
        productColorSize.memory = memory
        productColorSize.price = price
        productColorSize.save()

    
        return redirect(reverse('admin_product_detail', kwargs={'id':id}))


@csrf_exempt
def productColorSize_delete(request):
    productId = request.POST.get('productId')
    productColorSize = ProductColorSize.objects.get(id=productId)
    productColorSize.delete()
    return HttpResponse('ok')


@csrf_exempt
def productColorSize_edit(request):
 
    productId = request.POST.get('productId')
    price = request.POST.get('price')
    productColorSize = ProductColorSize.objects.get(id=productId)
    productColorSize.price = price
    productColorSize.save()
    return HttpResponse(price)


def productColor_create(request, id):
    if request.method == 'POST':
        colorId = request.POST.get('colorId')
        color = Color.objects.get(id=colorId)
        product = Product.objects.get(id=id)

        productColorItem = ProductColor()
        productColorItem.product = product
        productColorItem.color = color
        productColorItem.save()
        return redirect(reverse('productColor_create', kwargs={'id':id}))

    else:
        product = Product.objects.get(id=id)
        colors = Color.objects.order_by('title')
        return render(request, 'pages/admin/color-detail.html', {'product':product, 'colors':colors})


@csrf_exempt
def admin_product_detail_memory_edit(request):
    id = request.POST.get('id')
    price = request.POST.get('price')

    productColorSize = ProductColorSize.objects.get(id=id)

    income = sum([storage.quantity for storage in productColorSize.storage_set.filter(storage_type = True)])
    consumption = sum([storage.quantity for storage in productColorSize.storage_set.filter(storage_type = False)])
    count = income - consumption

    productColorSize.price = price
    productColorSize.save()

    return HttpResponse(count)
      

def productColor_delete(request, id):
    if request.method == 'POST':
        answer = request.POST.get('answer')
        
        if answer == 'delete':
            productColors = request.POST.getlist('productColor')
      
            for item_id in productColors:
                productColor = ProductColor.objects.get(id=item_id)
                productColor.delete()
        
    
        
        return redirect(reverse('admin_product_detail', kwargs={'id':id}))


def productColor_gallery(request, id):
    productColor = ProductColor.objects.get(id=id)
    gallery = ProductGallery.objects.filter(productColor=productColor)
    return render(request, 'pages/admin/product-detail-gallery.html',  {'gallery':gallery, 'productColor':productColor})


def productColor_gallery_create(request, id):
    if request.method == 'POST':
        productColor = ProductColor.objects.get(id=id)
        images = request.FILES.getlist('image[]')
        for image in images:
            gallery = ProductGallery()
            gallery.productColor = productColor
            myfile = image
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            gallery.image = filename
            gallery.save()  
        return redirect(reverse('productColor_gallery', kwargs={'id':id}))


@csrf_exempt
def productColor_gallery_remove(request):
  
    imageId = request.POST.get('imageId')

    productColor = ProductGallery.objects.get(id=imageId)
    productColor.delete()

    return HttpResponse('ok')



def storage(request):
    products = ProductColorSize.objects.order_by('-id')
    return render(request, 'pages/admin/storage.html', {'products':products})


def storage_reload(request, id):
    if request.method == 'POST': 
        product = ProductColorSize.objects.get(id = id)
        quantity = request.POST.get('quantity')

        product.storage_set.create(
            storage_type = request.POST.get('answer'),
            quantity = quantity,
        )


        # storage = Storage()
        # storage.productColorSize = product
        # storage.storage_type = request.POST.get('storage_type'),
        # storage.quantity = quantity
        # storage.save()
        
        return redirect('storage') 



def storage_detail(request, id):
    product = ProductColorSize.objects.get(id=id)

    storage = Storage.objects.filter(productColorSize=product)
    
    return render(request, 'pages/admin/storage-detail.html', {'storage':storage})




def search(request):
    if request.method == 'GET' and 'search' in request.GET:
        query = request.GET.get('search')
        products = Product.objects.filter(
            Q(title__icontains=query)
        )
      
        
        return render(request, 'pages/settings/search.html',{'products':products, 'query':query})
    else:
        
        return render(request, 'pages/settings/search.html',{'products':products, 'query':query})


def favourite(request):
    if request.user.is_authenticated:
        user = request.user
        favourites = user.user_favourites.all()
        return render(request, 'pages/settings/favourite.html',{'favourites':favourites})
    else:
        return redirect('index')







@csrf_exempt
def add_favourite(request):
    if request.method == "POST":

        sizeId = request.POST.get('sizeId')
        user = request.user
        productColorSize = ProductColorSize.objects.get(id=sizeId)
        if Favourite.objects.filter(user=user).filter(productColorSize = productColorSize).exists():
            favourite = Favourite.objects.filter(user=user).get(productColorSize = productColorSize)         
            favourite.delete()
            productColorSize.is_favourite=False   
            productColorSize.save()  
            return HttpResponse('deleted')
        else:

            favourite = Favourite()
            favourite.user = user
            favourite.productColorSize = productColorSize
            favourite.save()
            productColorSize.is_favourite=True  
            productColorSize.save()         


            return HttpResponse('ok')


def personal(request):
    return render (request, 'pages/settings/personal.html')

def moveEditPersonal(request):
    return render (request, 'pages/settings/edit-personal.html')



def user(request):
    return render (request, 'pages/settings/user.html')



def category(request):
    categories = Category.objects.all()
    return render(request, 'pages/category.html',  {'categories':categories})

def editPersonal(request):
    if request.user.is_authenticated:
        
        if request.method == 'POST':
            user = request.user
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            date = request.POST.get('date')
            # image = request.POST.get('image')
            gender = request.POST.get('gender')
            passport = request.POST.get('passport')
            address = request.POST.get('address')
            number = request.POST.get('number')
            
            
            user.first_name = firstname
            user.last_name = lastname
            user.date = date
            # user.image = image
            user.gander = gender
            user.pasport = passport
            user.address = address
            user.number = number        
            user.save()
            return render(request, 'pages/settings/personal.html')
        else:
            return render(request, 'pages/settings/personal.html')
  

    else:
        return render("ok")




























# def admin_product_detail_memory_more(request, id, productId):
#     if request.method == 'POST':
    
#         price = request.POST.getlist('price')
#         memory = request.POST.getlist('memory')

     
#         productColor = ProductColor.objects.get(id=id)

#         for item in range(0, len(price)):
#             product = ProductColorSize()
#             product.price = price[item]
#             size = Memory.objects.get(id=memory[item])
#             product.memory = size
#             product.productColor = productColor

#             product.save()

#         return redirect(reverse('admin_product_detail', kwargs={'id':productId}))
        

# def admin_product_detail_memory_create(request,id, productId):
#     if request.method == "POST":
#         sizeId = request.POST.get('size')

#         productColor = ProductColor.objects.get(id=id)
#         price = request.POST.get('price')
#         size = Memory.objects.get(id=sizeId)

#         productColorSize = ProductColorSize()
#         productColorSize.price = price
#         productColorSize.memory = size
#         productColorSize.productColor = productColor
#         productColorSize.save()

#         return redirect(reverse('admin_product_detail', kwargs={'id':productId}))
        
