# Biblioteca
from Category import Category

# Classe - Receita
class Recipe:
    # Metódo - Criação do objeto
    def __init__(self, title: str, category: Category, description: str, ingredients: str, instructions: str, preparation_time: int, portions: int) -> None:
        self.title = title
        self.category = category
        self.description = description
        self.ingredients = ingredients
        self.instructions = instructions
        self.preparation_time = preparation_time
        self.portions = portions
