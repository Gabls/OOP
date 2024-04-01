# Bibliotecas
from typing import List
from Recipe import Recipe
from Category import Category
from Interfaces import RecipeRepositoryInterface

# Classe - Repositório das Receitas
class RecipeRepository(RecipeRepositoryInterface):
    # Metódo - Criação do objeto
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    # Metódo - Formatação da Receita
    def _format_recipe(self, receita: Recipe) -> str:
        return f'{receita.title}\nCategoria: {receita.category.name}\nDescrição: {receita.description}\nIngredientes: {', '.join(receita.ingredients)}\nInstruções: {receita.instructions}\nTempo de preparo: {receita.preparation_time} minutos\nPorções: {receita.portions}\n'

    # Metódo - Criar a receita
    def save_recipe(self, recipe: Recipe) -> None:
        with open(self.file_path, 'a', encoding='utf-8') as file:
            file.write(self._format_recipe(recipe) + '\n')

    # Metódo - Ler a receita
    def read_recipes(self) -> List[Recipe]:
        # Variáveis
        recipes = []

        # Abrindo o arquivo .txt
        try: 
            with open(self.file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    field = line.split('\n')[0]

                    if field.startswith("Categoria:"):
                        category = field.split(': ')[1]
                    elif field.startswith("Descrição:"):
                        description = field.split(': ')[1]
                    elif field.startswith("Ingredientes:"):
                        ingredients = field.split(': ')[1].split(', ')
                    elif field.startswith("Instruções:"):
                        instructions = field.split(': ')[1]
                    elif field.startswith("Tempo de preparo:"):
                        preparation_time = int(field.split(': ')[1].split(' ')[0])
                    elif field.startswith("Porções:"):
                        portions = int(field.split(': ')[1])
                    elif field != '':
                        title = field
                    else:
                        recipe = Recipe(title, Category(category), description, ingredients, instructions, preparation_time, portions)
                        recipes.append(recipe)
        
        # Erro - Arquivo não encontrado
        except FileNotFoundError:
            print("Arquivo não encontrado!")
        
        # Retornando lista de receitas
        return recipes
