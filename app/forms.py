from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired


class TodoForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    completed = SelectField('Completed', choices=[
                            ('True', 'True'), ('False', 'False')])
    validator = [DataRequired()]
    submit = SubmitField('Add Todo')
