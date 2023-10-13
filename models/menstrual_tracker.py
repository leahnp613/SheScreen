from pydantic import BaseModel


class cycle_create(BaseModel):
    period: str
    spotting: str
    emotions: str
    pain: str
    sex_life: str
    energy: str
    pms: str
    collection_method: str
    discharge: str
    skin: str
    hair: str
    digestion: str
    stool: str
    exercise: str
    birth_control: str


class cycle_history(BaseModel):
    period: str
    spotting: str
    emotions: str
    pain: str
    sex_life: str
    energy: str
    pms: str
    collection_method: str
    discharge: str
    skin: str
    hair: str
    digestion: str
    stool: str
    exercise: str
    birth_control: str


class cycle_update(BaseModel):
    period: str
    spotting: str
    emotions: str
    pain: str
    sex_life: str
    energy: str
    pms: str
    collection_method: str
    discharge: str
    skin: str
    hair: str
    digestion: str
    stool: str
    exercise: str
    birth_control: str


class cycle_delete(BaseModel):
    pass
