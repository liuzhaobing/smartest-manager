from rest_framework.pagination import PageNumberPagination


class PageNumberPaginationManual(PageNumberPagination):  # 重写分页引擎
    page_query_param = 'index'
    page_size_query_param = 'count'
    page_query_description = "页码"
    page_size_query_description = "每页显示条数"
