import requests
from threading import Thread, Lock

# La función chequea recibe un string y una letra.
# Devuelve el número de veces que se encontró esa letra en el string


def chequea(string, letra):
    count = 0
    upper = letra.upper()
    lower = letra
    for letter in string:
        if letter == upper:
            count += 1
        elif letter == lower:
            count += 1
    return count

# La función ask_page será llamadas por threadss. Esta recibe un path, una lista de nombres y un lock.
# la función llama al path y agrega todos los nombres de la pagina que recibió a la lista.
# El lock evita que se agreguen elementos a la lista al mismo tiempo en los diferentes threads


def ask_page(path, lista_nombres, lock):
    response = requests.get(path)
    characters = response.json()
    lock.acquire()
    for character in characters["results"]:
        lista_nombres.append(character["name"])
    lock.release()


# Función para generar cada path

def path_generator(path_element, page_number, element, search_letter):
    if element == "character":
        extra_filter = "&name=c"
    elif element == "location":
        extra_filter = "&name=l"
    elif element == "episode":
        extra_filter = "&name=e"
    return path_element + str(page_number) + extra_filter

# Función genérica para recuperar los datos que se piden


def check_letter_in_element(path_element, element, search_letter):
    # Generamos el primer path
    path = path_generator(path_element, 1, element, search_letter)

    # Hacemos el primer llamado
    response = requests.get(path)

    # Generamos el primer json
    characters = response.json()

    # creamos el lock
    lock = Lock()

    # creamos la lista donde irán todos los nombres
    string = []

    # generamos el diccionario con los threads
    threads = {}

    # En las siguientes líneas se crean los path correspondientes a cada página y se llama
    # una función mediante threads. La función agrega los nombres de la pagina que recibe a la lista string
    n = 1
    # se crean tantos threads como páginas
    while n <= characters["info"]["pages"]:
        path = path_generator(path_element, n, element, search_letter)
        threads[str(n)] = Thread(target=ask_page, args=(path, string, lock))
        n += 1

    # Iniciamos todos los threads
    n = 1
    while n <= characters["info"]["pages"]:
        threads[str(n)].start()
        n += 1

    # Hacemos join() con todos los threads
    n = 1
    while n <= characters["info"]["pages"]:
        threads[str(n)].join()
        n += 1

    # unimos todos los nombres de la lista y formamos un solo string
    todo = "".join(string)

    # revisamos el string creado a partir de la lista
    count = chequea(todo, search_letter)

    return count
