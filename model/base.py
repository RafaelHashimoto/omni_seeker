from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:root@db/omni_seeker_db')
Session = sessionmaker(bind=engine)
Base = declarative_base()
Base.session = Session()