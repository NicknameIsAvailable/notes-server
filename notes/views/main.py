class Main(APIView):
    def get(self):
        try:
            response = {
                "success": True,
                "server": "OK"
            }
            return Response(response, status=status.HTTP_200_OK, content_type="application/json")
        except Exception as e:
            response = {
                "success": False,
                "error": e
            }
            print(e)
            return Response(response, status=status.HTTP_400_BAD_REQUEST, content_type="application/json")
