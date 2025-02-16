from .core import app, logger
import marvhus.service_users.core as users_core
import marvhus.service_users.models as users_models

from fastapi import HTTPException

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

@app.patch("/users/{id}")
def update_user(user: users_models.User, id: str) -> dict:
    success = users.update_user(id, user)

    if not success:
        raise HTTPException(status_code=404, detail="User not found")

    # NOTE(mvh): Maybe return a 204 No Content instead?
    # This is kinda redundant.
    return {
        "success": true,
    }

@app.delete("/users/{id}")
def remove_user(id: str) -> dict:
    success = users.remove_user(id)

    if not success:
        raise HTTPException(status_code=404, detail="User not found")

    # NOTE(mvh): Maybe return a 204 No Content instead?
    # This is kinda redundant.
    return {
        "success": true,
    }
