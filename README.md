
# 🧩 FastAPI + Strawberry GraphQL Task Manager





A simple GraphQL API server built with FastAPI, SQLAlchemy, and Strawberry GraphQL to manage a list of tasks.





This project demonstrates basic GraphQL schema design and mutation/query handling.



---



## 🚀 Features





- Create, read, update, and delete (CRUD) tasks via GraphQL



- Uses UUIDs as unique identifiers for tasks



- Automatic timestamping (`created_at`, `updated_at`)



- Input validation for task title and UUID format



- SQLite database





---





## ⚙️ Setup Instructions (Local & MacOS)





### Clone the repository

``git clone https://github.com/yourusername/fastapi-graphql-tasks.git``

``cd fastapi-graphql-tasks``



### Activate the virtual environment

``python3 -m venv venv``

``source venv/bin/activate``



### Install dependencies

``pip install -r requirements.txt``



### Run the server

``uvicorn app.main:app --reload``



- The API will then be available at: http://localhost:8000/graphql

## Next Steps
  - Raw exceptions, currently the API is sending back HTTPResponse errors. A better way to handle errors would be to send back an object in the mutation response.
  - Multiple field updates, currently the toggle mutation and the update title mutation are separate, if the project were to grow there would want to be a way to update multiple fields in a single mutation.
  - Pagination, if the number of tasks is large then it would be wise to group these in the response and only return a certain number at a time to manage performance and load on the database.

## Example Queries



### Create a task
```
mutation {
	createTask(title: "Finish report") {
		id
		title
		completed
		createdAt
		updatedAt
	}
}
```
### List all tasks
```
query {
	tasks {
		id
		title
		completed
		createdAt
		updatedAt
	}
}
```

### Filter tasks by title input
```
query {
	tasks(title: "Title filter") {
		id
		title
		completed
		createdAt
		updatedAt
	}
}
```

### Update a task title
```
mutation {
	updateTaskTitle(id: "UUID", newTitle: "New title!") {
		id
		title
		completed
		createdAt
		updatedAt
	}
}
```

### Toggle a task completed
```
mutation {
	toggleTask(id: "UUID"){
		id
		title
		completed
		createdAt
		updatedAt
	}
}
```

### Delete a task
```
mutation {
	deleteTask(id: "UUID"){
		id
		title
	}
}
```
