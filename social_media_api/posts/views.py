from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework import filters, generics
from .models import Post, Like
from notifications.models import Notification
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


@action(detail=True, methods=['post'])
class LikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        # Fetch the post
        post = generics.get_object_or_404(Post, pk=pk)

        # Create a Like instance
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if created:
            # Create a notification for the post's author
            Notification.objects.create(
                recipient=post.author,  # Assuming Post has an author field
                actor=request.user,
                verb='liked',
                target=post  # Post object being liked
            )
            return Response({'message': 'Post liked.'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'You already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)


@action(detail=True, methods=['post'])
class UnlikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        post = generics.get_object_or_404(Post, pk=pk)

        try:
            # Attempt to remove the like
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return Response({'message': 'Post unliked.'}, status=status.HTTP_204_NO_CONTENT)
        except Like.DoesNotExist:
            return Response({'message': 'You have not liked this post.'}, status=status.HTTP_400_BAD_REQUEST)


class FeedView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # Get the current user
        user = request.user

        # Get all users that the current user is following
        following_users = user.following.all()  # Assuming 'following' is the ManyToMany field in your User model

        # Fetch posts from the followed users, ordered by creation date
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')  # Adjust the field name as necessary

        # Serialize the posts
        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)