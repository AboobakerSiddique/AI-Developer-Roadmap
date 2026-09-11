from database import SessionLocal, Task


def get_user_tasks(user_id: str) -> list[dict]:
    print(f"🔧 Executing get_user_tasks for user: {user_id}")

    db = SessionLocal()

    try:
        tasks = (
            db.query(Task)
            .filter(Task.user_id == user_id)
            .all()
        )

        result = [
            {
                "id": task.id,
                "title": task.title,
            }
            for task in tasks
        ]

        print(f"🔧 Tool result: {result}")

        return result

    finally:
        db.close()