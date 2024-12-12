# Example file showing a basic pygame "game loop"
import pygame


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 400))

img_dino = pygame.image.load("dino.png")
img_cactus = pygame.image.load("cactus.png")
img_dino = pygame.transform.scale(img_dino,(100,100))

dino_rect = img_dino.get_rect()
dino_rect.x = 50
dino_rect.y = 300



is_jumping = False
g=1
jump=23
nowjump =jump

cactus_rect = img_cactus.get_rect()
cactus_rect.x = 2000
cactus_rect.y = 330
speed=5

score=0
highscore=0
font=pygame.font.Font(None,36)

clock = pygame.time.Clock()
running = True
gameover = False 


while running:
    score+=1
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
               is_jumping = True
            if event.key == pygame.K_r:
                score=0
                cactus_rect.x=2000
                gameover =False
        if event.type==pygame.MOUSEBUTTONDOWN:
            is_jumping =True
            if gameover:
                score=0
                cactus_rect.x=2000
                gameover =False
    if not gameover:

        if is_jumping:
           dino_rect.y-=nowjump
           nowjump-=g
        if dino_rect.y>300:
           dino_rect.y=300
           nowjump=jump
           is_jumping=False

        cactus_rect.x -= speed
        if cactus_rect.x < 0:
            cactus_rect.x = 1280

        if dino_rect.colliderect(cactus_rect):
            if score>highscore:
                highscore=score
            
            gameover=True


        # fill the screen with a color to wipe away anything from last frame
        screen.fill((255,255,255))
        score_show =font.render(f"Score: {score}",True,(0,0,0))
        screen.blit(score_show,(10,10))
        highscore_show =font.render(f"Hi Score: {highscore}",True,(0,0,0))
        screen.blit(highscore_show,(10,100))

        if gameover:
           gameover_show =font.render(f"GAME OVER",True,(0,0,0))
           screen.blit(gameover_show,(500,100))
        # RENDER YOUR GAME HERE
    screen.blit(img_dino,dino_rect)
    screen.blit(img_cactus,cactus_rect)

        # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()