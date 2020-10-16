import requests
from threading import Thread, Lock

# Genera una url para cada cambio de pagina


def path_generator(path_element, page_number):
    return path_element + str(page_number)

# Esta función se corre en un thread y sirve para agregar a un diccionario los indices y
# personajes de cada episodio. La llave es el índice y el valor es una lista con urls de todos
# los personajes


def ask_episodes_characters(path, chararacter_urls_in_episode, lock):
    response = requests.get(path)
    page = response.json()
    for episode in page["results"]:
        lock.acquire()
        chararacter_urls_in_episode[str(episode["id"])] = (
            episode["characters"])
        lock.release()


# Genera todo el diccionario completo y es el punto desde donde se crean los thread de
# ask_episodes_characters
def check_locations_per_episode(path_element):
    # Generamos el primer path
    path = path_generator(path_element, 1)

    # Hacemos el primer llamado
    response = requests.get(path)

    # Generamos el primer json
    episodes = response.json()
    # print(characters)

    # creamos el lock
    lock = Lock()

    # creamos el diccionario ["indice_episodio"]=[lista de urls]
    chararacter_urls_in_episode = {}

    # generamos el diccionario con los threads
    threads = {}

    # En las siguientes líneas se crean los path correspondientes a cada página y se llama
    # una función mediante threads. La función agrega keys y values de nombres y origin.
    n = 1
    # se crean tantos threads como páginas
    while n <= episodes["info"]["pages"]:
        path = path_generator(path_element, n)
        threads[str(n)] = Thread(target=ask_episodes_characters,
                                 args=(path, chararacter_urls_in_episode, lock))
        n += 1

    # Iniciamos todos los threads
    n = 1
    while n <= episodes["info"]["pages"]:
        threads[str(n)].start()
        n += 1

    # Hacemos join() con todos los threads
    n = 1
    while n <= episodes["info"]["pages"]:
        threads[str(n)].join()
        n += 1

    return chararacter_urls_in_episode


# función dirigida a thread. agrega a un diccionario común los url de cada personaje (como llaves)
# y los valores son el lugar de origen de cada personaje
def ask_characters_url(path, dicc_urls_origins, lock):
    response = requests.get(path)
    page = response.json()
    for character in page["results"]:
        lock.acquire()
        dicc_urls_origins[str(character["url"])] = (
            character["origin"]["name"])
        lock.release()


# Función desde donde se originan lo thread anteriores y donde se genera
# el diccionario común
def check_ulrs_and_origins(path_element):
    # Generamos el primer path
    path = path_generator(path_element, 1)

    # Hacemos el primer llamado
    response = requests.get(path)

    # Generamos el primer json
    characters = response.json()
    # print(characters)

    # creamos el lock
    lock = Lock()

    # creamos el diccionario tipo ["url_de_character"]=origen de character
    dicc_urls_origins = {}

    # generamos el diccionario con los threads
    threads = {}

    # En las siguientes líneas se crean los path correspondientes a cada página y se llama
    # una función mediante threads. La función agrega keys y values de nombres y origin.
    n = 1
    # se crean tantos threads como páginas
    while n <= characters["info"]["pages"]:
        path = path_generator(path_element, n)
        threads[str(n)] = Thread(target=ask_characters_url,
                                 args=(path, dicc_urls_origins, lock))
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

    for i in dicc_urls_origins.keys():
        # print(i)
        # print(dicc_urls_origins[i])
        pass

    return dicc_urls_origins


# Función que reemplaza del diccinario tipo ["indice_episodio"] = [lista_de_urls], El valor de cada url
# por el valor de origen del personaje que representa esa url
# Para esto se ua otro diccionario tipo ["url_de_un_personaje"] = [origen_del_personaje]
def replace_urls_for_origin(chararacter_urls_in_episode, dicc_urls_origins):
    for episode in chararacter_urls_in_episode.keys():
        for i in range(0, len(chararacter_urls_in_episode[episode])):
            chararacter_urls_in_episode[episode][i] = dicc_urls_origins[chararacter_urls_in_episode[episode][i]]

    return chararacter_urls_in_episode


# Imprime todo lo pedido desde el diccionario resultado de la función anterior
def imprime_diccionario(charater_origins_per_episode):
    for i in charater_origins_per_episode.keys():
        print("##############################")
        print(
            f"El episodio numero #{i} tiene los sigueintes lugares de origenes")
        charater_origins_per_episode[i] = list(
            dict.fromkeys(charater_origins_per_episode[i]))
        print(len(charater_origins_per_episode[i]))
        print(charater_origins_per_episode[i])
