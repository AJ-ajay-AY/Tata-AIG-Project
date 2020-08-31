from django.http import JsonResponse

class ErrorResponse():

    @staticmethod
    def json_500(message = '500 - Internal Server Error'):
        return JsonResponse({"data":message, 'status':False}, safe=False, status=500)

    @staticmethod
    def json_404(message= '404 - Pagenot Found'):
        return JsonResponse({"data":message, 'status':False}, safe=False, status=404)