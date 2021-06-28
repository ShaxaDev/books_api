from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination


class PostPaginationCustom(LimitOffsetPagination):
	max_limit=10
	default_limit=2
	limit_query_param='page'
