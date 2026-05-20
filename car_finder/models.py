from dataclasses import dataclass, field
from typing import Optional, List


@dataclass
class Car:
    id: str
    source: str          # 'olx' | 'webmotors'
    url: str
    title: str
    brand: str
    model: str
    version: str
    year: int
    price: float
    km: Optional[int] = None
    transmission: Optional[str] = None
    has_airbag: Optional[bool] = None
    location: str = ""
    description: str = ""
    images: List[str] = field(default_factory=list)

    # Filled by FipeService
    fipe_price: Optional[float] = None
    fipe_model_name: Optional[str] = None
    discount_vs_fipe: Optional[float] = None   # positive = cheaper than FIPE

    # Filled by OpportunityScorer
    is_opportunity: bool = False
    opportunity_score: float = 0.0
    alerts: List[str] = field(default_factory=list)
