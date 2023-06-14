import time
from django.db import connection, reset_queries


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        reset_queries()
        start_queries = len(connection.queries)
        start = time.perf_counter()

        response = self.get_response(request)

        end = time.perf_counter()
        end_queries = len(connection.queries)
        print(f"Number of Queries : {end_queries - start_queries}")
        print(f"Finished in : {(end - start):.2f}s")

        return response
