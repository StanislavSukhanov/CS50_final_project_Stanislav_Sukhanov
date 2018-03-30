from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
from django.utils.html import mark_safe
from django.contrib.auth.models import User

# Create your models here.
class Sets(models.Model):

    ''' Model representing a set (box with candies) '''

    name = models.CharField(max_length=40, help_text="Enter a name of an item")
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of an item")
    image = models.ImageField(blank=True, null=True, upload_to="sets_images")
    price = models.IntegerField(default=0, null=True, blank=True, help_text="Entrer a price here")
    weight = models.CharField(max_length=4, null=True, blank=True, help_text="Enter a weight in grams here")
    candy_item = models.ManyToManyField('Candy', blank=True, help_text='Select a candy for this set')

    # declare a tuple witth tuples key-value pairs. Key will be stored in DB, value - to represent a status in the selection list
    ITEM_STATUS = (
        ('a', 'Available'),
        ('d', 'Under development'),
        ('o', 'Out of stock'),
        ('i', 'In production'),
    )

    status = models.CharField(max_length=1, choices=ITEM_STATUS, default='d', blank=True, help_text='Item availability')

    def __str__(self):
        ''' String represeting the model object '''
        return self.name

        #return '<img src={0} alt="chirkova" width="50" height="50"/> {1}'.format(self.image, self.name)

    def image_tag(self):
        return mark_safe('<img src=/media/{0} width="40" height="40">'.format(self.image))
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def get_absolute_url(self):
        ''' Returns an URL to access a detail record of this set '''
        return reverse('set-detail', args=[str(self.id)])

    def display_candy(self):
        pass

class Candy(models.Model):

    ''' Model represetning a candy '''
    # represents what is inside of a candy
    name = models.CharField(max_length=100, blank=True, null=True, help_text="Enter a name of a candy")
    image = models.ImageField(blank=True, null=True, upload_to="candies_images/%Y/%M/%D")
    description = models.TextField(max_length=1000, help_text="Enter a brief description of an item")

    class Meta:
        permissions = (('can_update_models', 'Can update models'),    )
        ordering = ["name"]

    def __str__(self):
        return self.name
        #return '<img src={0} alt="chirkova" width="50" height="50"> {1}'.format(self.image, self.name)

class Bar(models.Model):

    size = models.ForeignKey('Size', blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField(max_length=1000, help_text="Enter a description of the item")
    image = models.ImageField(blank=True, null=True, upload_to='bars_images')

    def __str__(self):
        return self.description

    def image_tag(self):
        return mark_safe('<img src=/media/{0} width="40" height="40">'.format(self.image))
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

#Applies both for DrawWalls and DrawBars
class Size(models.Model):
    height = models.CharField(max_length=10, help_text="enter a height in cm.")
    width = models.CharField(max_length=10, help_text="enter a height in cm.")
    price = models.CharField(max_length=5, help_text="enter a price here.")

    def __str__(self):
        return '{0}cm. x {1}cm. price: {2} uah.'.format(self.height, self.width, self.price)

class ProductInBasket(models.Model):
    session_key = models.CharField(max_length=100, default=None)
    product_name = models.CharField(max_length=50, blank=True, null=True, default=None,)
    number = models.IntegerField(default=1);
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)


    def __str__(self):
        return "{}" .format(self.product_name)

    class Meta:
        verbose_name = "Item in Basket"
        verbose_name_plural = "Items in Basket"

    def save(self, *args, **kwargs):
        self.total_price = int(self.price_per_item) * int(self.number)


        super(ProductInBasket, self).save(*args, **kwargs)

class Order(models.Model):
    order_id = models.AutoField(primary_key=True,)

