from app.models import Visit
from app import db


def add_visitions() -> None:
    visit = Visit.query.first()
    if visit:
        visit.count += 1  
    else:
        visit = Visit()
        db.session.add(visit)  
    db.session.commit()


def get_visitions() -> int:
    visit = Visit.query.first()
    return visit.count if visit else 0
