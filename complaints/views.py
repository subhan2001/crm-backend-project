from rest_framework.pagination import PageNumberPagination
from django.core.mail import send_mail
from accounts.models import UserProfile
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Complaint
from .serializers import ComplaintSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_complaints(request):

    complaints = Complaint.objects.all()

    serializer = ComplaintSerializer(complaints, many=True)

    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_complaint(request):

    serializer = ComplaintSerializer(data=request.data)

    if serializer.is_valid():

        serializer.save()

        send_mail(
            subject='Complaint Registered',
            message='Your complaint has been registered successfully.',
            from_email='admin@crm.com',
            recipient_list=['customer@gmail.com'],
            fail_silently=False,
        )
        

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_complaint(request, pk):

    try:
        complaint = Complaint.objects.get(id=pk)

    except Complaint.DoesNotExist:
        return Response(
            {"error": "Complaint not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = ComplaintSerializer(
        complaint,
        data=request.data,
        partial=True
    )

    if serializer.is_valid():

        serializer.save()

        return Response(serializer.data)

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_complaint(request, pk):

    try:
        complaint = Complaint.objects.get(id=pk)

    except Complaint.DoesNotExist:
        return Response(
            {"error": "Complaint not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    
        try:
            profile = UserProfile.objects.get(user=request.user)

            if profile.role != 'Admin':

                return Response(
                    {"error": "Only Admin can delete complaints"},
                    status=status.HTTP_403_FORBIDDEN
                )

        except UserProfile.DoesNotExist:

            return Response(
                {"error": "User profile not found"},
                status=status.HTTP_404_NOT_FOUND
            )

    complaint.delete()

    return Response(
        {"message": "Complaint deleted successfully"},
        status=status.HTTP_204_NO_CONTENT
    )

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def complaint_dashboard(request):

    total_complaints = Complaint.objects.count()

    pending_complaints = Complaint.objects.filter(
        status='Pending'
    ).count()

    resolved_complaints = Complaint.objects.filter(
        status='Resolved'
    ).count()

    inprogress_complaints = Complaint.objects.filter(
        status='In Progress'
    ).count()

    data = {
        "total_complaints": total_complaints,
        "pending_complaints": pending_complaints,
        "resolved_complaints": resolved_complaints,
        "inprogress_complaints": inprogress_complaints
    }

    return Response(data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_complaints(request):

    customer_name = request.GET.get('customer_name')

    status_value = request.GET.get('status')

    complaints = Complaint.objects.all()

    if customer_name:

        complaints = complaints.filter(
            customer_name__icontains=customer_name
        )

    if status_value:

        complaints = complaints.filter(
            status=status_value
        )

    serializer = ComplaintSerializer(
        complaints,
        many=True
    )

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def paginated_complaints(request):

    complaints = Complaint.objects.all().order_by('-id')

    paginator = PageNumberPagination()

    paginator.page_size = 2

    result_page = paginator.paginate_queryset(
        complaints,
        request
    )

    serializer = ComplaintSerializer(
        result_page,
        many=True
    )

    return paginator.get_paginated_response(
        serializer.data
    )

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def sorted_complaints(request):

    sort_by = request.GET.get('sort_by', '-created_at')

    complaints = Complaint.objects.all().order_by(sort_by)

    serializer = ComplaintSerializer(
        complaints,
        many=True
    )

    return Response(serializer.data)