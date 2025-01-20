from django import  forms
from  . import models, parser_rezka

class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('rezka', 'rezka'),
        ('ts', 'ts'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)
    class Meta:
        fields = [
            'media_type',
        ]

    def parser_data(self):
        if self.data['media_type'] == 'rezka':
            file_rezka = parser_rezka.parsing()
            for i in file_rezka:
                models.RezkaParser.objects.create(**i)


