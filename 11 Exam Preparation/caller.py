import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from django.db.models import Count, Avg, F
from main_app.models import Director, Actor, Movie


def get_directors(search_name=None, search_nationality=None):
    result = []
    if search_name and search_nationality:
        query = (Director.objects.filter(
            full_name__icontains=search_name,
            nationality__icontains=search_nationality)
                 .order_by('full_name')
                 )

    elif search_name:
        query = (Director.objects.filter(
            full_name__icontains=search_name)
                 .order_by('full_name')
                 )

    elif search_nationality:
        query = (Director.objects.filter(
            nationality__icontains=search_nationality)
                 .order_by('full_name')
                 )

    else:
        query = ''

    for director in query:
        result.append(f"Director: {director.full_name}, "
                      f"nationality: {director.nationality}, "
                      f"experience: {director.years_of_experience}")

    return '\n'.join(result)

    # author solution
    # if search_name is None and search_nationality is None:
    #     return ""
    #
    # query = Q()
    # query_name = Q(full_name__icontains=search_name)
    # query_nationality = Q(nationality__icontains=search_nationality)
    #
    # if search_name is not None and search_nationality is not None:
    #     query |= query_name & query_nationality
    # elif search_name is not None:
    #     query |= query_name
    # else:
    #     query |= query_nationality
    #
    # directors = Director.objects.filter(query).order_by('full_name')
    #
    # if not directors:
    #     return ""
    #
    # result = []
    #
    # [result.append(f"Director: {director.full_name}, nationality: {director.nationality}, "
    #                f"experience: {director.years_of_experience}") for director in directors]
    #
    # return '\n'.join(result)


def get_top_director():
    director = Director.objects.get_directors_by_movies_count().first()
    if not director:
        return ''
    return f"Top Director: {director.full_name}, movies: {director.num_movies}."


def get_top_actor():
    actor = (Actor.objects.prefetch_related('starring_movies')
             .annotate(num_of_movies=Count('starring_movies'),
                       movies_avg_rating=Avg('starring_movies__rating'))
             .order_by('-num_of_movies', 'full_name').first())

    if not actor or not actor.num_of_movies:
        return ""

    movies = ", ".join(movie.title for movie in actor.starring_movies.all() if movie)

    return (f"Top Actor: {actor.full_name}, starring in movies: {movies}, "
            f"movies average rating: {actor.movies_avg_rating:.1f}")


def get_actors_by_movies_count():
    top_actors = Actor.objects.annotate(
        num_movies=Count('actor_movies')).order_by('-num_movies', 'full_name')[:3]

    if not top_actors or not top_actors[0].num_movies:
        return ''
    result = []
    for actor in top_actors:
        result.append(f"{actor.full_name}, participated in {actor.num_movies} movies")

    return '\n'.join(result)


def get_top_rated_awarded_movie():
    top_movie = (
        Movie.objects.select_related('starring_actor')
        .prefetch_related('actors')
        .filter(is_awarded=True)
        .order_by('-rating', 'title')
        .first()
    )
    if not top_movie:
        return ''

    starring_actor = top_movie.starring_actor.full_name if top_movie.starring_actor else 'N/A'
    actors = top_movie.actors.order_by('full_name').values_list('full_name', flat=True)
    cast = ', '.join(actors)

    return (f"Top rated awarded movie: {top_movie.title},"
            f" rating: {top_movie.rating:.1f}."
            f" Starring actor: {starring_actor}. Cast: {cast}.")


def increase_rating():
    to_update = Movie.objects.select_related().filter(is_classic=True, rating__lt=10.0)
    if not to_update:
        return f"No ratings increased."

    updated = to_update.update(rating=F('rating') + 0.1)

    return f"Rating increased for {updated} movies."



