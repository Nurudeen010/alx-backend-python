import django_filters
from .models import Message

class MessageFilter(django_filters.FilterSet):
    # Filter by 'created_at' date range
    created_at__gte = django_filters.DateTimeFilter(field_name='sent_at', lookup_expr='gte')
    created_at__lte = django_filters.DateTimeFilter(field_name='sent_at', lookup_expr='lte')
    
    # Filter by participant
    participant = django_filters.CharFilter(field_name='sender_id__email', lookup_expr='icontains')

    class Meta:
        model = Message
        fields = ['sent_at', 'sender_id']  # Specify which fields to allow filtering by
