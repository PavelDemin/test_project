import sqlalchemy

metadata = sqlalchemy.MetaData()

images = sqlalchemy.Table(
    "images",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("image_url", sqlalchemy.String),
    sqlalchemy.Column("needed_amount_of_shows", sqlalchemy.Integer),
    sqlalchemy.Column("category1", sqlalchemy.String),
    sqlalchemy.Column("category2", sqlalchemy.String),
    sqlalchemy.Column("category3", sqlalchemy.String),
    sqlalchemy.Column("category4", sqlalchemy.String),
    sqlalchemy.Column("category5", sqlalchemy.String),
    sqlalchemy.Column("category6", sqlalchemy.String),
    sqlalchemy.Column("category7", sqlalchemy.String),
    sqlalchemy.Column("category8", sqlalchemy.String),
    sqlalchemy.Column("category9", sqlalchemy.String),
    sqlalchemy.Column("category10", sqlalchemy.String),
)
