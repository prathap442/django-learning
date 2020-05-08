from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profiles_api import serializers
from rest_framework import viewsets
from profiles_api import models
from profiles_api import permissions


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


class HelloViewSet(viewsets.ViewSet):
    """Used For TEsting the ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """this would be used to perform HTTP GET for retriving list of records"""
        list_of_functions = [
          "provides the methods that will help to automatically intellisense the HTTP actions",
          "map the HTTP actions with the functions that are listed here",
          "the following are the functions that exist:",
          "the functions would be list,create,retrieve,update(PUT),partial_update(PATCH),destroy(DELETE)"
        ]
        return Response({"list": list_of_functions})

    def post(self,request):
        """this is used for the sake of the postin of the HelloViewSet"""
        serialized_data = self.serializer_class(data=request.data)
        if serialized_data.is_valid():
            print('the serialized data is')
            name = serialized_data.validated_data.get('name')
            return Response({"message": "Posting the Data With name {name}".format(name=name)})
        else:
            print('the data could not be serialized')
            return Response(serialized_data.errors,status=status.HTTP_400_BAD_REQUEST)

    def retreive(self,request,pk=None):
        """this is used to retrieve single record"""
        return Response({"message": "RETRIEVING A Single Record"})

    def destroy(self, request,pk=None):
        """this is used for the sake of destroying a single record"""
        return Response({"message": "DESTROYED A SINGle Record"})

    def update(self,request,pk=None):
        """updating the single record completely which is a PUT request"""
        return Response({"message": "Updating the record entirely"})

    def partial_update(self,request,pk=None):
        """updating the singl e record partially and is a equivalent of the PATCH request"""
        return Response({"message": "Updating the Record partially"})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and Updating of the profiles"""
    serializer_class = serializers.UserProfileSerializer
    # if we give the queryset assesment here then in the urls.py no need to mention the connection with the 
    # in the urls.py for the sake of addding of the endpoint
    queryset = models.UserProfile.objects.all()
    permission_classes = (permissions.UpdateOwnProfile,)
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)