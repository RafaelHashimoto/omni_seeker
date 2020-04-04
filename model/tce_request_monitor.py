from sqlalchemy import Column, Integer, String, Boolean
from model.base import Base

class TceRequestMonitor(Base):
	__tablename__ = 'tce_request_monitor'

	id = Column(Integer, primary_key=True)
	method = Column(String)
	year = Column(Integer)
	error = Column(String)
	success = Column(Boolean)

	def __init__(self, method, year, error, success):
		self.method = method
		self.year = year
		self.error = error
		self.success = success

	def save(self):
		self.session.add(self)
		self.session.commit()

	@classmethod
	def save_multiple(cls, array):
		cls.session.add_all(array)
		cls.session.commit()

	@classmethod
	def all(cls):
		ls.session.query(cls).all()