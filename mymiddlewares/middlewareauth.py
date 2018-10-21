from django.http import response
from django.utils.deprecation import MiddlewareMixin


class AuthMiddleWare(MiddlewareMixin):


    def process_request(self,request):
        pass
    def process_view(self):
        pass
    def process_template_response(self):
        pass
    def process_exception(self):
        pass
    def process_response(request):

        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET，OPTIONS"
        response["Access-Control-Max-Age"] = "1200"
        response["Access-Control-Allow-Headers"] = "*"
        return response
