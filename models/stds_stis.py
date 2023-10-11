from pydantic import BaseModel


class std_sti_create(BaseModel):
    number_of_partners_in_last_six_months: int
    discharge: str
    pain: str
    other_symptoms: str
    previous_infection: str


class std_sti_history(BaseModel):
    number_of_partners_in_last_six_months: int
    discharge: str
    pain: str
    other_symptoms: str
    previous_infection: str


class std_sti_update(BaseModel):
    number_of_partners_in_last_six_months: int
    discharge: str
    pain: str
    other_symptoms: str
    previous_infection: str


class std_sti_delete(BaseModel):
    pass
