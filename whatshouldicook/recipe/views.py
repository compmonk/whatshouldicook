from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .core import listener
from .core.recipe_finder import get_recipe


@api_view(('POST',))
def search(request):
    text = request.data.get("ingredients", "pizza")
    ingredients = text.split(',')
    recipes = get_recipe(ingredients)
    return Response(data={"ingredients": ingredients, "recipes": recipes}, status=status.HTTP_200_OK)
    # return HttpResponse("Hello")


@api_view(('GET',))
def listen(request):
    text = listener.listen()
    ingredients = text
    recipes = get_recipe(ingredients)
    return Response(data={"ingredients": ingredients, "recipes": recipes}, status=status.HTTP_200_OK)
