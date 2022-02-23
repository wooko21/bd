import urllib as url
import click

from flask import Flask, render_template, redirect
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'siema'
bootstrap = Bootstrap(app)

@app.cli.command("show-movies")

def print_movies():
    from database import get_all_movies
    print (get_all_movies())

@app.route('/dummy')
def temp():
    from forms import AddReservationForm
    from forms import AddCityForm
    form = AddCityForm()
    return render_template('reservation_default.html', form=form, edit_type='miasto')

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/get_movies')
def get_movies():
    """
    :return: fun returns a dict of all movies within movies_table
    """
    from database import get_all_movies
    print(get_all_movies())
    return get_all_movies()


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

@app.route('/create_reservation/', methods=['GET', 'POST'])
def choose_movie():
    from forms import SelectMovie
    from database import get_titles

    form = SelectMovie()
    _movies = get_titles()
    print(_movies)
    form.movie_name.choices = _movies
    if form.validate_on_submit():
        return redirect(f'/create_reservation/{form.movie_name.data}')
    return render_template('reservation_default.html', form=form)


@app.route('/create_reservation/<movie_name>', methods=['GET', 'POST'])
def choose_showing(movie_name):
    from forms import SelectShowing
    from database import get_showing_per_movie

    form = SelectShowing()
    _show = get_showing_per_movie(movie_name)
    print(_show)
    form.showing_date_auditorium.choices = list(_show.keys())
    if form.validate_on_submit():
        return redirect(f'/create_reservation/show/{_show[form.showing_date_auditorium.data]}')
    return render_template('reservation_default.html', form=form)


@app.route('/create_reservation/show/<showing>', methods=['GET', 'POST'])
def choose_seating(showing):
    from forms import SelectSeat
    from database import get_free_seats_per_showing, usiadz_na_m

    form = SelectSeat()
    _seat = get_free_seats_per_showing(showing)
    print(_seat)
    form.seat.choices = _seat
    if form.validate_on_submit():
        usiadz_na_m(seat_id=(int(form.seat.data)), showing_id=showing)
        return redirect(f'/create_reservation/success/{_seat[form.seat.data]}')
    return render_template('reservation_default.html', form=form)


@app.route('/create_reservation/success/<seat_id>')
def ticket_booked(show_id: int, seat_id: int):
    return render_template('success.html', seat=seat_id, show=show_id)

@app.route('/get_shows_by_movie/<movie_name>')
def get_shows_by_movie(movie_name: str) -> dict:
    from database import get_shows_by_movie as get_shows
    return get_shows(movie_name)


@app.route('/get_reservations_per_showing/<showing_id>')
def get_reservations_per_showing(showing_id: str):
    from database import get_reservations_per_showing 
    return get_reservations_per_showing(showing_id)

if __name__ == '__main__':
    app.run()
