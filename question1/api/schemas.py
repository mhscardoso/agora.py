from pydantic import BaseModel, Field, ConfigDict

class EntitySchema(BaseModel):
    id: int
    name: str
    description: str
    image_url: str | None


class EntityNode(BaseModel):
    id: int
    name: str = Field(..., alias='label')

    model_config = ConfigDict(populate_by_name=True)


class EntityCreate(BaseModel):
    name: str
    description: str
    image_url: str | None


class EdgeSchema(BaseModel):
    from_: int = Field(..., alias='from')
    to: int
    description: str

    model_config = ConfigDict(populate_by_name=True)


class EdgeSmart(BaseModel):
    from_: int = Field(..., alias='from')
    to: int

    model_config = ConfigDict(populate_by_name=True)
