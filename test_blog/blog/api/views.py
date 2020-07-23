from django_comments_xtd.api import CommentCreate
from rest_framework.response import Response
from django.contrib import messages


class CustomCommentCreate(CommentCreate):
    def post(self, request, *args, **kwargs):
        if request.recaptcha_is_valid:
            return super(CustomCommentCreate, self).post(request, *args, **kwargs)
        storage = messages.get_messages(request)
        errors = []
        for message in storage:
            errors.append(message.message)
            pass
        storage.used = True
        return Response(errors, status=403)
