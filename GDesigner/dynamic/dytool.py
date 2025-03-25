from typing import Dict, Any
from abc import ABC, abstractmethod

class Dytool(ABC):
    @abstractmethod
    def get_dynamic_info(self) -> str:
        pass