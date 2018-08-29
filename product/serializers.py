from rest_framework import serializers

from product.models import Category


class DynamicCategorySerializer(serializers.ModelSerializer):
    authenticated = serializers.SerializerMethodField()

    def __init__(self, *args, **kwargs):
        super(DynamicCategorySerializer, self).__init__(*args, **kwargs)

        request = self.context['request']
        fields = request.query_params.get('params')
        if fields:
            fields = fields.split('|')
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                if field_name != 'authenticated':
                    self.fields.pop(field_name)
        else:
            self.fields.pop('authenticated')

    def get_authenticated(self, obj):
        return self.context['request']._user.is_authenticated


class CategorySerializer(DynamicCategorySerializer, serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
