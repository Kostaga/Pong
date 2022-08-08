# Importing the library
import pygame
import random
# Initializing Pygame
pygame.init()
class rect:
  def __init__(self, x, y,width,height,vy):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.vy = vy

class ball:
  def __init__(self, x, y, vx, vy, r):
    self.x = x
    self.y = y
    self.vx = vx
    self.vy = vy
    self.r = r

# Initializing surface
width=800
height=500
surface = pygame.display.set_mode((width, height))
running = True

ball1 = ball(400,250,0.15,0.15,10)
rect1 = rect(30,250-45,15,90,0.2)
rect2 = rect(755, 250-45, 15, 90,0.2)
line = rect(400,0, 3, 500,0)
color = (255, 255, 255)

score1=score2=0
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

flag_win = False
gameover = False
randx = random.randint(0, 1)
randy = random.randint(0, 1)

flag = False
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if running == False:
      pygame.quit()
  keys = pygame.key.get_pressed()
  if (keys[pygame.K_DOWN]):
    rect1.y += rect1.vy
  if (keys[pygame.K_UP]):
    rect1.y -= rect1.vy
  if (keys[pygame.K_w]):
    rect2.y -= rect2.vy
  if (keys[pygame.K_s]):
    rect2.y += rect2.vy
  if (keys[pygame.K_SPACE]):
    flag = True


  if (flag_win):
    ball1 = ball(400, 250, 0.15, 0.15, 10)
    pygame.draw.circle(surface, color, (ball1.x, ball1.y), ball1.r)
    flag = False
    flag_win = False
    randx = random.randint(0, 1)
    randy = random.randint(0, 1)

  textsurface1 = myfont.render(f'Score 1: {score1}', False, (255, 255, 255))
  textsurface2 = myfont.render(f'Score 2: {score2}', False, (255, 255, 255))
  surface.fill(0)
  surface.blit(textsurface1, (10, 0))
  surface.blit(textsurface2, (640, 0))
  # BALL
  if (not gameover):
    pygame.draw.circle(surface,color, (ball1.x,ball1.y), ball1.r)
  if (flag):
    if (randx==1 and randy==1):
      ball1.x += ball1.vx
      ball1.y += ball1.vy
    elif (randx==1 and randy==0):
      ball1.x += ball1.vx
      ball1.y -= ball1.vy
    elif (randx==0 and randy==1):
      ball1.x -= ball1.vx
      ball1.y += ball1.vy
    else:
      ball1.x -= ball1.vx
      ball1.y -= ball1.vy

  #limits
  if (rect1.y<=0):
    rect1.y=0
  if (rect1.y+rect1.height>height):
    rect1.y=height-rect1.height
  if (rect2.y <= 0):
    rect2.y = 0
  if (rect2.y + rect2.height > height):
    rect2.y = height - rect2.height
  #collision
  if ((rect1.x + rect1.width >= ball1.x) and (rect1.x <= ball1.x + ball1.r)
  and (rect1.y + rect1.height >= ball1.y) and (rect1.y <= ball1.y + ball1.r)):
    if (ball1.y+ball1.r>(rect1.y+rect1.height)/2):
        ball1.vx=-ball1.vx
    else:
      ball1.vx = -ball1.vx
      ball1.vy = -ball1.vy

  if ((rect2.x + rect2.width >= ball1.x) and (rect2.x <= ball1.x + ball1.r)
          and (rect2.y + rect2.height >= ball1.y) and (rect2.y <= ball1.y + ball1.r)):
    if (ball1.y + ball1.r > (rect2.y + rect2.height)/2):
      ball1.vx = -ball1.vx
    else:
      ball1.vx = -ball1.vx
      ball1.vy = -ball1.vy

  #limits
  if (ball1.y<=0 or ball1.y+ball1.r>height):
    ball1.vy=-ball1.vy
  if (ball1.x<=0 and not flag_win):
    score2+=1
    flag_win=True

  if (ball1.x+ball1.r>width and not flag_win):
    score1+=1
    flag_win=True

  if (score1==5 or score2==5):
    wintext = myfont.render(f'Game Over', False, (255, 255, 255))
    surface.blit(wintext, (280, 250))
    if (score1==5):
      player1text = myfont.render(f'Player 1 wins', False, (255, 255, 255))

    else:
      player1text = myfont.render(f'Player 2 wins', False, (255, 255, 255))
    surface.blit(player1text, (280, 400))
    gameover=True




  # Drawing Rectangle
  if (not gameover):
    pygame.draw.rect(surface, color, pygame.Rect(rect1.x, rect1.y, rect1.width, rect1.height))
    pygame.draw.rect(surface, color, pygame.Rect(rect2.x, rect2.y, rect2.width, rect2.height))
    pygame.draw.rect(surface, color, pygame.Rect(line.x, line.y, line.width, line.height))
  pygame.display.flip()



