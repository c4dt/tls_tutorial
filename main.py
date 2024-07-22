from fastapi import FastAPI

app = FastAPI()


# Basic storage for demonstration purposes
db = [{"hello": "world"}]


@app.get("/")
def shopping_cart() -> list[dict[str, str]]:
    return db


@app.post("/")
def register_new_information(data: dict) -> list[dict[str, str]]:
    db.append(data)
    return db
