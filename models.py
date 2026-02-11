from dataclasses import dataclass
from typing import List, Tuple, Set, Dict, Optional

@dataclass
class Production:
    left: str
    right: str
    
    def __str__(self) -> str:
        return f"{self.left} → {self.right}"
    
    def __repr__(self) -> str:
        return self.__str__()