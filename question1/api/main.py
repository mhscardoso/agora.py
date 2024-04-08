from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .db import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/entities/", response_model=schemas.EntityCreate)
def create_entity(entity: schemas.EntityCreate, db: Session = Depends(get_db)):
    db_entity = crud.get_entity_by_name(db, entity.name)

    if db_entity:
        raise HTTPException(status_code=400, detail="Pessoa já inserida na Base")

    return crud.create_entity(db=db, entity=entity)


@app.get("/entities/", response_model=list[schemas.EntitySchema])
def get_entities(db: Session = Depends(get_db)):
    entities = crud.get_entities(db)

    return entities


@app.get("/entities_nodes/", response_model=list[schemas.EntityNode])
def get_entities_node(db: Session = Depends(get_db)):
    entities = crud.get_entities_nodes(db)

    return entities


@app.post("/edges/", response_model=schemas.EdgeSchema)
def create_edge(edge: schemas.EdgeSchema, db: Session = Depends(get_db)):

    return crud.create_edge(db=db, relation=edge)


@app.get("/edges/", response_model=list[schemas.EdgeSchema])
def get_edges(db: Session = Depends(get_db)):
    edges = crud.get_edges(db)

    return edges