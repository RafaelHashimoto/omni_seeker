from sqlalchemy import Column, Integer, String, Boolean, DateTime
from model.base import Base
import pdb
from datetime import datetime
class TceRequestMonitor(Base):
	__tablename__ = 'tce_request_monitor'

	id = Column(Integer, primary_key=True)
	method = Column(String)
	year = Column(Integer)
	month = Column(Integer)
	error = Column(String)
	success = Column(Boolean)
	municipio_id = Column(Integer)
	tries = Column(Integer, default=0)
	created_at = Column(DateTime, default=datetime.now)
	updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

	def __init__(self, method, year, month, error, success, municipio_id, tries = 0):
		self.method = method
		self.year = year
		self.month = month
		self.error = error
		self.success = success
		self.municipio_id = municipio_id
		self.tries = tries

	@classmethod
	def save_multiple(cls, array):
		cls.session.add_all(array)
		cls.session.commit()

	@classmethod
	def all(cls):
		return  cls.session.query(cls).all()

	@classmethod
	def save_progress(cls, request, method, year, month, error, success, municipio_id):
		if request is not None:
			request.set_attributes(
				year = year, month = month, error = error,
				success = success, municipio_id = municipio_id
			)
		else:
			request = TceRequestMonitor(
				method, year, month, error, success, municipio_id
			)
		request.save()

	@classmethod
	def find_by_method(cls, method):
		return cls.session.query(cls).filter(cls.method == method).first()

	def save(self):
		self.__update_tries()
		self.session.add(self)
		self.session.commit()

	def set_attributes(_self, **kwargs):
		for k,v in kwargs.items():
			setattr(_self, k, v)

	def __update_tries(self):
		self.tries = 0 if self.success else self.tries + 1
