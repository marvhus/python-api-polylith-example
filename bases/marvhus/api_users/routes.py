from .core import app, logger
import marvhus.service_users.core as users_core
import marvhus.service_users.models as users_models

from fastapi import HTTPException, status

@app.get("/assert")
def get_assert() -> None:
    assert false

    return

@app.get("/users")
def get_users() -> users_models.Users:
    retrieved = users_core.get_users()

    if retrieved is None:
        raise HTTPException(status_code=404, detail="Users not found")

    return retrieved

@app.get("/users/{id}")
def get_user(id: str) -> users_models.User:
    retrieved = users_core.get_user(id)

    if retrieved is None:
        raise HTTPException(status_code=404, detail="User not found")

    return retrieved

@app.patch("/users")
def update_users(users: users_models.Users) -> dict:
    count = users_core.update_users(users)

    return {
        "updated": count,
    }

@app.patch("/users/{id}", status_code = status.HTTP_204_NO_CONTENT)
def update_user(user: users_models.User, id: str) -> None:
    success = users_core.update_user(id, user)

    if not success:
        raise HTTPException(status_code=404, detail="User not found")


@app.delete("/users/{id}", status_code = status.HTTP_204_NO_CONTENT)
def remove_user(id: str) -> None:
    success = users_core.remove_user(id)

    if not success:
        raise HTTPException(status_code=404, detail="User not found")
