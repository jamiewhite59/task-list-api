import datetime
import uuid
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.db import Base

class Task(Base):
	__tablename__ = "tasks"

	id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
	title = Column(String, nullable=False)
	completed = Column(Boolean, default=False)
	created_at = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))
	updated_at = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc), onupdate=datetime.datetime.now(datetime.timezone.utc))

	def __repr__(self):
		return f"<Task(id={self.id}, title='{self.title}', completed={self.completed})>"
