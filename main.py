import urllib as url
import click

from flask import Flask, render_template
app = Flask(__name__)

# @app.cli.command("show-movies")
# @click.argument("abc")
# def show_movies(abc):
#     print("hahaha!" + abc)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.cli.command("show-movies")
#@click.argument("abc")
@app.route('/get_movies')
def get_movies():
    """
    :return: fun returns a dict of all movies within movies_table
    """
    from database import get_all_movies
    print (get_all_movies())


@app.route('/genres')
def show_genres():
    """
    :return: fun returns a dict of all distinct genres within movies_table
    """
    from database import get_genres
    return get_genres()


@app.route('/get_movies/<genre>')
def get_movies_by_genre(genre):
    """
    :param genre: a desired genre as a string
    :return: a dict of movies matching the genre
    """
    from database import get_movies_by_genre as mov_per_gen
    return mov_per_gen(genre)


@app.route('/get_movies_by_title/<title>')
def get_movies_by_title(title: str):
    """
    :param title: string of desired title to be searched
            replaces all / with -
    :return:
    """
    from database import get_movies_by_title as mov_per_title
    print(title)
    title = url.parse.quote(title.encode('utf8'), safe='')
    print(title)
    return mov_per_title(title)

@app.route('/add_movie')
def add_movie(movie_name: str, genre: str, length: int):
    """
    :param movie_name: name of film to be added as str
    :param genre: genre of film to be added as str
    :param length: length of film to be added as str
    :return: dict indicating result
    """
    from database import add_movie
    return add_movie()

@app.route('/create_reservation')
# def create_reservation():
#     from forms import AddReservationForm
#     from database import get_all_movies
#
#     form = AddReservationForm()
#     form.movie_name.choices = get_all_movies()
#     form.showings.choices = get
#     if form.validate_on_submit():
#         if add(form.name.data, form.date.data, form.price.data, form.location.data, form.artist.data):
#             flash(f'Poprawnie dodano wydarzenie {form.name.data}')
#         else:
#             flash(f'Nie udało dodać się wydarzenia {form.name.data}')
#     return render_template('add_template.html', form=form)


@app.route('/get_shows_by_movie/<movie_name>')
def get_shows_by_movie(movie_name: str) -> dict:
    from database import get_shows_by_movie as get_shows
    return get_shows(movie_name)


if __name__ == '__main__':
    app.run()
