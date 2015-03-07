from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from hw.blog import models


class PostResource(ModelResource):
    class Meta:
        queryset = models.Post.objects.all()
        resource_name = 'post'
        authorization = Authorization()


class CommentResource(ModelResource):
    class Meta:
        queryset = models.Comment.objects.all()
        resource_name = 'comment'
        authorization = Authorization()