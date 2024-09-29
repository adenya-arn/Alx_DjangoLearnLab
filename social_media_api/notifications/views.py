from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Notification



class NotificationViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        user = request.user
        notifications = user.notifications.filter(unread=True).order_by('-timestamp')
        data = [{"actor": n.actor.username, "verb": n.verb, "target": str(n.target), "timestamp": n.timestamp} for n in notifications]
        return Response(data)
