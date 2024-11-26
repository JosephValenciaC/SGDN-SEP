from import_export import resources
from .models import Inmuebles_data

class InmueblesResource(resources.ModelResource):
    class Meta:
        model = Inmuebles_data


