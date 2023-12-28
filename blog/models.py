from django.db import models
from accounts.models import User


class Item(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)    
    image = models.ImageField(upload_to="image/item/")  # /media/image/
    content = models.TextField()
    price = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]  # 기본 정렬 방식(작성일시 내림차순)

    def __str__(self) -> str:
        return self.title
    


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    item = models.ForeignKey(Item, on_delete = models.CASCADE)
    added = models.BooleanField(default=False) # 장바구니에 추가 여부
    added_at = models.DateTimeField(auto_now_add = True)







# Question 모델
# id, subject(제목), content(내용), created_at(질문 작성일시), modified_at(질문 수정일시-직접입력(값이 없을 수도 있음))
class Question(models.Model):
    subject = models.CharField(max_length=200, verbose_name="제목")
    image = models.ImageField(upload_to="image/question_image", blank=True, verbose_name="이미지")  # /media/image/question_image
    content = models.TextField(verbose_name="내용")
    # 한사람의 user는 여러 질문을 작성할 수 있음(1:N)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="author_question"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일시")
    modified_at = models.DateTimeField(blank=True, null=True, verbose_name="수정일시")
    # 하나의 질문에 여러 사람이 추천을 할 수 있다.
    # 한 사람은 여러 질문을 추천할 수 있다
    # voter = models.ManyToManyField(User, related_name="voter_question")

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.subject
    

# Answer 모델
# id, question(외래 키 설정), content(내용), created_at(질문 작성일시), modified_at(질문 수정일시-직접입력(값이 없을 수도 있음))
# 하나의 질문에는 여러개의 답변을 작성할 수 있다(1:N)
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField(verbose_name="내용")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="author_answer"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일시")
    modified_at = models.DateTimeField(blank=True, null=True, verbose_name="수정일시")

    def __str__(self) -> str:
        return self.content



# Comment (댓글) 모델
# 질문 댓글 Question_Comment - id, question, content, author, created_at, modified_at
# 답변 댓글 Answer_Comment - id, answer, content, author, created_at, modified_at
class Comment(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, blank=True, null=True
    )
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField(verbose_name="내용")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일시")
    modified_at = models.DateTimeField(blank=True, null=True, verbose_name="수정일시")

    def __str__(self) -> str:
        return self.content
