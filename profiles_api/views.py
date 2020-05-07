from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status

from profiles_api import serializers
class HelloApiView(APIView):
    """Test the API View"""
    serializer_class = serializers.HelloSerializer
    # the above statement is for telling what serializer class are we using

    def get(self, request, format=None):
        """Returns the list of the APIView features"""
        an_api_view = [
          "Maps the HTTP Verbs as the functions that is get, post, put, patch(partial update), delete",
          "It is similar to the django views",
          "Gives you the most control over your application",
          "Is mapped manually to URLs"]
        # here we utlise the Response object that whic we have got from the Response definition if in the response.py from rest_framework
        return Response({"message": "Hello","an_api_view": an_api_view})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            print('the serializer is valid')
            name = serializer.validated_data.get('name')
            message = 'Hello {name} Suya'.format(name=name)
            return Response({"message": message})
        else:
            return Response(
                {
                    "errors": serializer.errors,"status": status.HTTP_400_BAD_REQUEST
                }
            )

    def put(self,request,pk="None"):
        """Updating only one record completely not partially"""
        return Response({"message": "Completely Updated a Record"})

    def patch(self,request,pk="None"):
        """Updating a specific field in a record"""
        return Response({"message": "Updated only certain fields in a record"})

    def delete(self, request,pk="None"):
        """Deleting a single record"""
        return Response({"message": "Deleting only one record."})
