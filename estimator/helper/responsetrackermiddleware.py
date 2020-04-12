import time
from estimator.helper.file import writeToFile

class StatsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()

        response = self.get_response(request)

        duration = time.time() - start_time
        timeTaken = int(round(duration * 1000))
        timeTaken = "%02d" % (timeTaken,)
        writeToFile(request.method, request.path, response.status_code, timeTaken)
        return response
