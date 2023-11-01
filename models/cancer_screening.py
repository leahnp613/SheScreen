from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Appointment(BaseModel):
    uuid: str
    datetime: datetime
    provider_questions: Optional[list[str]] = None

class Screening(Appointment):
    id: str

