# Bibliotecas
from typing import List
from Recipe import Recipe
from abc import ABC, abstractmethod

# Interface - Repositório das Receitas
class RecipeRepositoryInterface(ABC):
    @abstractmethod
    def save_recipe(self, recipe: Recipe) -> None:
        pass

    @abstractmethod
    def read_recipes(self) -> List[Recipe]:
        pass
