

from .serializers import TodoSerializer
from .models import Todo
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import  IsAuthenticated
from rest_framework import status
from rest_framework.exceptions import NotFound


    

    
class LoginView(ObtainAuthToken):
     def post(self, request, *args, **kwargs):
        serializer = self.serializer_clas(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
        
class TodoItemView(APIView):
   
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True,)
        return Response(serializer.data)
    
    
    def post(self, request, format=None):
        
        serializer = TodoSerializer(data=request.data)
        

        if serializer.is_valid():
            serializer.save(author=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        try:
            todo = Todo.objects.get(pk=pk)
            todo.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Todo.DoesNotExist:
            raise NotFound(detail="Todo not found", code=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, format=None):
       
        todo_id = request.data.get('pk')  
        try:
            todo = Todo.objects.get(pk=todo_id)
        except Todo.DoesNotExist:
            return Response({'error': 'Todo nicht gefunden'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def patch(self, request, format=None):
        try:
            todo = Todo.objects.get(pk=request.data.get('pk')  )
        except Todo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TodoSerializer(todo, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
