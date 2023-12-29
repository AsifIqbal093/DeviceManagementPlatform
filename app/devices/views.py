from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from .serializers import DeviceSerializer
from .models import DevicesInfo


class DevicesListView(generics.ListCreateAPIView):
    """
    A view for listing and creating device objects.

    This view requires authentication for access and filters the queryset
    based on the user's role.
    """

    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Returns the queryset of device objects based on the user's role.

        If the user has a role of 'lev_operator', 'lev_engineer', or
        'lev_manager', all device objects are returned.
        If the user has a role of 'owner', only the device objects
        owned by the user are returned.
        """
        user = self.request.user
        if user.role in ['lev_operator', 'lev_engineer', 'lev_manager']:
            return DevicesInfo.objects.all()
        elif user.role == 'owner':
            return DevicesInfo.objects.filter(owner=user.id)

    def perform_create(self, serializer):
        """
        Saves the created device object with the owner set to the
        current user if the user has a role of 'owner'.
        """
        user = self.request.user
        if user.role == 'owner':
            serializer.save(owner=user)


class DevicesDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role in ['lev_manager', 'owner']:
            return DevicesInfo.objects.filter(owner=user)

    def get_object(self):
        user = self.request.user
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs['pk'])
        if user.role == 'owner' and obj.owner != user:
            # If the user is an owner, they can only access their own devices
            raise PermissionDenied(
                "You do not have permission to access this DevicesInfo."
            )
        return obj
