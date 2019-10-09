from .serializers import HelloWorldSerializer


class HelloWorldView(APIView):
    def get(self, request):
        return Response({"message": "Hello World!"})

    def post(self, request):
        serializer = HelloWorldSerializer(data=request.data)
        if serializer.is_valid():
            valid_data = serializer.data

            name = valid_data.get("name")
            age = valid_data.get("age")

            return Response({"message": "Hello {}, you're {} years old".format(name, age)})
        else:
            return Response({"errors": serializer.errors})
