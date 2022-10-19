from enum import Enum

INDENTATION = "  "

class DamageType(Enum):
    PYRO = 0
    HYDRO = 1
    DENDRO = 2
    ELECTRO = 3
    CRYO = 4
    ANEMO = 5
    GEO = 6
    PHYSICAL = 7
    
class Element(Enum):
    PYRO = 0
    HYDRO = 1
    DENDRO = 2
    ELECTRO = 3
    CRYO = 4
    ANEMO = 5
    GEO = 6