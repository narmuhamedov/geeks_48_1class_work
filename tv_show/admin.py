from django.contrib import admin
from django.core.exceptions import ValidationError

from . import models
from PIL import Image
from django import forms

class ImageForm(forms.ModelForm):
    class Meta:
        model = models.Slider
        fields = ['image_slide']
    def clean(self):
        super().clean()
        if self.cleaned_data.get('image_slide'):
            try:
                img = Image.open(self.cleaned_data.get('image_slide'))
                width, height = img.size
                print('ширина высота', width, height)
                #Проверяем размер изображения по пикселям
                if width >=1500 or height >=900:
                    raise ValidationError(f'Размер картинки слишком большой пожалуйста загрузите 1500х900 или ниже'
                                          f'Загруженное изображение имеет размер - {width}x{height}')
            except Exception as e:
                raise ValidationError(f'Ошибка в обработке{e}')



class ImageSlideForm(admin.ModelAdmin):
    form = ImageForm



admin.site.register(models.Slider, ImageSlideForm)
admin.site.register(models.Movies)
admin.site.register(models.Reviews)
