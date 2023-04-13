import json

from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()

    return HttpResponseNotAllowed('Only GET request are allowed')


def add(request, *args, **kwargs):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            a = int(data.get('A'))
            b = int(data.get('B'))
            result = a + b
            return JsonResponse({'answer': result})
        except (TypeError, ValueError):
            return JsonResponse({'error': 'Division by zero!'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed!'}, status=405)
