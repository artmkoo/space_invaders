import sys
import pygame

def run_game():
    #inicjalizacja gry i utworzenie obiektu ekranu
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Inwazja obcych")

    #Zdefiniowanie koloru tła
    bg_color = (230, 230, 230)

    #Rozpoczęcie głównej pętli gry
    while True:

        #Oczekiwanie na nacisniecie klawisza lub przycisku myszy
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #Odświeżenie ekranu w trakcie każdej iteracji pentli
        screen.fill(bg_color)

        #Wyświetlanie ostatnio zmodyfikowanego ekranu
        pygame.display.flip()

run_game()
print(test)