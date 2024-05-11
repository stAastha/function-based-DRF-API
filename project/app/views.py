# from django.shortcuts import render
# # from django.contrib.auth.models import User
# from .models import User
# from .serializers import UserSerializer
# from rest_framework.renderers import JSONRenderer
# from django.http import HttpResponse
# import io
# import json
# from rest_framework.parsers import JSONParser

# from django.http import HttpResponse,JsonResponse

# # Create your views here.
# from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt
# def list(request):
#     if request.method =="GET":
#         user = User.objects.all()
#         serializer_data = UserSerializer(user,many=True)
#         # print(serializer_data.data)
#         json_data = JSONRenderer().render(serializer_data.data)
#         return HttpResponse(json_data,content_type = 'application/json')
    
#     elif request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         serializer = UserSerializer(data = python_data)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Data Created'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')

#     elif request.method == 'PUT':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id')
#         stu = User.objects.get(id=id)
#         # serializer = UserSerializer(stu, data=python_data, partial = True)
#         serializer = UserSerializer(stu, data=python_data)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'Data Updated !!'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')

#     # elif request.method == 'PATCH':
#     #     json_data = request.body
#     #     stream = io.BytesIO(json_data)
#     #     python_data = JSONParser().parse(stream)
#     #     id = python_data.get('id')
#     #     stu = User.objects.get(id=id)
#     #     serializer = UserSerializer(stu, data=python_data, partial = True)
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         res = {'msg':'Data Partially Updated !!!!!!!!!!!!'}
#     #         json_data = JSONRenderer().render(res)
#     #         return HttpResponse(json_data, content_type='application/json')
#     #     json_data = JSONRenderer().render(serializer.errors)
#     #     return HttpResponse(json_data, content_type='application/json') 
 
#     elif request.method == 'DELETE':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id')
#         if id:
#             stu = User.objects.get(id=id)
#             stu.delete()
#             res = {'msg': 'Data Deleted!!'}
#             return JsonResponse(res, safe=False)
#         else:
#             res = {'msg': 'id not present in Database'}
#             return JsonResponse(res)
from models import User
from serializers import UserSerializer
from rest_framework import mixins
from rest_framework import generics

class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = UserSerializer.objects.all()
    serializer_class =UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)