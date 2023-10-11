

from datetime import datetime
from xmlrpc.client import Boolean


class BreastExam_Create(BaseModel):
    date: datetime
    concerns: str
    lumps: str
    pain: Boolean
    discoloration: str
    discharge: str
    size: str
    shape: str
    lymph_nodes: str
    areola_changes: str
    tissue_consistency: str


class BreastExam_History(BaseModel):
    

class BreastExam_Update(BaseModel):
    date: datetime
    time: datetime


class BreastExam_Delete():