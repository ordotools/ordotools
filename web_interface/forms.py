from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Optional, NumberRange

class TemporalFeastForm(FlaskForm):
    id = StringField('ID', validators=[DataRequired()])
    rank_numeric = IntegerField('Rank (Numeric)', validators=[DataRequired(), NumberRange(min=1, max=4)])
    rank_verbose = StringField('Rank (Verbose)', validators=[DataRequired()])
    color = SelectField('Color', choices=[
        ('white', 'White'),
        ('red', 'Red'),
        ('green', 'Green'),
        ('violet', 'Violet'),
        ('black', 'Black')
    ], validators=[DataRequired()])
    office_type = BooleanField('Office Type (Has specific office?)')
    
    # Nobility
    nobility_1 = IntegerField('Nobility 1', validators=[Optional()])
    nobility_2 = IntegerField('Nobility 2', validators=[Optional()])
    nobility_3 = IntegerField('Nobility 3', validators=[Optional()])
    nobility_4 = IntegerField('Nobility 4', validators=[Optional()])
    nobility_5 = IntegerField('Nobility 5', validators=[Optional()])
    nobility_6 = IntegerField('Nobility 6', validators=[Optional()])
    
    # Properties (JSON fields as text for now, could be improved)
    mass_properties = TextAreaField('Mass Properties (JSON)', validators=[Optional()])
    vespers_properties = TextAreaField('Vespers Properties (JSON)', validators=[Optional()])
    matins_properties = TextAreaField('Matins Properties (JSON)', validators=[Optional()])
    lauds_properties = TextAreaField('Lauds Properties (JSON)', validators=[Optional()])
    prime_properties = TextAreaField('Prime Properties (JSON)', validators=[Optional()])
    little_hours_properties = TextAreaField('Little Hours Properties (JSON)', validators=[Optional()])
    compline_properties = TextAreaField('Compline Properties (JSON)', validators=[Optional()])
    com_1_properties = TextAreaField('Com 1 Properties (JSON)', validators=[Optional()])
    com_2_properties = TextAreaField('Com 2 Properties (JSON)', validators=[Optional()])
    com_3_properties = TextAreaField('Com 3 Properties (JSON)', validators=[Optional()])
    
    submit = SubmitField('Save Feast')

class SanctoralFeastForm(FlaskForm):
    id = IntegerField('ID', validators=[Optional()]) # Optional for new feasts
    month = IntegerField('Month', validators=[DataRequired(), NumberRange(min=1, max=12)])
    day = IntegerField('Day', validators=[DataRequired(), NumberRange(min=1, max=31)])
    diocese_source = StringField('Diocese Code (e.g., roman, usa)', validators=[Optional()])
    
    rank_numeric = IntegerField('Rank (Numeric)', validators=[DataRequired(), NumberRange(min=1, max=4)])
    rank_verbose = StringField('Rank (Verbose)', validators=[DataRequired()])
    color = SelectField('Color', choices=[
        ('white', 'White'),
        ('red', 'Red'),
        ('green', 'Green'),
        ('violet', 'Violet'),
        ('black', 'Black')
    ], validators=[DataRequired()])
    office_type = BooleanField('Office Type (Has specific office?)')
    
    # Nobility
    nobility_1 = IntegerField('Nobility 1', validators=[Optional()])
    nobility_2 = IntegerField('Nobility 2', validators=[Optional()])
    nobility_3 = IntegerField('Nobility 3', validators=[Optional()])
    nobility_4 = IntegerField('Nobility 4', validators=[Optional()])
    nobility_5 = IntegerField('Nobility 5', validators=[Optional()])
    nobility_6 = IntegerField('Nobility 6', validators=[Optional()])
    
    # Properties
    mass_properties = TextAreaField('Mass Properties (JSON)', validators=[Optional()])
    vespers_properties = TextAreaField('Vespers Properties (JSON)', validators=[Optional()])
    matins_properties = TextAreaField('Matins Properties (JSON)', validators=[Optional()])
    lauds_properties = TextAreaField('Lauds Properties (JSON)', validators=[Optional()])
    prime_properties = TextAreaField('Prime Properties (JSON)', validators=[Optional()])
    little_hours_properties = TextAreaField('Little Hours Properties (JSON)', validators=[Optional()])
    compline_properties = TextAreaField('Compline Properties (JSON)', validators=[Optional()])
    com_1_properties = TextAreaField('Com 1 Properties (JSON)', validators=[Optional()])
    com_2_properties = TextAreaField('Com 2 Properties (JSON)', validators=[Optional()])
    com_3_properties = TextAreaField('Com 3 Properties (JSON)', validators=[Optional()])
    
    submit = SubmitField('Save Feast')
