from datetime import datetime

from extensions import db

__all__ = ["Todo"]


class Todo(db.Model):
    """data model"""

    __tablename__ = "todo"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    posted_on = db.Column(db.Date, default=datetime.utcnow)
    status = db.Column(db.Boolean(), default=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return "<Todo '%s'>"

    def store_to_db(self):
        """save to database"""

        db.session.add(self)
        db.session.commit()

    def delete_todo(self):
        """delete data"""

        db.session.delete(self)
        db.session.commit()
