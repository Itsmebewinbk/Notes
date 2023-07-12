def note(data) -> dict:
    return {
        "id": str(data["_id"]),
        "title": data["title"],
        "description": data["description"],
        "important": data["important"],
    }


def notes(datas) -> list:
    return [note(data) for data in datas]
