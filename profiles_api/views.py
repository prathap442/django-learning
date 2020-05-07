from rest_framework.views import APIView
from rest_framework.response import Response 

class HelloApiView(APIView):
    """Test the API View"""

    def get(self, request, format=None):
        """Returns the list of the APIView features"""
        an_api_view = [
          "Maps the HTTP Verbs as the functions that is get, post, put, patch(partial update), delete",
          "It is similar to the django views",
          "Gives you the most control over your application",
          "Is mapped manually to URLs"]
        # here we utlise the Response object that whic we have got from the Response definition if in the response.py from rest_framework
        return Response({"message": "Hello","an_api_view": an_api_view})