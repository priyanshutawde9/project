from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from FOLDER.models import Folder
from .serializers import FolderSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from FOLDER.models import Folder 
# Create your views here.

@api_view(['GET'])
def getData(request):
    folders = Folder.objects.all().exclude(state="Bin")
    serializer = FolderSerializer(folders, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addFolder(request):
    serializer = FolderSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
        return Response(serializer.errors)

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

@api_view(['POST'])
def move_to_bin(request, folder_id):
    new_state = 'Bin'

    try:
        folder = Folder.objects.get(id=folder_id, state='Active')
    except Folder.DoesNotExist:
        return Response({'error': 'Folder not found or not in Active state'}, status=status.HTTP_404_NOT_FOUND)

    folder.state = new_state
    folder.save()

    return Response({'message': 'Folder moved to bin'}, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_bin_data(request):
    bin_data = Folder.objects.filter(state='Bin')
    serializer = FolderSerializer(bin_data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)






