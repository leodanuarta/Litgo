from django.db import models
from colorfield.fields import ColorField
from django.forms import ValidationError
from django.core.validators import RegexValidator

# Create your models here.

class UpdateOnlyManager(models.Manager):
    
    def create(self, *args, **kwargs):
        # Melarang operasi create() dengan raising exception
        raise NotImplementedError("You cannot use create() with this manager.")

    def bulk_create(self, *args, **kwargs):
        # Melarang operasi bulk_create() dengan raising exception
        raise NotImplementedError("You cannot use bulk_create() with this manager.")


class aboutus(models.Model):
    name = 'Aboutus CMS'
    title = models.TextField()
    image = models.ImageField(upload_to='static/img/aboutus')

    def __str__(self) :
        return self.name


class sliders(models.Model):
    titleImage = models.CharField(max_length=256)
    image = models.ImageField(upload_to='static/img/sliders')
    descImage = models.TextField()
    colorBackground = ColorField(verbose_name='color', default='#FFFFFF')
    colorBackground = ColorField(image_field="image")


    def __str__(self) :
        return self.titleImage

def validate_nomor_hp(value):
    if '0' in value or '+' in value:
        raise ValidationError("Nomor handphone tidak boleh mengandung angka 0 atau tanda '+'.")
    
phone_regex = RegexValidator(
    regex=r'^08\d{8,}$',
    message="Nomor telepon harus dimulai dengan '08' dan memiliki panjang minimal 10 karakter (termasuk '08')."
)

url_regex = RegexValidator(
    regex=r'^(http|https)://[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4})(:[0-9]+)?(/.*)?$',
    message="URL tidak valid. Pastikan formatnya benar, seperti 'http://www.example.com'."
)

class footers(models.Model):
    name = 'Footer CMS'
    nomor_hp = models.CharField(max_length=15, validators=[phone_regex])
    link_instagram = models.CharField(max_length=200, validators=[url_regex])
    link_tokopedia = models.CharField(max_length=200, validators=[url_regex])
    link_blibli = models.CharField(max_length=200, validators=[url_regex])
    link_shopee = models.CharField(max_length=200, validators=[url_regex])

    def __str__(self) :
        return self.name

class logos(models.Model):
    name = 'Logo CMS'
    image = models.ImageField(upload_to='static/img/logo')

    def __str__(self) :
        return self.name
