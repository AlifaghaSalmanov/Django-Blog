from django.shortcuts import (
    render,
    HttpResponse,
    redirect,
    get_object_or_404,
    get_list_or_404,
)
from django.urls import reverse
from .forms import ArticleForm
from django.contrib import messages
from .models import Article, Comment
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


@login_required(login_url="user:login")
def addarticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    context = {
        "form": form,
    }
    if form.is_valid():

        article = form.save(commit=False)

        article.author = request.user
        article.save()

        messages.success(request, "Successfully added")
        return redirect("article:dashboard")

    return render(request, "addarticle.html", context)


@login_required(login_url="user:login")
def dashboard(request):
    articles = Article.objects.filter(author=request.user)
    context = {"articles": articles}
    return render(request, "dashboard.html", context)


@login_required(login_url="user:login")
def detail(request, id):
    article = get_object_or_404(Article, id=id)
    comments = article.comments.all()
    context = {"article": article, "comments": comments}
    return render(request, "detail.html", context)


@login_required(login_url="user:login")
def update(request, id):
    article = get_object_or_404(Article, id=id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, "Article updated successfully")
        return redirect("article:dashboard")
    context = {"form": form}
    return render(request, "update.html", context)


@login_required(login_url="user:login")
def delete(request, id):
    article = get_object_or_404(Article, id=id)
    article.delete()
    messages.info(request, "Article successfully deleted")
    return redirect("article:dashboard")


def articles(request):
    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
        context = {"articles": articles}
        return render(request, "articles.html", context)

    articles = Article.objects.all()
    context = {"articles": articles}
    return render(request, "articles.html", context)


def addComment(request, id):
    article = get_object_or_404(Article, id=id)

    if request.POST:
        author = request.POST.get("comment_author")
        content = request.POST.get("comment_content")
        comment = Comment(comment_author=author, comment_content=content)
        comment.article = article
        comment.save()
    messages.success(request, "Successfuly comment added")
    return redirect(reverse("article:detail", kwargs={"id": id}))
