from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./tasks.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    user_id = Column(String, nullable=False)
    title = Column(String, nullable=False)


Base.metadata.create_all(bind=engine)

def seed_database():
    db = SessionLocal()

    if db.query(Task).count() == 0:
        db.add_all([
            Task(
                user_id="user_123",
                title="Finish RAG implementation",
            ),
            Task(
                user_id="user_123",
                title="Test the API",
            ),
            Task(
                user_id="user_123",
                title="Update README",
            ),
            Task(
                user_id="user_456",
                title="Private task belonging to another user",
            ),
        ])

        db.commit()

    db.close()


seed_database()