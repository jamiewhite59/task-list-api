import uuid
from fastapi import HTTPException, status


def validate_uuid(id: str):
	try:
		uuid.UUID(id)
	except ValueError:
		raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ID format")

	return id

def validate_title(title: str):
	if not title or not title.strip():
		raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Title cannot be empty")

	return title.strip()
