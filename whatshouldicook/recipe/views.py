import json

from django.core.files.base import ContentFile
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .core.import_service import upload_file
from .core.vision import recognize

from .core.image_util import recognize_image
from .core.recipe_finder import get_recipe


@api_view(('POST',))
def search(request):
    ingredients = request.data.get("ingredients", ["chicken"])
    recipes = get_recipe(ingredients)
    return Response(data={"ingredients": ingredients, "recipes": recipes}, status=status.HTTP_200_OK)


@api_view(('POST',))
def upload(request):
    image_path = upload_file(request.FILES['image'].name, ContentFile(request.FILES['image'].read()))
    ingredients = recognize(image_path)
    # ingredients = request.data.get("ingredients", ["chicken"])
    recipes = get_recipe(ingredients)
    return Response(data={"ingredients": ingredients, "recipes": recipes}, status=status.HTTP_200_OK)
