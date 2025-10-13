from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import PostSerializer, CategorySerializer
from blog.models import Post, Category
from rest_framework import status, mixins
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import (
    GenericAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .paginations import DefaultPagination
from .filters import PostFilter


"""@api_view(["GET", "POST"])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_list_view(request):
    if request.method == "GET":
        post = Post.objects.filter(status=True)
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def post_detail_view(request, id):
        
        
        # retrieving /  editing / deleting post
        
    # try:
        post = get_object_or_404(Post,id=id)
        if request.method == "GET":
            serializer = PostSerializer(post)
            return Response(serializer.data)
        elif request.method == "PUT":
            serializer = PostSerializer(post, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        elif request.method == "DELETE":
             post.delete()
             return Response({'detail':'item removed successfully'}, status=status.HTTP_204_NO_CONTENT)

    # except Post.DoesNotExist:
    #     return Response({'detail':'post does not exit'}, status=status.HTTP_404_NOT_FOUND)


    """


'''class PostListView(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    
    def get(self, request):
        """
        Retrieving post list
        """
        post = Post.objects.filter(status=True)
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        """
        creating post
        """
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)'''


'''class PostListView(GenericAPIView):

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def get(self, request):
        """
        Retrieving post list
        """
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)'''

"""class PostListView(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)"""


class PostListView(ListCreateAPIView):

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)


'''class PostDetail(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    
    def get(self, request, id):
        """
        Retrieving post list
        """
        post = get_object_or_404(Post,id=id)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
    
    def put(self, request, id):
        """
        creating post
        """
        post = get_object_or_404(Post,id=id)
        serializer = self.serializer_class(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
         
    def delete(self, request, id):
        """
        deleting post
        """
        post = get_object_or_404(Post,id=id)
        post.delete()
        return Response({'detail':'item removed successfully'}, status=status.HTTP_204_NO_CONTENT)'''


class PostDetailView(RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)


"""class PostViewSet(viewsets.ViewSet):

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        post = get_object_or_404(self.queryset,id=pk)
        serializer = self.serializer_class(post)
        return Response(serializer.data)


    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def update(self, request, pk=None):
        post = get_object_or_404(self.queryset,id=pk)
        serializer = self.serializer_class(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        
        post = get_object_or_404(self.queryset,id=pk)
        serializer = self.serializer_class(post, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        post = get_object_or_404(self.queryset,id=pk)
        post.delete()
        return Response({'detail':'item removed successfully'}, status=status.HTTP_204_NO_CONTENT)"""


class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['author', 'category']
    search_fields = ["title", "content"]
    ordering_fields = ["published_date"]
    pagination_class = DefaultPagination
    filterset_class = PostFilter


class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
