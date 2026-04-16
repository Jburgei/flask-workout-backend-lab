from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy import CheckConstraint
db = SQLAlchemy()


class Exercise(db.Model):
    __tablename__ = 'exercises'

    __table_args__ = (
        CheckConstraint("length(name) > 1", name = "check_exercise_name_length"),
    )

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    equipment_needed = db.Column(db.Boolean, nullable=False)

    @validates('name')
    def validate_name(self, key, value): 
        if not value or len(value) < 2:
            raise ValueError("Exercise name must be at lease 2 characterslong.")
            return value.strip()

        
    @validates('category')
    def validate_category(self, key, value):
        allowed_categories = ['strength', 'cardio', 'mobility', 'flexibility', 'core']
        if not value:
            raise ValueError("Category is required.")
        value = value.strip().lower()
        if value not in alowed_categories:
            raise ValueError(f"Category must be one of: {', '.join(allowed_categories)}.")
        return value
        