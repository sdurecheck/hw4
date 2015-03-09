from tastypie.resources import ModelResource, ALL_WITH_RELATIONS, ALL
from tastypie.authorization import Authorization
from hw.blog import models
from tastypie import fields

class CommentResource(ModelResource):
    author = fields.CharField(attribute="author")
    text = fields.CharField(attribute="text")
    post = fields.ToOneField('hw.blog.api.PostResource', 'post')    
    class Meta:
        queryset = models.Comment.objects.all()
        resource_name = 'comment'
        authorization = Authorization()
        always_return_data = True

class PostResource(ModelResource):
    text = fields.CharField(attribute="text")
    author = fields.CharField(attribute="author")
    title = fields.CharField(attribute="title")
    is_public = fields.BooleanField(attribute="is_public")    
    comment = fields.ToManyField('hw.blog.api.CommentResource','comment_set', null=True,use_in="detail")
    class Meta:
        queryset = models.Post.objects.all()
        resource_name = 'post'
        authorization = Authorization()
        always_return_data = True

