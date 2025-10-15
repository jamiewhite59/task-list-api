from fastapi import HTTPException, status

def check_task_exists(db, model, id: str):
	task = db.query(model).filter(model.id == id).first()
	if not task:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task not found with ID: {id}")
	return task
