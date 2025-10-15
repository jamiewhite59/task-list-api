from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from app.schemas.task_schema import schema
from app.db import Base, engine
from app.models import task

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task GraphQL API")

graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

@app.get("/")
def root():
	return {"message": "Welcome to the Task GraphQL API"}
