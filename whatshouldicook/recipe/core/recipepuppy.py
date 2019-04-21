import requests


class Recipe(object):
    def __init__(self, dict_in):
        self.data = dict_in


def clean():
    def decorator(function_to_execute):
        def modified_function(name):
            return function_to_execute(name).strip()  # On exécute la fonction

        return modified_function

    return decorator


# Global search
def query(name='', ingredient='', page='1'):
    # Handling lists
    if isinstance(ingredient, list):
        li = iter(ingredient)
        obj = next(li)
        ingredient_fin = str(obj) + ', '
        while True:
            try:
                ingredient_fin = ingredient_fin + str(obj) + ', '
                obj = next(li)
            except StopIteration:
                ingredient_fin = ingredient_fin + str(obj)
                break
    else:
        ingredient_fin = ingredient
    try:
        r = requests.get("http://www.recipepuppy.com/api/?", params={'i': ingredient_fin, "q": name, "p": page}).json()
        return r
    except urllib2.URLError as exception_variable:
        # prints the reason for failure out to help debugging
        print
        'Error'
        print
        exception_variable.reason
    except requests.exceptions.HTTPError as exception_variable:
        # prints the HTTP error code that was given
        print
        'Error'
        print
        exception_variable.code
    except requests.exceptions.ConnectionError as exception_variable:
        print
        'Error'
        print
        exception_variable.code
    except requests.exceptions.Timeout as exception_variable:
        print
        exception_variable.code
    except requests.exceptions.TooManyRedirects as exception_variable:
        print
        exception_variable.code
    return None


# get only ingredients
def get_ingredients(name):
    results = query(name=name)
    return results["results"][0]["ingredients"]


def get_recipe(ingredient):
    results = query(name='', ingredient=ingredient)
    return results["results"][0]["title"]


def get_link(name):
    results = query(name)
    return results["results"][0]["href"]


@clean()
def get_clean_ingredient(name):
    results = get_ingredients(name)


@clean()
def get_clean_recipe(name):
    return get_recipe(name)


# Make it a dictionnary
def get_full_info(name='', ingredient='', page='1'):
    results = query(name, ingredient, page)
    # Need to create a dict with all info
    all = dict()
    i = 0
    while i < len(results['results']):
        all[results['results'][i]['title']] = results['results'][i]['ingredients']
        # all[results['results'][i]['title']].append(results['results'][i]['href'])
        i = i + 1
    return Recipe(all)
