import strawberry
from typing import List, Optional
from strawberry.types import Info
from app.db import get_db
from app.crud import task_crud
from app.models.task import Task
import uuid

@strawberry.type
class TaskType:
	id: str
	title: str
	completed: bool
	created_at: str
	updated_at: str

@strawberry.type
class Query:
	@strawberry.field
	def tasks(self, info: Info, title: Optional[str] = None) -> List[TaskType]:
		db = next(get_db())
		return task_crud.get_tasks(db, title=title)

	@strawberry.field
	def task(self, info: Info, id: str) -> Optional[TaskType]:
		db = next(get_db())
		return task_crud.get_task(db, id)


@strawberry.type
class Mutation:
	@strawberry.mutation
	def create_task(self, info: Info, title: str) -> TaskType:
		if not title or not title.strip():
			raise ValueError("Title cannot be empty")
		db = next(get_db())
		return task_crud.create_task(db, title)

	@strawberry.mutation
	def update_task(self, info: Info, id: str, completed: bool) -> Optional[TaskType]:
		db = next(get_db())
		return task_crud.update_task(db, id, completed)

	@strawberry.mutation
	def delete_task(self, info: Info, id: str) -> Optional[TaskType]:
		db = next(get_db())
		return task_crud.delete_task(db, id)

	@strawberry.mutation
	def toggle_task(self, info: Info, id: str) -> Optional[TaskType]:
		db = next(get_db())
		return task_crud.toggle_task(db, id)
	@strawberry.mutation
	def update_task_title(self, info: Info, id: str, new_title: str) -> Optional[TaskType]:
		db = next(get_db())
		return task_crud.update_task_title(db, id, new_title)




schema = strawberry.Schema(query=Query, mutation=Mutation)
