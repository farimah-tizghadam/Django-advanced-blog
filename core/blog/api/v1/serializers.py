from rest_framework import serializers
from blog.models import Post, Category
from accounts.models import Profile


# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)



class PostSerializer(serializers.ModelSerializer):
    """
    create serializer for post
    """
    snippet = serializers.ReadOnlyField(source='get_snippet')
    relative_url = serializers.URLField(source='get_absolute_api_url', read_only=True)
    absolute_url = serializers.SerializerMethodField(method_name='get_absolute_url')
    # category = serializers.SlugRelatedField(many=False, slug_field='name', queryset=Category.objects.all())
    # category = CategorySerializer()

    class Meta:
        model = Post
        fields = ['id','author', 'title','content','category', 'image', 'status','snippet','relative_url','absolute_url', 'creation_date', 'published_date']
        read_only_fields = ['author']

    def get_absolute_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)
    
    def to_representation(self, instance):
        request = self.context.get('request')
        rep = super().to_representation(instance)
        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('snippet', None)
            rep.pop('relative_url', None)
            rep.pop('absolute_url', None)
        else:
            rep.pop('content', None)
        print(request.__dict__)
        rep['category'] = CategorySerializer(instance.category).data
        return rep
    
    def create(self, validate_data):
        validate_data['author'] = Profile.objects.get(user__id = self.context.get('request').user.id)
        return super().create(validate_data)  

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']