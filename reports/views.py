import pandas as pd

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from complaints.models import Complaint

from django.http import HttpResponse
import csv


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def complaint_report(request):

    complaints = Complaint.objects.all().values()

    df = pd.DataFrame(complaints)

    report_data = df.to_dict(orient='records')

    return Response(report_data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def export_complaints_csv(request):

    response = HttpResponse(content_type='text/csv')

    response['Content-Disposition'] = 'attachment; filename="complaints_report.csv"'

    writer = csv.writer(response)

    writer.writerow(['ID', 'Customer Name', 'Phone Number', 'Complaint', 'Status'])

    complaints = Complaint.objects.all()

    for c in complaints:
        writer.writerow([
            c.id,
            c.customer_name,
            c.phone_number,
            c.complaint_text,
            c.status
        ])

    return response