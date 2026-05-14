from django.urls import path
from .views import complaint_report, export_complaints_csv

urlpatterns = [
    path('complaint-report/', complaint_report),
    path('export-csv/', export_complaints_csv),
]