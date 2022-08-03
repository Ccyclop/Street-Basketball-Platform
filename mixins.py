from rest_framework import serializers

class RequestMethodSerializerClassMixin:
    method_serializer_classes:dict[list[str], serializers.Serializer] = {}

    def get_serializer_class(self) -> serializers.Serializer: 
        for methods, serializer_class in self.method_serializer_classes.items():
            if self.request.method in methods:
                return serializer_class
        return self.method_serializer_classes['DEFAULT']