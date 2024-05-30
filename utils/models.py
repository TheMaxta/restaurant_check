from pydantic import BaseModel, Field
from typing import List, Optional

class Item(BaseModel):
    name: str
    price: float
    type: Optional[str] = None

class Check(BaseModel):
    items: List[Item] = Field(default_factory=list)
    total: Optional[float] = None
    tip: Optional[float] = None
    split: Optional[int] = None

    def calculate_tip(self, percentage: float):
        self.tip = self.total * (percentage / 100)
    
    def calculate_split(self, num_people: int):
        self.split = (self.total + (self.tip or 0)) / num_people
