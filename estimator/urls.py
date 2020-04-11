from django.urls import path
from estimator.views import Covid19EstimatorJson,Covid19EstimatorXML,Covid19EstimatorLogs

urlpatterns = [
    path('', Covid19EstimatorJson.as_view()),
    path('/json', Covid19EstimatorJson.as_view()),
    path('/xml', Covid19EstimatorXML.as_view()),
    path('/logs', Covid19EstimatorLogs.as_view()),
]