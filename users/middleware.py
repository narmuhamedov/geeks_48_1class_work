from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest

class AgeClubMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/register/' and request.method == 'POST':
            age = int(request.POST.get('age'))
            if age < 7:
                return HttpResponseBadRequest("Вы сликом малы приходите на следующий год")
            elif age >=7 and age < 12:
                request.club = 'Детский клуб'
            elif age  >=12 and age < 18:
                request.club = 'Подростковый клуб'
            elif age >=18 and age <= 60:
                request.club = 'Взрослый клуб'
            else:
                return HttpResponseBadRequest('Ваш возраст больше 60 извните вы не проходите')
        elif request.path == '/register/' and request.method == 'GET':
            setattr(request, 'club', 'Клуб не определен')


