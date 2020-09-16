from django_filters import rest_framework as filters

from mail.models import Mail


COMPARE_FILTERS = ['lte', 'gte', 'lt', 'gt', 'exact']
MATCH_FILTERS = ['exact', 'in']


class MailFilters(filters.FilterSet):
    class Meta:
        model = Mail
        fields = {
            'timestamp': COMPARE_FILTERS,
            'receivers': MATCH_FILTERS,
        }
