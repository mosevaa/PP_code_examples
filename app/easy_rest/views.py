from rest_framework.response import Response
from rest_framework.views import APIView


class UserInfoView(APIView):
    def get (self, request):
        return Response({'name': 'John', 'surname': 'Jackson', 'age': 21})
