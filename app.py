from flask import Flask, render_template, url_for, redirect
from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm

app = Flask(__name__,
            instance_relative_config=False,
            template_folder="templates",
            static_folder="static")
app.config['SECRET_KEY'] = 'any secret string'

# @app.route('/')
# def done():
#     return render_template("index.html",
#                            title="Jinja Demo Site",
#                            description="Smarter page template with flask & Jinja")


class GetPlayerNames(FlaskForm):
    player1 = StringField("Player 1")
    player2 = StringField('Player 2')
    player3 = StringField('Player 3')
    submit = SubmitField('Submit')


@app.route('/', methods=('GET', 'POST'))
def contact():
    form=GetPlayerNames()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('get-player-names.html', form=form)


if __name__ == '__main__':
    app.run()
