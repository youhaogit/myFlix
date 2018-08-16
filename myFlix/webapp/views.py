from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.decorators import action

from webapp.utils.utils import get_qs_params
from webapp.models import Movies
from webapp.serializers.serializers import MovieInfoSerializer


DEFAULT_PAGE_NUMBER = 1
DEFAULT_ITEM_PER_PAGE = 20


def index(request):
    return render(request,
                  'webapp/index.html',
                  )


class MoviesViewSet(viewsets.ModelViewSet):
    """
    Movies viewset in one page
    """
    serializer_class = MovieInfoSerializer
    renderer_classes = (TemplateHTMLRenderer,)

    def get_queryset(self):
        queryset = Movies.objects.all()
        _page_number = int(self.request.GET.get('page', DEFAULT_PAGE_NUMBER))
        _item_per_page = int(self.request.GET.get('items', DEFAULT_ITEM_PER_PAGE))

        return queryset[(_page_number - 1) * _item_per_page : _page_number * _item_per_page]

    @action(detail=False)
    def movies(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response({'context': serializer.data}, template_name='webapp/main.html')


class MovieViewSet(viewsets.ModelViewSet):
    """
    Single movie view page
    """
    serializer_class = MovieInfoSerializer
    renderer_classes = (TemplateHTMLRenderer,)

    def get_queryset(self):
        queryset = Movies.objects.all()
        _page_number = int(self.request.GET.get('page', DEFAULT_PAGE_NUMBER))
        _item_per_page = int(self.request.GET.get('items', DEFAULT_ITEM_PER_PAGE))

        return queryset[(_page_number - 1) * _item_per_page : _page_number * _item_per_page]

    @action(detail=False)
    def movies(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response({'context': serializer.data}, template_name='webapp/main.html')