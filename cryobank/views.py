from django.shortcuts import render
from rest_framework import generics, mixins, serializers
from .models import Samples
from .serializers import SampleSerializer


class SampleApiView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = Samples.objects.all()
    serializer_class = SampleSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class SampleDetail(generics.GenericAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    queryset = Samples.objects.all()
    serializer_class = SampleSerializer
    lookup_field = 'id'

    def put(self, request, id):
        return self.update(request, id=id)

    def get(self, request, id):
        return self.retrieve(request, id=id)

    def delete(self, request, id):
        return self.destroy(request, id=id)
