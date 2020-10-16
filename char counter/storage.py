
def check_letter_in_location():
    response = requests.get("https://rickandmortyapi.com/api/location/")
    locations = response.json()

    count = 0
    n = 0

    while n < locations["info"]["count"]:
        locations = response.json()
        # print(type(locations["info"]["next"]))
        for location in locations["results"]:
            algo = chequea(location["name"], "l")
            count += algo
            # print(n)
            n += 1
        if locations["info"]["next"] != None:
            response = requests.get(locations["info"]["next"])

    return count


# episodes
def check_letter_in_episodes():
    response = requests.get("https://rickandmortyapi.com/api/episode/")
    episodes = response.json()

    count = 0
    n = 0

    while n < episodes["info"]["count"]:
        episodes = response.json()
        # print(type(locations["info"]["next"]))
        for episode in episodes["results"]:
            algo = chequea(episode["name"], "e")
            count += algo
            # print(n)
            n += 1
        if episodes["info"]["next"] != None:
            response = requests.get(episodes["info"]["next"])

    return count


# characters

'''
def check_letter_in_characters():
    # Generamos el primer path
    path = "https://rickandmortyapi.com/api/character/?page=" + \
        str(1) + "&name=c"

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
    # una función mediante threads. La función agrega los nombres de la pagina que recibe a la lista
    n = 1
    while n <= characters["info"]["pages"]:
        path = "https://rickandmortyapi.com/api/character/?page=" + \
            str(n) + "&name=c"
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

    # unimos todos los nombres de la lista con los nombres
    todo = "".join(string)

    # revisamos el string creado a partir de la lista
    count = chequea(todo, "c")

    return count
'''
