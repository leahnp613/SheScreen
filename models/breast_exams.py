from datetime import datetime
from pydantic import BaseModel


class BreastExam(BaseModel):
    uuid: str
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


class BreastExamUpdate(BaseModel):
    date: datetime
    time: datetime
