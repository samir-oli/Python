from fastapi import FastAPI

app = FastAPI()
students = {
      1: {
            "name": "Samir",
            "age": 24,
            "class": "Bachelors"
      }
}


@app.get("/")
def index():
      return {"message": "Hello samir"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int):
      return students[student_id]