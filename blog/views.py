from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from .models import Item, Question, Answer, Comment, Cart
from .forms import ItemForm, QuestionForm, AnswerForm, CommentForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.core.paginator import Paginator
from accounts.models import User
from blog.models import Item, Cart, CartItem

from django.http import JsonResponse
from django.views.decorators.http import require_POST


# Cart 추가한 것만 보여주기
def cart(request, nickname):
    user = get_object_or_404(User, nickname=nickname ) # cart의 소유주 = user
    # item = get_object_or_404(Item, id=user.) # ??????
    

    context = {"user": user}
    return render(request, "blog/cart_page.html", context)




def add_to_cart(request, item_id): # item id가 다르게 들어와야 함
    item = get_object_or_404(Item, id=item_id)
    user = request.user

    # 수량 가져오기
    quantity = int(request.POST.get("quantity"))
    # 사용자의 cart 가져오기
    cart = get_object_or_404(Cart,user=user)

    # 사용자의 장바구니에 해당 아이템이 이미 있는지 확인
    # 만약 이미 장바구니에 있는 아이템이면 수량을 증가시킴


    try:
        cart_item = CartItem.objects.get(cart=cart, item=item)
        cart_item.quantity += quantity
        cart_item.save()

    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            item = item,
            quantity = quantity,
            cart = cart
        )
        cart_item.save()

    messages.success(request, f"{item.title}이(가) 장바구니에 추가되었습니다.")

    # cart_item, created = CartItem.objects.get_or_create(cart=cart,item=item,quantity=quantity)
    
    # if not created:
    #     cart_item.quantity += quantity
    #     cart_item.save()

    # # 여기에서는 간단하게 메시지를 추가하여 장바구니에 성공적으로 추가되었음을 알려줄 수 있습니다.
    # messages.success(request, f"{item.title}이(가) 장바구니에 추가되었습니다.")

    return redirect('blog:cart', user.nickname)  # 장바구니 페이지로 리다이렉트

































def index(request):
    items= Item.objects.all()
    page = request.GET.get("page",1)
    paginator = Paginator(items, 3)
    page_obj = paginator.get_page(page)
    context = {
        "items" : page_obj
    }

    return render(request, 'blog/index.html', context)

# item
@login_required
def item_register(request):
    """
    item 추가
    """
    if request.method == "POST":
        # request.FILES : type=file 에 들어있는 값 가져오기
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            # form 에 author 가 없기 때문에
            item = form.save(commit=False)
            # request.user : 현재 로그인 사용자
            item.author = request.user
            item.save()
            # # 태그 저장
            # form.save_m2m()

            return redirect("blog:index")
    else:
        form = ItemForm()

    return render(request, "blog/item_register.html", {"form": form})


def item_detail(request, id):
    item = get_object_or_404(Item, id=id)
    context={
        "item":item
    }
    return render(
        request, "blog/item_detail.html", context
    )


@login_required
def item_modify(request,pk):
    """
    질문 수정 - form 사용
    """
    item = get_object_or_404(Item, id=pk ) # 수정할 대상 찾기
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES, instance=item) # instance= 찾은 대상 적어주기. 안쓰면 create 되어버림
        if form.is_valid():
            item = form.save(commit=False)
            item.modified_at = timezone.now()
            item.save()
            return redirect("blog:item_detail", item.id)
    else:
        form = ItemForm(instance=item)
    return render(request, "blog/item_modify.html", {"form":form})


@login_required
def item_delete(request, pk):
    item = get_object_or_404(Item, id=pk)
    item.delete()
    return redirect("blog:index")


def faq(request):
    return render(request, "blog/faq.html")

def qna(request):
    """
    question 전체 목록 추출
    """
    # http://127.0.0.1:8000/board/?page=3
    # page = request.GET.get("page", 1)

    # 기본 정렬을 이용해서 목록 추출
    question_list = Question.objects.all()
    # paginator = Paginator(question_list, 10)
    # page_obj = paginator.get_page(page)

    context = {"question_list": question_list}
    
    return render(request, "blog/question_list.html", context)




# Question
@login_required
def question_register(request):
    """
    질문등록 - form 사용
    """
    if request.method == "POST":
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect("blog:question_detail", question.id)
    else:
        form = QuestionForm()
    return render(request, "blog/question_register.html", {"form": form})


def question_detail(request, qid):
    """
    Question 상세 조회
    """
    question = get_object_or_404(Question, id=qid)
    return render(request, "blog/question_detail.html", {"question": question})

@login_required
def question_modify(request,qid):
    """
    질문 수정 - form 사용
    """
    question = get_object_or_404(Question, id=qid ) # 수정할 대상 찾기
    if request.method == "POST":
        form = QuestionForm(request.POST, request.FILES, instance=question) # instance= 찾은 대상 적어주기. 안쓰면 create 되어버림
        if form.is_valid():
            question = form.save(commit=False)
            question.modified_at = timezone.now()
            question.save()
            return redirect("blog:question_detail", question.id)
    else:
        form = QuestionForm(instance=question)
    return render(request, "blog/question_modify.html", {"form":form})


@login_required
def question_delete(request, qid):
    question = get_object_or_404(Question, id=qid)
    question.delete()
    return redirect("blog:qna")





# Answer
@login_required
def answer_create(request, qid):
    '''
    답변등록
    1) question.answer_set.create()
    2) answer = Answer()
       answer.save()
    '''
    # 3번 방식 - form 이용
    question = get_object_or_404(Question,id=qid)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.save()
            return redirect("blog:question_detail", qid)
    else:
        form = AnswerForm()
    
    context = {"form":form, "question":question}

    return render(request, "blog/question_detail.html", context)

@login_required
def answer_modify(request,aid):
    """
    질문 수정 - form 사용
    """
    answer = get_object_or_404(Answer, id=aid ) # 수정할 대상 찾기
    if request.method == "POST":
        form = AnswerForm(request.POST, request.FILES, instance=answer) # instance= 찾은 대상 적어주기. 안쓰면 create 되어버림
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modified_at = timezone.now()
            answer.save()
            return redirect("blog:question_detail", answer.question.id)
    else:
        form = AnswerForm(instance=answer)
    return render(request, "blog/answer_modify.html", {"form":form})

@login_required
def answer_delete(request, aid):
    answer = get_object_or_404(Answer, id=aid)
    answer.delete()
    return redirect("blog:question_detail" ,answer.question.id)







# Comment
@login_required
def comment_create_answer(request, aid):
    '''
    답변등록
    1) question.answer_set.create()
    2) answer = Answer()
       answer.save()
    '''
    # 3번 방식 - form 이용
    answer = get_object_or_404(Answer, id=aid)
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.answer = answer
            comment.save()
            return redirect("blog:question_detail", answer.question.id)
            # return redirect( "{}#comment_{}".format(
            #         resolve_url("blog:question_detail", answer.id),
            #         comment.id,
            #     ))
    else:
        form = CommentForm()
    
    context = {"form":form, "answer":answer}

    return render(request, "blog/question_detail.html", context)

@login_required
def comment_modify_answer(request, cid):
    comment = get_object_or_404(Comment, id=cid)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.modified_at = timezone.now()
            comment.save()
            return redirect("blog:question_detail", comment.answer.question.id)
            # return redirect(
            #     "{}#comment_{}".format(
            #         resolve_url("board:question_detail", comment.answer.question.id),
            #         comment.id,
            #     )
            # )
    else:
        form = CommentForm(instance=comment)
    return render(request, "blog/comment_form.html", {"form": form})

@login_required
def comment_delete_answer(request, cid):
    comment = get_object_or_404(Comment, id=cid)
    comment.delete()
    return redirect("blog:question_detail" ,comment.answer.question.id)






