from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings import settings

engine = create_engine(url=settings.get_db_url)

Session = sessionmaker(engine=engine)


def get_db_session():
    with Session() as session:
        yield session
