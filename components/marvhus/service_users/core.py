from .models import User, Users

# :)
_database: Users = {
    "0": User(id = "0", name = "Foo"),
    "1": User(id = "1", name = "Bar"),
    "2": User(id = "2", name = "Baz"),
}


def get_user(id: str) -> User | None:
    if id in _database:
        return _database[id]

    return None


def get_users() -> Users:
    return _database


def update_user(id: str, user: User) -> bool:
    if not id in _database: return False

    _database[id] = user

    return True


def update_users(users: Users) -> int:
    updated = 0

    for user in users:
        if not user.id in _database:
            continue
        updated += 1

        _database[user.id] = user

    return updated


def remove_user(id: str) -> bool:
    if not id in _database: return False

    del _database[id]

    return True

