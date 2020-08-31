from django.db import models
from movie_cat.models import VideoCategory
from django.conf import settings
from django.db import models
from django.contrib.postgres.indexes import BrinIndex
from django.utils import timezone
from pilkit.processors import ResizeToFill, ResizeToFit
from imagekit.models import ProcessedImageField
from django.db.models import Q


class Video(models.Model):
    image = ProcessedImageField(format='JPEG',
                                options={'quality': 90},
                                upload_to="movies/%Y/%m/%d/",
                                processors=[ResizeToFit(width=500, upscale=False)],
                                verbose_name="Обложка")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создан")
    description = models.CharField(max_length=500, blank=True, verbose_name="Описание")
    category = models.ForeignKey(VideoCategory, blank=True, null=True, related_name='video_category', on_delete=models.CASCADE, verbose_name="Плейлист")
    title = models.CharField(max_length=255, verbose_name="Название")
    link = models.CharField(max_length=255, verbose_name="Ссылка на видео")
    comments_enabled = models.BooleanField(default=True, verbose_name="Разрешить комментарии")
    votes_on = models.BooleanField(default=True, verbose_name="Реакции разрешены")
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Создатель")

    class Meta:
        verbose_name = "Видео-ролики"
        verbose_name_plural = "Видео-ролики"
        indexes = (BrinIndex(fields=['created']),)

    def __str__(self):
        return self.title

    def likes(self):
        likes = VideoVotes.objects.filter(parent_id=self.pk, vote__gt=0)
        return likes

    def dislikes(self):
        dislikes = VideoVotes.objects.filter(parent_id=self.pk, vote__lt=0)
        return dislikes

    def likes_count(self):
        likes = VideoVotes.objects.filter(parent=self, vote__gt=0).values("pk")
        return likes.count()

    def dislikes_count(self):
        dislikes = VideoVotes.objects.filter(parent=self, vote__lt=0).values("pk")
        return dislikes.count()

    def count_comments(self):
        parent_comments = VideoComment.objects.filter(video_comment_id=self.pk)
        parents_count = parent_comments.count()
        i = 0
        for comment in parent_comments:
            i = i + comment.count_replies()
        i = i + parents_count
        return i

    def get_comments(self):
        comments_query = Q(video_comment_id=self.pk)
        comments_query.add(Q(parent_comment__isnull=True), Q.AND)
        return VideoComment.objects.filter(comments_query)


class VideoComment(models.Model):
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, related_name='video_comment_replies', null=True, blank=True, verbose_name="Родительский комментарий")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создан")
    modified = models.DateTimeField(auto_now_add=True, auto_now=False, db_index=False)
    commenter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Комментатор")
    text = models.TextField(blank=True)
    is_edited = models.BooleanField(default=False, verbose_name="Изменено")
    is_deleted = models.BooleanField(default=False, verbose_name="Удаено")
    video_comment = models.ForeignKey(Video, on_delete=models.CASCADE, blank=True)

    class Meta:
        indexes = (BrinIndex(fields=['created']), )
        verbose_name = "комментарий к ролику"
        verbose_name_plural = "комментарии к ролику"

    def __str__(self):
        return "{0}/{1}".format(self.commenter.get_full_name(), self.text[:10])

    def get_created(self):
        from django.contrib.humanize.templatetags.humanize import naturaltime
        return naturaltime(self.created)

    def get_replies(self):
        get_comments = VideoComment.objects.filter(parent_comment=self).all()
        return get_comments

    def count_replies(self):
        return self.video_comment_replies.count()

    def likes(self):
        likes = VideoCommentVotes.objects.filter(item=self, vote__gt=0)
        return likes

    def likes_count(self):
        likes = VideoVotes.objects.filter(parent=self, vote__gt=0).values("pk")
        return likes.count()

    def dislikes_count(self):
        dislikes = VideoVotes.objects.filter(parent=self, vote__lt=0).values("pk")
        return dislikes.count()

    def dislikes(self):
        dislikes = VideoCommentVotes.objects.filter(item=self, vote__lt=0)
        return dislikes

    def likes_count(self):
        likes = VideoCommentVotes.objects.filter(item=self, vote__gt=0).values("pk")
        return likes.count()

    def dislikes_count(self):
        dislikes = VideoCommentVotes.objects.filter(item=self, vote__lt=0).values("pk")
        return dislikes.count()

    @classmethod
    def create_comment(cls, commenter, video_comment=None, parent_comment=None, text=None, created=None ):
        comment = VideoComment.objects.create(commenter=commenter, parent_comment=parent_comment, video_comment=video_comment, text=text)
        comment.save()
        return comment

    def count_replies_ru(self):
        count = self.video_comment_replies.count()
        a = count % 10
        b = count % 100
        if (a == 1) and (b != 11):
            return str(count) + " ответ"
        elif (a >= 2) and (a <= 4) and ((b < 10) or (b >= 20)):
            return str(count) + " ответа"
        else:
            return str(count) + " ответов"


class VideoVotes(models.Model):
    LIKE = 1
    DISLIKE = -1
    VOTES = ((DISLIKE, 'Не нравится'),(LIKE, 'Нравится'))

    vote = models.IntegerField(default=0, verbose_name="Голос", choices=VOTES)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
    parent = models.ForeignKey(Video, on_delete=models.CASCADE)

class VideoCommentVotes(models.Model):
    LIKE = 1
    DISLIKE = -1
    VOTES = ((DISLIKE, 'Не нравится'),(LIKE, 'Нравится'))

    vote = models.IntegerField(verbose_name="Голос", choices=VOTES)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
    item = models.ForeignKey(VideoComment, on_delete=models.CASCADE)
