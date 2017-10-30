from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, etc.)',
            'It is similar to a traditional django view'
        ]

        return Response({ 'message': 'Hello!', 'an_apiview': an_apiview })
