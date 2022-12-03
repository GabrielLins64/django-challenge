from drf_yasg.generators import OpenAPISchemaGenerator


class CustomOpenAPISchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        """Generate a :class:`.Swagger` object with custom tags"""

        swagger = super().get_schema(request, public)
        swagger.tags = [
            {
                "name": "api",
                "description": "Main API endpoints"
            },
            {
                "name": "auth",
                "description": "Authentication endpoints"
            },
        ]

        return swagger
