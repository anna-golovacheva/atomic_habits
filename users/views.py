from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from users.models import User
from users.permissions import UserRetrievePermissionManager
from users.serializers import UserSerializer, RegisterSerializer


class RegisterApiView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token: http://localhost:8000/api/token/",
        })


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [UserRetrievePermissionManager]


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [UserRetrievePermissionManager]
