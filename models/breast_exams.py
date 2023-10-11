from datetime import datetime
from pydantic import BaseModel


class BreastExam_Create(BaseModel):
    date: datetime
    concerns: str
    lumps: str
    pain: str
    discoloration: str
    discharge: str
    size: str
    shape: str
    lymph_nodes: str
    areola_changes: str
    tissue_consistency: str


class BreastExam_History(BaseModel):
    date: datetime
    concerns: str
    lumps: str
    pain: str
    discoloration: str
    discharge: str
    size: str
    shape: str
    lymph_nodes: str
    areola_changes: str
    tissue_consistency: str
    discussed_with_provider: str


class BreastExam_Update(BaseModel):
    date: datetime
    time: datetime


class BreastExam_Delete():
    pass
