from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework import viewsets
from profiles.models import Profile, ProfileStatus

from rest_framework import mixins
from profiles.api.permissions import IsOwnProfileOrReadOnly, IsOwnStatusOrReadOnly
from profiles.api.serializers import ProfileSerializer, ProfileStatusSerializer, ProfileAvatarSerializer


class AvatarUpdateView(generics.UpdateAPIView):
    serializer_class = ProfileAvatarSerializer
    permission_classes = (IsAuthenticated, )

    def get_object(self):
        profile_object = Profile.objects.get(user=self.request.user)
        return profile_object


class ProfileViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated, IsOwnProfileOrReadOnly)


class ProfileStatusViewSet(ModelViewSet):
    queryset = ProfileStatus.objects.all()
    serializer_class = ProfileStatusSerializer
    permission_classes = (IsAuthenticated, IsOwnStatusOrReadOnly)

    def perform_create(self, serializer):
        user_profile = Profile.objects.get(user=self.request.user)
        serializer.save(user_profile=user_profile)
