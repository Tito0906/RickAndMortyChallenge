from functions import check_locations_per_episode, check_ulrs_and_origins, replace_urls_for_origin, imprime_diccionario
from threading import Thread
import time


if __name__ == "__main__":
    start_time = time.time()

    print("-------Parte 2-------")

    print("La lista de urls por episodio se está generando")
    # La siguiente función genera un diccionario cuyas llaves son el índice del episodio
    # los valores son una lista de url de cada personaje que aparece ene se episodio
    locations_per_episode = check_locations_per_episode(
        "https://rickandmortyapi.com/api/episode/?page=")

    print("La lista de origenes por urls se está generando")
    # La siguiente función genera un diccionario cuyas llaves son el url de cada personaje
    # los valores son el origen de cada personaje
    urls_and_origins = check_ulrs_and_origins(
        "https://rickandmortyapi.com/api/character/?page=")

    # La siguiente función reemplaza las url del primer diccionario por los origenes
    # El reemplazo es bastante directo porque cada valor de la lista es la llave del segundo diccionario
    locations_per_episode = replace_urls_for_origin(
        locations_per_episode, urls_and_origins)

    print("se imprime todo lo pedido")
    # Se imprime el diccionario agregando algunos valores
    imprime_diccionario(locations_per_episode)

    print("---FIN Parte 2-------")

    print("--- %s seconds ---" % (time.time() - start_time))
