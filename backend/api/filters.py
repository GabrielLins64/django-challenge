from django.db.models import Q, F
from api.models import Vulnerability


class VulnerabilitySearchFilter:
    """
    Vulnerability List Filter. Allow to query Vulnerability 
    Model by using url query params.
    """
    @classmethod
    def find(cls, query_params):
        """
        Query Vulnerability Model using request's query parameters.
        """
        full_query = None

        if query_params.get('asset_hostname'):
            value = query_params['asset_hostname']
            if full_query:
                full_query = full_query & Q(asset_hostname__icontains=value)
            else:
                full_query = Q(asset_hostname__icontains=value)

        if query_params.get('title'):
            value = query_params['title']
            if full_query:
                full_query = full_query & Q(title__icontains=value)
            else:
                full_query = Q(title__icontains=value)

        if query_params.get('severity'):
            value = query_params['severity']
            if full_query:
                full_query = full_query & Q(severity__icontains=value)
            else:
                full_query = Q(severity__icontains=value)

        if query_params.get('asset_ip_address'):
            value = query_params['asset_ip_address']
            if full_query:
                full_query = full_query & Q(asset_ip_address__icontains=value)
            else:
                full_query = Q(asset_ip_address__icontains=value)

        if query_params.get('publication_date'):
            value = query_params['publication_date']
            if full_query:
                full_query = full_query & Q(publication_date__icontains=value)
            else:
                full_query = Q(publication_date__icontains=value)

        if query_params.get('fixed'):
            value = query_params['fixed'].lower() == 'true'
            if full_query:
                full_query = full_query & Q(fixed=value)
            else:
                full_query = Q(fixed=value)

        if full_query:
            query = Vulnerability.objects.filter(full_query)
        else:
            query = Vulnerability.objects.all()

        if query_params.get('order_by'):
            value = query_params['order_by']
            order_by = value.split(',')
            field = order_by[0]

            if len(order_by) == 2 and order_by[1] == 'desc':
                query = query.order_by(F(field).desc(nulls_last=True))
            else:
                query = query.order_by(F(field).asc(nulls_last=True))

        return query
