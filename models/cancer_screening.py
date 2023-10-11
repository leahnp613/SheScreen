from pydantic import BaseModel
from datetime import datetime


class cervical_cancer_create(BaseModel):
    date: datetime
    time: datetime
    provider_questions: str


class cervical_cancer_history(BaseModel):
    date: datetime
    time: datetime
    provider_questions: str


class cervical_cancer_update(BaseModel):
    date: datetime
    time: datetime
    provider_questions: str


class cervical_cancer_delete(BaseModel):
    pass


class ovarian_cancer_create(BaseModel):
    date: datetime
    time: datetime
    provider_questions: str


class ovarian_cancer_history(BaseModel):
    date: datetime
    time: datetime
    provider_questions: str


class ovarian_cancer_update(BaseModel):
    date: datetime
    time: datetime
    provider_questions: str


class ovarian_cancer_delete(BaseModel):
    pass


class breast_cancer_create(BaseModel):
    date: datetime
    time: datetime
    provider_questions: str


class breast_cancer_history(BaseModel):
    date: datetime
    time: datetime
    provider_questions: str


class breast_cancer_update(BaseModel):
    date: datetime
    time: datetime
    provider_questions: str


class breast_cancer_delete(BaseModel):
    pass


class uterine_cancer_create(BaseModel):
    date: datetime
    time: datetime
    provider_questions: str


class uterine_cancer_history(BaseModel):
    date: datetime
    time: datetime
    provider_questions: str


class uterine_cancer_update(BaseModel):
    date: datetime
    time: datetime
    provider_questions: str


class uterine_cancer_delete(BaseModel):
    pass
