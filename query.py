"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
Brand.query.get('brand_id'=8)
# SELECT * FROM brands WHERE id=8;

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter_by(brand_name='Chevrolet', name='Corvette').all()
# SELECT * FROM models WHERE brand_name = 'Chevrolet' and  name = 'Corvette';

# Get all models that are older than 1960.
Model.query.filter(Model.year < 1960).all()
#Model.query.filter_by(year=1960).all() YES
#SELECT * FROM models WHERE year < 1960

# Get all brands that were founded after 1920.
# SELECT * FROM brands WHERE founded > 1920 
Brand.query.filter(Brand.founded > 1920).all() 

# Get all models with names that begin with "Cor".
#SELECT * FROM models WHERE name LIKE 'Cor%'
Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
# SELECT * FROM brands WHERE discontinued IS NULL and founded > 1903;
Brand.query.filter(Brand.founded > 1903, Brand.discontinued.is_(None)).all() 

# Get all brands that are either 1) discontinued (at any time) or 2) founded 
# before 1950.
Brand.query.filter( db.or_(Brand.discontinued.isnot(None), Brand.founded<1950) ).all() 

# Get any model whose brand_name is not Chevrolet.
Model.query.filter(Model.brand_name != 'Chevrolet').all() 
# SELECT * FROM models WHERE brand_name != 'Chevrolet';

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''
# Query here
#SELECT model, brand_name, headquarters
	years = Model.query.get(year)

	by_year = db.session.query(Model.name, Model.brand_name, Brand.headquarters).all()

	for year in year:
		print out each model (Model) 
				brand_name (foreign key from Brand to Model)
				headquarters (Brand)
				.all()

    movie = Movie.query.get(movie_id)

    rating_counts = db.session.query(Rating.score, func.count(Rating.score)).\
                               group_by(Rating.score).\
                               filter(Rating.movie_id==movie_id).\
                               order_by(Rating.score).\
                               all()
    avg_rating = db.session.query(func.avg(Rating.score)).\
                            filter(Rating.movie_id==movie_id).\
                            first()
    

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    pass

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

# This query from the brands table return the location of the object 
# with the attribute name "Ford" in memory. This is just a question because nothing 
#runs until you use dotsomething() to get results.
#<flask_sqlalchemy.BaseQuery object at 0x109a0c4d0>

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
#An association table is a table you use in a many to many situation
#between tables with the use of foreign keys. 
# 

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    pass


def get_models_between(start_year, end_year):
    pass
