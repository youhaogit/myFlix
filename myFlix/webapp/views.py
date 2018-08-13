from django.shortcuts import render
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





class MovieViewSet(viewsets.ModelViewSet):
    """
    Movie page viewset
    """
    serializer_class = MovieInfoSerializer
    renderer_classes = (TemplateHTMLRenderer,)

    def get_queryset(self):
        queryset = Movies.objects.all()
        _page_number = int(self.request.query_params.get('pageNumber', DEFAULT_PAGE_NUMBER))
        _item_per_page = int(self.request.query_params.get('itemPerPage', DEFAULT_ITEM_PER_PAGE))

        if _page_number is not None and _item_per_page is not None:
            return queryset[(_page_number - 1) * _item_per_page : _page_number * _item_per_page]

    @action(detail=False)
    def movies(self, request):
        # _page_number, _item_per_page = get_qs_params(request)
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        print ('here')
        print (serializer.data)
        return Response({'context': serializer.data}, template_name='webapp/index.html')