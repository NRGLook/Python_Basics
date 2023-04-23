from JSON import JSONSerializer
from XML import XMLSerializer


class SerializerFactory:
    @staticmethod
    def create_serializer(format_type):
        if format_type == "json":
            return JSONSerializer
        elif format_type == "xml":
            return XMLSerializer
        else:
            raise ValueError(f"Unsupported serializer format '{format_type}'")
