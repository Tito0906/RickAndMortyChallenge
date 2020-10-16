from functions import check_letter_in_element
import time


if __name__ == "__main__":
    start_time = time.time()

    print("-------Parte 1-------")

    print("La cantidad de l en los nombres de locations es:")
    count = check_letter_in_element(
        "https://rickandmortyapi.com/api/location/?page=", "location", "l")
    print(count)

    print("La cantidad de e en los nombres de episodios es:")
    count = check_letter_in_element(
        "https://rickandmortyapi.com/api/episode/?page=", "episode", "e")
    print(count)

    print("La cantidad de c en los nombres de characters es:")
    count = check_letter_in_element(
        "https://rickandmortyapi.com/api/character/?page=", "character", "c")
    print(count)

    print("---FIN Parte 1-------")

    print("--- %s seconds ---" % (time.time() - start_time))
