from pydantic import BaseModel
from typing import List, Optional, Dict, Union

# A single mass definition (Introit, Gloria, etc.)
# Supports both strings and booleans as requested
MassDetails = Dict[str, Union[str, bool]]

# MassData can be a single set of details OR a dictionary of multiple masses
# e.g., {"introit": ".."} OR {"Ad Primam Missam": {"introit": ".."}}
MassData = Union[MassDetails, Dict[str, MassDetails]]

class Feast(BaseModel):
    id: Optional[int] = None
    name_translations: Dict[str, str] = {}
    date: str
    rank_verbose: str
    rank_numeric: int
    color: str
    office_type: Optional[Union[str, bool]] = None
    mass_properties: Optional[MassData] = None
    alt_mass_properties: Optional[MassData] = None # Added for seasonal/alt masses
    commemorations: List[Dict[str, Union[str, MassData]]] = [] # Support mass_props in comms
    nobility: List[int] = [] 

class DioceseOrdo(BaseModel):
    diocese_name: str
    country: str
    feasts: List[Feast]
