from tkinter.messagebox import RETRY
from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from .serializers import RegisterSerializer, UserDetailSerializer, UserLeaderSerializer,UserStatusSerializer
from .models import User


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class RegisterAPIView(generics.GenericAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = RegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "id": user.id,
            "email": user.email,
            "token": get_tokens_for_user(user),
        })
        

class UserDetailAPIView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
    
    
class UserStatusAPIView(generics.UpdateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserStatusSerializer
    
    
    def update(self, request, *args, **kwargs):
        instanse = self.get_object()
        last_status = instanse.is_active
        serializer = self.get_serializer(instanse, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'id': serializer.data['id'],
                'new_status': serializer.data['is_active'],
                'last_status': last_status
            })
        else:
            return Response({
                'message': 'Please type correct value'
            })
            
class UserLeaderAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserLeaderSerializer
    permission_classes = (IsAdminUser,)
    
    
    def update(self, request, *args, **kwargs):
        instanse = self.get_object()
        serializer = self.get_serializer(instanse, data=request.data, partial=True)
        if serializer.is_valid():
            check_leader = User.objects.get(id=request.data['leader']) 
            if instanse.is_staff:
                print(serializer.data)
                print(instanse)
                return Response({
                    'message': 'The user is the leader'
                })
            if check_leader.is_staff:
                serializer.save()
                return Response({
                    'staff_id': serializer.data['id'],
                    'leader_id': serializer.data['leader'],
                    'message': 'Successfully changed'
                })
            else:
                return Response({
                    'message': 'The leader_id is not Leader'
                })
        else:
            return Response({
                'message': 'Some error'
            })
    
        
        
