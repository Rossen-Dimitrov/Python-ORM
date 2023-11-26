import os
import django
from django.db import models
from django.db.models import Q

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()
from main_app.models import Author, Article, Review


def get_authors(search_name=None, search_email=None):
    if search_name is None and search_email is None:
        return ""

    query_name = Q(full_name__icontains=search_name)
    query_email = Q(email__icontains=search_email)

    if search_name and search_email:
        query = query_name & query_email
    elif search_name:
        query = query_name
    else:
        query = query_email

    author = Author.objects.filter(query).order_by('-full_name')

    return '\n'.join([(
        f"Author: {a.full_name},"
        f" email: {a.email},"
        f" status: {'Banned' if a.is_banned else 'Not Banned'}")
        for a in author])


def get_top_publisher():
    top = Author.objects.get_authors_by_article_count().first()
    if not top or top.num_articles == 0:
        return ''

    return f"Top Author: {top.full_name} with {top.num_articles} published articles."


def get_top_reviewer():
    top_author = (Author.objects.prefetch_related().annotate(
        reviews_count=models.Count('reviews')
    ).order_by('-reviews_count', 'email')
                  .first())
    if not top_author or not top_author.reviews_count:
        return ""

    return f"Top Reviewer: {top_author.full_name} with {top_author.reviews_count} published reviews."


def get_latest_article():
    latest = Article.objects.order_by('-published_on').first()

    if not latest:
        return ''

    authors = ', '.join(author.full_name for author in latest.authors.all().order_by('full_name'))
    avg_rating = Review.objects.filter(article=latest).aggregate(models.Avg('rating'))['rating__avg']

    return (
        f"The latest article is: {latest.title}. "
        f"Authors: {authors}. "
        f"Reviewed: {Review.objects.filter(article=latest).count()} times. "
        f"Average Rating: {avg_rating:.2f}."
    )


def get_top_rated_article():
    top = (
        Review.objects
        .values('article')
        .annotate(avg_rating=models.Avg('rating'), num_reviews=models.Count('article__reviews'))
        .order_by('-avg_rating', 'article__title')
        .first()
    )

    if not top:
        return ''

    article = Article.objects.get(pk=top['article'])

    return (
        f"The top-rated article is: {article.title}, "
        f"with an average rating of {top['avg_rating']:.2f}, "
        f"reviewed {top['num_reviews']} times."
    )

def ban_author(email=None):
    author = Author.objects.filter(email=email).first()

    if not author or email is None:
        return "No authors banned."

    author.is_banned = True

    reviews = author.reviews.all()
    reviews_count = len(reviews)
    for r in reviews:
        r.delete()

    reviews.delete()

    return f"Author: {author.full_name} is banned! {reviews_count} reviews deleted."

