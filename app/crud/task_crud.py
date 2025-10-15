from sqlalchemy.orm import Session
from app.models.task import Task
from typing import Optional
import uuid

from app.utils.validators import validate_uuid, validate_title
from app.utils.helpers import check_task_exists

def get_tasks(db: Session, title: Optional[str] = None):
	query = db.query(Task)
	if title:
		query = query.filter(Task.title.contains(title))
	return query.all()

def get_task(db: Session, task_id: str):
	task_id = validate_uuid(task_id)

	return check_task_exists(db, Task, task_id)

def create_task(db: Session, title: str):
	title = validate_title(title)

	task = Task(title=title)
	db.add(task)
	db.commit()
	db.refresh(task)
	return task

# def update_task(db: Session, task_id: str, completed: bool):
# 	task = db.query(Task).filter(Task.id == task_id).first()
# 	if task:
# 		task.completed = completed
# 		db.commit()
# 		db.refresh(task)
# 	return task

def update_task_title(db: Session, task_id: str, new_title: str):
	task_id = validate_uuid(task_id)
	task = check_task_exists(db, Task, task_id)
	new_title = validate_title(new_title)

	task.title = new_title
	db.commit()
	db.refresh(task)
	return task

def delete_task(db: Session, task_id: str):
	task_id = validate_uuid(task_id)
	task = check_task_exists(db, Task, task_id)

	db.delete(task)
	db.commit()
	return task

def toggle_task(db: Session, task_id: str):
	task_id = validate_uuid(task_id)
	task = check_task_exists(db, Task, task_id)

	task.completed = not task.completed
	db.commit()
	db.refresh(task)
	return task
