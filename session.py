from sqlalchemy.orm import Session

session = Session(engine)

class User(Base):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    password = db.Column(db.String)


user = User(
    first_name='Ali',
    last_name='Alavi',
    'password'='$2y$10$xN75dounLcCTW/Tx/u6ta.gTKsLMlrZU9FPgQjYcqPSonexuBrapS'
)

session.add(user)
session.commit()
