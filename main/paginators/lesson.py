from rest_framework import pagination


class LessonPaginator(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'размер страницы'
    max_page_size = 10
