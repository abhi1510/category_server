from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from product.models import Category
from product.serializers import CategorySerializer
from product.filters import CategoryFilter
from product.tasks import trigger_email


class CategoryList(APIView):
    '''
    Lists all the categories and create a category
    '''

    def get(self, request):
        categories = Category.objects.all()
        category_filter = CategoryFilter(request.GET, queryset=categories)
        serializer = CategorySerializer(category_filter.qs, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # Send email 
            email_sub = 'Category Created'
            email_msg = 'New Category Name: {}'.format(serializer.data.get('name'))
            # trigger_email.delay(email_sub, email_msg)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetail(APIView):
    '''
    Retrieve, update or delete a category instance.
    '''

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, _, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, context={'request': _})
        return Response(serializer.data)

    def put(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, _, pk):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
