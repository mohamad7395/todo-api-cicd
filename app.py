from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, CI/CD!"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/todos")
def get_todos():
    todos = [
        {"id": 1, "task": "Learn CI/CD", "done": False},
        {"id": 2, "task": "Build a pipeline", "done": True}
    ]
    return {"todos": todos}

