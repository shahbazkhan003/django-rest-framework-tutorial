from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from .serializer import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Snippet
from .serializer import SnippetSerializer


@api_view(['GET', 'POST'])
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




# @api_view(['GET','POST'])
# def car_list(request):
#     if request.method == "GET":
#         cars = carlist.objects.all()
#         serializer = carserializer(cars,many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         data = request.data
#         print(data)
#         serializer = carserializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
        
# @api_view(['GET','PUT','DELETE'])
# def car_detail(request,pk):
#     try:
#          cars = carlist.objects.get(pk=pk)
#     except carlist.DoesNotExist:
#          return Response({'status':'not found'},status=status.HTTP_400_BAD_REQUEST)     
#     if request.method == "GET":
#         serializer = carserializer(cars)
#         return Response(serializer.data)
#     if request.method == "PUT":
#             data = request.data
#             serializer = carserializer(cars,data=data)
#             if serializer.is_valid():
#                  serializer.save()
#                  return Response(serializer.data)
#             else:
#                  return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     if request.method == "DELETE":
#          cars.delete()
#          return Response(status=status.HTTP_204_NO_CONTENT)




