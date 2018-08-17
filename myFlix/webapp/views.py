from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.decorators import action

from webapp.utils.utils import get_qs_params
from webapp.models import Movies
from webapp.serializers.serializers import MovieSerializer


DEFAULT_PAGE_NUMBER = 1
DEFAULT_ITEM_PER_PAGE = 20


def index(request):
    return render(request,
                  'webapp/index.html',
                  )


class MovieViewSet(viewsets.ViewSet):
    """
    Movie viewset standard opration with DRF
    """
    #TODO change setting to dev and prod
    renderer_classes = (TemplateHTMLRenderer, JSONRenderer,)
    # renderer_classes = (JSONRenderer,)

    def list(self, request):
        _page_number = int(self.request.GET.get('page', DEFAULT_PAGE_NUMBER))
        _item_per_page = int(self.request.GET.get('items', DEFAULT_ITEM_PER_PAGE))

        query_set = Movies.objects.all()[(_page_number - 1) * _item_per_page : _page_number * _item_per_page]
        serializer = MovieSerializer(query_set, many=True)

        return Response({'context': serializer.data}, template_name='webapp/main.html')

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        query_set = Movies.objects.get(pk=pk)
        serializer = MovieSerializer(query_set)

        return Response({'context': serializer.data})

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
