from django.urls import path
from .views import (get_complaints, create_complaint,
 update_complaint, delete_complaint, complaint_dashboard,
 search_complaints, paginated_complaints, sorted_complaints)

urlpatterns = [
    path('all/', get_complaints),
    path('create/', create_complaint),
    path('update/<int:pk>/', update_complaint),
    path('delete/<int:pk>/', delete_complaint),
    path('dashboard/', complaint_dashboard),
    path('search/', search_complaints),
    path('paginated/', paginated_complaints),
    path('sorted/', sorted_complaints),
]

