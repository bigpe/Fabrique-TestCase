from drf_yasg.generators import OpenAPISchemaGenerator


class BothHttpAndHttpsSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        if 'heroku' in schema.host:
            schema.schemes = ["https"]
        else:
            schema.schemes = ["http", "https"]
        return schema
    