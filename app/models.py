from tabnanny import verbose
from django.utils import timezone
from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL



class Category(models.Model):
    title = models.CharField('Категория товара', max_length=256)
    icon = models.ImageField('Иконка', upload_to='category_icons', blank=True)


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Brand(models.Model):
    title = models.CharField('Бренд товара', max_length=256)
    image = models.ImageField('Логотип', upload_to='product_logos', blank=True)


    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField('Цвет', max_length=256)
    code = models.CharField('Hex', max_length=256, null=True)


    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    def __str__(self):
        return self.title



class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', related_name='category_products')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Бренд', related_name='brand_products')
    title = models.CharField('Название товара', max_length=256)
    text = models.TextField('Описание')
    year = models.IntegerField(default=0)
    image = models.ImageField('Фото', upload_to='product_image', blank=True)
    created_at = models.DateTimeField('Дата создания',default=timezone.now())
    color = models.ManyToManyField(Color, verbose_name='Цвет', through="ProductColor")



    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты(общий)'

    def __str__(self):
        return self.title


    
class Memory(models.Model):
    size = models.IntegerField('Память', default=0)


    class Meta:
        verbose_name = 'Память'
        verbose_name_plural = 'Память'

    def __str__(self):
        return str(self.size)




class ProductColor(models.Model):
    color = models.ForeignKey(Color, on_delete=models.CASCADE, verbose_name='Цвет', related_name='color_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')


    class Meta:
        verbose_name = 'Product color'
        verbose_name_plural = 'Product color'

    def __str__(self):
        return self.product.title + ' ' + self.color.title


class ProductGallery(models.Model):
    productColor = models.ForeignKey(ProductColor, on_delete=models.CASCADE, verbose_name='Продукт', related_name='gallery_products')
    image = models.ImageField('Фото продукта', upload_to='productColor_gallery', blank=True)

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'

    def __str__(self):
        return self.productColor.product.title


class ProductColorSize(models.Model):
    productColor = models.ForeignKey(ProductColor, on_delete=models.CASCADE, verbose_name='Продукт', related_name='product_productsColors')
    memory = models.ForeignKey(Memory, null=True,  on_delete=models.CASCADE, verbose_name='Память', related_name='memory_productsColors')
    price = models.IntegerField('Цена', default=0)
    is_favourite = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


    def real_count(self):
        income = sum([storage.quantity for storage in self.storage_set.filter(storage_type = True)])
        consumption = sum([storage.quantity for storage in self.storage_set.filter(storage_type = False)])
        result = income - consumption
        return result

    def __str__(self):
        return  str(self.productColor.product) + ' ' + str(self.memory)+ 'GB' + ' ' + str(self.productColor.color.title)



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Юзер', related_name='user_carts' )
    product = models.ForeignKey(ProductColorSize, on_delete=models.CASCADE, verbose_name='Продукт', related_name='cart_products')
    quantity = models.IntegerField('Кол-во', default=0)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'

    def __str__(self):
        return str(self.user) + " " + str(self.product)



class Order(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, verbose_name='Юзер', related_name='user_orders' )
    total = models.IntegerField('Total', default=0)
    status = models.BooleanField('Status', default=False)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказ'

    def __str__(self):
        return str(self.user) 


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    product = models.ForeignKey(ProductColorSize, on_delete = models.SET_NULL, null=True)
    product_count = models.IntegerField('Количество', default=0)

    class Meta:
        verbose_name = 'Order Product'
        verbose_name_plural = 'Order Product'

    def __str__(self):
        return str(self.product) 



class Storage(models.Model):
    quantity = models.IntegerField('Кол-во товара в наличии', default = 0)  
    productColorSize = models.ForeignKey(ProductColorSize, on_delete = models.SET_NULL,   null=True, verbose_name="Продукт")   
    storage_type = models.BooleanField(default=False) 
    date = models.DateTimeField('Дата', default = timezone.now)




class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_favourites', verbose_name='User')
    productColorSize = models.ForeignKey(ProductColorSize, null=True, on_delete=models.CASCADE, related_name='product_favourites', verbose_name='Пост')

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'




    

    def str(self):
        return self.user.username




class View(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="recomendation")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="recomendation")

    

    class Meta:
        verbose_name = 'Recomendation'
        verbose_name_plural = 'Recomendations'


    def str(self):
        return self.user.product