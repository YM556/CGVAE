from typing import Dict, Any
from abc import ABC, abstractmethod


class Dytool(ABC):
    """
    Abstract base class for a set of prompts.
    """
    @staticmethod
    @abstractmethod
    def get_role() -> str:
        """ TODO """
