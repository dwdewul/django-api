from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import HelloSerializer
from rest_framework import status


class HelloAPIView(APIView):
    """Test API View"""

    serializer_class = HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, etc.)',
            'It is similar to a traditional django view'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""

        serializer = HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {}'.format(name)
            return Response({'message': message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Updates an object"""

        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Only update fields provided in request"""

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """Delete a specified object"""

        return Response({'method': 'delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            'Users actions (list, create, retrieve, update, partial_update)',
            'automatically maps to URLs using routers',
            'More fnctionality with less code'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})
