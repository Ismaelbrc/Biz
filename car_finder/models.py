"""Domain model for a car listing."""
from dataclasses import dataclass, field, asdict
from typing import Optional


@dataclass
class Car:
    id:           str
    source:       str
    url:          str
    title:        str
    brand:        str
    model:        str
    version:      str
    year:         int
    price:        float
    km:           Optional[int]  = None
    transmission: Optional[str]  = None
    has_airbag:   Optional[bool] = None
    location:     str            = ""
    description:  str            = ""
    images:       list           = field(default_factory=list)
    fipe_price:      Optional[float] = None
    fipe_model_name: Optional[str]   = None
    discount_pct:    Optional[float] = None
    is_opportunity:    bool  = False
    opportunity_score: float = 0.0
    alerts:            list  = field(default_factory=list)

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict) -> "Car":
        known = {f.name for f in cls.__dataclass_fields__.values()}
        return cls(**{k: v for k, v in d.items() if k in known})
