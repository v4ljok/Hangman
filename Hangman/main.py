import pygame
from pygame import mixer
from randomizer import randomword
import time

pygame.init()
screen = pygame.display.set_mode((720, 720))
pygame.display.set_caption('Hangman')
clock = pygame.time.Clock()
title = pygame.font.Font('font/Rock Show Whiplash.ttf', 150)
mediumtext = pygame.font.Font('font/Rock Show Whiplash.ttf', 40)

background = pygame.image.load('images/background.png')

loading_ring = pygame.image.load('images/circle.png')
loading_ring.set_colorkey((255, 255, 255))
loading_ring = pygame.transform.scale(loading_ring, (loading_ring.get_width()//2, loading_ring.get_height()//2))

gallows = pygame.image.load('images/gallows.jpg')
gallows.set_colorkey((255, 255, 255))
gallows = pygame.transform.scale(gallows, (gallows.get_width()//2.5, gallows.get_height()//2.5))

head = pygame.image.load('images/face.png').convert_alpha()
head = pygame.transform.scale(head, (head.get_width()//2.5, head.get_height()//2.5))

hands = pygame.image.load('images/hands.jpg')
hands.set_colorkey((255, 255, 255))
hands = pygame.transform.scale(hands, (hands.get_width()//2.5, hands.get_height()//2.5))

legs = pygame.image.load('images/legs.jpg')
legs.set_colorkey((255, 255, 255))
legs = pygame.transform.scale(legs, (legs.get_width()//2.5, legs.get_height()//2.5))

title_surf = title.render('Hangman', True, 'Black')
undertitle_surf = mediumtext.render('click on the mouse button to start...', True, 'Black')
loadingtext_surf = mediumtext.render('Generating a word...', True, 'Black')
restart_surf = mediumtext.render('click on the mouse button to restart...', True, 'Black')

misssound = mixer.Sound('sound/miss.wav')
misssound.set_volume(0.1)
notmisssound = mixer.Sound('sound/notmiss.wav')
notmisssound.set_volume(0.1)
losesound = mixer.Sound('sound/lose.wav')
losesound.set_volume(0.1)
winsound = mixer.Sound('sound/win.wav')
winsound.set_volume(0.1)
clicksound = mixer.Sound('sound/click.wav')
clicksound.set_volume(0.1)

current_scene = None
def switch_scene(scene):
    global current_scene
    current_scene = scene

def start_scene():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                switch_scene(None)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                switch_scene(loading_scene)
                running = False
        
        screen.blit(background,(0,0))   
        screen.blit(title_surf,(125,170))
        screen.blit(undertitle_surf,(125,500))

        pygame.display.update()
        clock.tick(60)

def loading_scene():
    clicksound.play()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                switch_scene(None)
            
        screen.blit(background,(0,0))   
        screen.blit(loading_ring,(250,170))
        screen.blit(loadingtext_surf,(220,500))

        switch_scene(mainscene)
        running = False
        
        pygame.display.update()
        clock.tick(60)

def mainscene():  
    word = randomword()
    splitted_word = list(word)
    guessed = ['_' for i in splitted_word]
    hidden_word = " ".join(guessed)
    hidden_word_surf = mediumtext.render(hidden_word, True, 'Black')
    hidden_word_rect = hidden_word_surf.get_rect(midbottom = (360,540))
    attempts = 4
    miss = 4

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                switch_scene(None)
            
            if '_' not in guessed:
                switch_scene(winscene)
                running = False
            
            if attempts == 0:
                switch_scene(losescene)
                running = False
     
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    char = "q"
                    if char in splitted_word:
                        for i, c in enumerate(splitted_word):
                            if c == char:
                                notmisssound.play()
                                guessed[i] = char
                                hidden_word = " ".join(guessed)
                                hidden_word_surf = mediumtext.render(hidden_word, True, 'Black')

                    else:
                        attempts -= 1
                if event.key == pygame.K_w:
                    char = "w"
                    if char in splitted_word:
                        for i, c in enumerate(splitted_word):
                            if c == char:
                                notmisssound.play()
                                guessed[i] = char
                                hidden_word = " ".join(guessed)
                                hidden_word_surf = mediumtext.render(hidden_word, True, 'Black')

                    else:
                        attempts -= 1
                if event.key == pygame.K_e:
                    char = "e"
                    if char in splitted_word:
                        for i, c in enumerate(splitted_word):
                            if c == char:
                                notmisssound.play()
                                guessed[i] = char
                                hidden_word = " ".join(guessed)
                                hidden_word_surf = mediumtext.render(hidden_word, True, 'Black')

                    else:
                        attempts -= 1
                if event.key == pygame.K_r:
                    char = "r"
                    if char in splitted_word:
                        for i, c in enumerate(splitted_word):
                            if c == char:
                                notmisssound.play()
                                guessed[i] = char
                                hidden_word = " ".join(guessed)
                                hidden_word_surf = mediumtext.render(hidden_word, True, 'Black')

                    else:
                        attempts -= 1
                if event.key == pygame.K_t:
                    char = "t"
                    if char in splitted_word:
                        for i, c in enumerate(splitted_word):
                            if c == char:
                                notmisssound.play()
                                guessed[i] = char
                                hidden_word = " ".join(guessed)
                                hidden_word_surf = mediumtext.render(hidden_word, True, 'Black')

                    else:
                        attempts -= 1
                if event.key == pygame.K_y:
                    char = "y"
                    if char in splitted_word:
                        for i, c in enumerate(splitted_word):
                            if c == char:
                                notmisssound.play()
                                guessed[i] = char
                                hidden_word = " ".join(guessed)
                                hidden_word_surf = mediumtext.render(hidden_word, True, 'Black')

                    else:
                        attempts -= 1
                if event.key == pygame.K_u:
                    char = "u"
                    if char in splitted_word:
                        for i, c in enumerate(splitted_word):
                            if c == char:
                                notmisssound.play()
                                guessed[i] = char
                                hidden_word = " ".join(guessed)
                                hidden_word_surf = mediumtext.render(hidden_word, True, 'Black')

                    else:
                        attempts -= 1
                if event.key == pygame.K_i:
                    char = "i"
                    if char in splitted_word:
                        for i, c in enumerate(splitted_word):
                            if c == char:
                                notmisssound.play()
                                guessed[i] = char
                                hidden_word = " ".join(guessed)
                                hidden_word_surf = mediumtext.render(hidden_word, True, 'Black')

                    else:
                        attempts -= 1
                if event.key == pygame.K_o:
                    char = "o"
                    if char in splitted_word:
                        for i, c in enumerate(splitted_word):
                            if c == char:
                                notmisssound.play()
                                guessed[i] = char
                                hidden_word = " ".join(guessed)
                                hidden_word_surf = mediumtext.render(hidden_word, True, 'Black')

                    else:
                        attempts -= 1
                if event.key == pygame.K_p:
                    char = "p"
                    if char in splitted_word:
                        for i, c in enumerate(splitted_word):
                            if c == char:
                                notmisssound.play()
                                guessed[i] = char
                                hidden_word = " ".join(guessed)
                                hidden_word_surf = mediumtext.render(hidden_word, True, 'Black')

                    else:
                        attempts -= 1
                if event.key == pygame.K_a:
                    char = "a"
                    if char in splitted_word:
                        for i, c in enumerate(splitted_word):
                            if c == char:
                                notmisssound.play()
                                guessed[i] = char
                                hidden_word = " ".join(guessed)
                                hidden_word_surf = mediumtext.render(hidden_word, True, 'Black')

                    else:
                        attempts -= 1
                if event.key == pygame.K_s:
                    char = "s"
                    if char in splitted_word:
                        for i, c in enumerate(splitted_word):
                            if c == char:
                                notmisssound.play()
                                guessed[i] = char
                                hidden_word = " ".join(guessed)
                                hidden_word_surf = mediumtext.render(hidden_word, True, 'Black')

                    else:
                        attempts -= 1
                if event.key == pygame.K_d:
                    char = "d"
                    if char in splitted_word:
                        for i, c in enumerate(splitted_word):
                            if c == char:
                                notmisssound.play()
                                guessed[i] = char
                                hidden_word = " ".join(guessed)
                                hidden_word_surf = mediumtext.render(hidden_word, True, 'Black')

                    else:
                        attempts -= 1
                if event.key == pygame.K_f:
                    char = "f"
                    if char in splitted_word:
                        for i, c in enumerate(splitted_word):
                            if c == char:
                                notmisssound.play()
                                guessed[i] = char
                                hidden_word = " ".join(guessed)
                                hidden_word_surf = mediumtext.render(hidden_word, True, 'Black')

                    else:
                        attempts -= 1
                if event.key == pygame.K_g:
                    char = "g"
                    if char in splitted_word:
                        for i, c in enumerate(splitted_word):
                            if c == char:
                                notmisssound.play()
                                guessed[i] = char
                                hidden_word = " ".join(guessed)
                                hidden_word_surf = mediumtext.render(hidden_word, True, 'Black')

                    else:
                        attempts -= 1
                if event.key == pygame.K_h:
                    char = "h"
                    if char in splitted_word:
                        for i, c in enumerate(splitted_word):
                            if c == char:
                                notmisssound.play()
                                guessed[i] = char
                                hidden_word = " ".join(guessed)
                                hidden_word_surf = mediumtext.render(hidden_word, True, 'Black')

                    else:
                        attempts -= 1
                if event.key == pygame.K_j:
                    char = "j"
                    if char in splitted_word:
                        for i, c in enumerate(splitted_word):
                            if c == char:
                                notmisssound.play()
                                guessed[i] = char
                                hidden_word = " ".join(guessed)
                                hidden_word_surf = mediumtext.render(hidden_word, True, 'Black')

                    else:
                        attempts -= 1
                if event.key == pygame.K_k:
                    char = "k"
                    if char in splitted_word:
                        for i, c in enumerate(splitted_word):
                            if c == char:
                                notmisssound.play()
                                guessed[i] = char
                                hidden_word = " ".join(guessed)
                                hidden_word_surf = mediumtext.render(hidden_word, True, 'Black')

                    else:
                        attempts -= 1
                if event.key == pygame.K_l:
                    char = "l"
                    if char in splitted_word:
                        for i, c in enumerate(splitted_word):
                            if c == char:
                                notmisssound.play()
                                guessed[i] = char
                                hidden_word = " ".join(guessed)
                                hidden_word_surf = mediumtext.render(hidden_word, True, 'Black')

                    else:
                        attempts -= 1
                if event.key == pygame.K_z:
                    char = "z"
                    if char in splitted_word:
                        for i, c in enumerate(splitted_word):
                            if c == char:
                                notmisssound.play()
                                guessed[i] = char
                                hidden_word = " ".join(guessed)
                                hidden_word_surf = mediumtext.render(hidden_word, True, 'Black')

                    else:
                        attempts -= 1
                if event.key == pygame.K_x:
                    char = "x"
                    if char in splitted_word:
                        for i, c in enumerate(splitted_word):
                            if c == char:
                                notmisssound.play()
                                guessed[i] = char
                                hidden_word = " ".join(guessed)
                                hidden_word_surf = mediumtext.render(hidden_word, True, 'Black')

                    else:
                        attempts -= 1
                if event.key == pygame.K_c:
                    char = "c"
                    if char in splitted_word:
                        for i, c in enumerate(splitted_word):
                            if c == char:
                                notmisssound.play()
                                guessed[i] = char
                                hidden_word = " ".join(guessed)
                                hidden_word_surf = mediumtext.render(hidden_word, True, 'Black')

                    else:
                        attempts -= 1
                if event.key == pygame.K_v:
                    char = "v"
                    if char in splitted_word:
                        for i, c in enumerate(splitted_word):
                            if c == char:
                                notmisssound.play()
                                guessed[i] = char
                                hidden_word = " ".join(guessed)
                                hidden_word_surf = mediumtext.render(hidden_word, True, 'Black')

                    else:
                        attempts -= 1
                if event.key == pygame.K_b:
                    char = "b"
                    if char in splitted_word:
                        for i, c in enumerate(splitted_word):
                            if c == char:
                                notmisssound.play()
                                guessed[i] = char
                                hidden_word = " ".join(guessed)
                                hidden_word_surf = mediumtext.render(hidden_word, True, 'Black')

                    else:
                        attempts -= 1
                if event.key == pygame.K_n:
                    char = "n"
                    if char in splitted_word:
                        for i, c in enumerate(splitted_word):
                            if c == char:
                                notmisssound.play()
                                guessed[i] = char
                                hidden_word = " ".join(guessed)
                                hidden_word_surf = mediumtext.render(hidden_word, True, 'Black')

                    else:
                        attempts -= 1
                if event.key == pygame.K_m:
                    char = "m"
                    if char in splitted_word:
                        for i, c in enumerate(splitted_word):
                            if c == char:
                                notmisssound.play()
                                guessed[i] = char
                                hidden_word = " ".join(guessed)
                                hidden_word_surf = mediumtext.render(hidden_word, True, 'Black')

                    else:
                        attempts -= 1
                
                if miss > attempts:
                    misssound.play()
                    miss = attempts
            
        screen.blit(background,(0,0))
        screen.blit(hidden_word_surf,hidden_word_rect)
        
        if attempts <= 3:
            screen.blit(gallows,(310,0))
        if attempts <= 2:
            screen.blit(head,(335,135))
        if attempts <= 1:
            screen.blit(hands,(335,225))
        if attempts == 0:
            screen.blit(legs,(338,293))
               
        pygame.display.update()
        clock.tick(60)

def losescene():
    time.sleep(2)
    losesound.play()
    lose_surf = title.render("You lose", True, 'Black')

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                switch_scene(None)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                switch_scene(loading_scene)
                running = False
        
        screen.blit(background,(0,0))
        screen.blit(lose_surf,(125,170))
        screen.blit(restart_surf,(125,500))

        pygame.display.update()
        clock.tick(60) 

def winscene():
    time.sleep(2)
    winsound.play()
    win_surf = title.render("You win", True, 'Black')
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                switch_scene(None)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                switch_scene(loading_scene)
                running = False
        
        screen.blit(background,(0,0))
        screen.blit(win_surf,(125,170))
        screen.blit(restart_surf,(125,500))

        pygame.display.update()
        clock.tick(60) 

switch_scene(start_scene)
while current_scene is not None:
    current_scene()