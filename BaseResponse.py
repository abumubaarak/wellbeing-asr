from instructor import OpenAISchema
from pydantic import BaseModel
from typing import List, Optional

class Illness(BaseModel):
    name:str
    confidence_rate:int

class Medication(BaseModel):
    drug_name:str
    purpose:str
    dosage_timing:str

class Analysis(BaseModel):
    diagnosis: str
    illness:List[Illness]
    medication: List[Medication]