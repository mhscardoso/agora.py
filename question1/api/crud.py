from sqlalchemy.orm import Session

from . import models, schemas

def get_entities(db: Session):
    return db.query(models.Entity)


def get_entities_nodes(db: Session):
    return db.query(models.Entity).with_entities(models.Entity.id, models.Entity.name).all()


def get_entity_by_id(db: Session, id: int):
    return db.query(models.Entity).filter(models.Entity.id == id).first()


def get_entity_by_name(db: Session, name: str):
    return db.query(models.Entity).filter(models.Entity.name == name).first()


def get_edges(db: Session):
    return db.query(models.Edge)


def create_entity(db: Session, entity: schemas.EntityCreate):
    db_entity = models.Entity(name=entity.name, description=entity.description, image_url=entity.image_url)
    db.add(db_entity)
    db.commit()
    db.refresh(db_entity)
    return db_entity


def create_edge(db: Session, relation: schemas.EdgeSchema):
    db_edge = models.Edge(entity1=relation.entity1, entity2=relation.entity2)
    db.add(db_edge)
    db.commit()
    db.refresh(db_edge)
    return db_edge