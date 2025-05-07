from gamebase import GameBase, ImageSprite
import pygame
from random import randint

def main() :
   game = SnakeGame()
   game.run()        
         
class Snake(ImageSprite) :
   def __init__(self, x, y) :
         super().__init__(x, y, "snake.bmp") 
         self._alive = True
         self._layer = 2
 
   def keyDown(self, key) :
      if self._alive :
         distance = 20
         if key == pygame.K_w or key == pygame.K_UP:
            self.moveBy(0, -distance)
         elif key == pygame.K_a  or key == pygame.K_LEFT:
            self.moveBy(-distance, 0)
         elif key == pygame.K_s  or key == pygame.K_DOWN:
            self.moveBy(0, distance)
         elif key == pygame.K_d  or key == pygame.K_RIGHT:
            self.moveBy(distance, 0)
         
   def die(self) :
      if self._alive :
         self.image = pygame.transform.flip(self.image, True, True)
         self._alive = False
             
class Car(ImageSprite) :
   def __init__(self, x, lane) :
      self._lane = lane
      y = 300 + 200 * lane        
      super().__init__(x, y, "car" + str(randint(0, 9)) + ".bmp") 
     
      if lane == 0 :
         self.image = pygame.transform.flip(self.image, True, False)
      self._layer = 1
     
   def update(self) :
      if self._lane == 0 :
         self.rect.x += 1
      else:
         self.rect.x -= 1
     
class SnakeGame(GameBase) :
   def __init__(self) :
     super().__init__(800, 600)        
     self._snake = Snake(400, 600) 
     self._frog = ImageSprite(400, 100, "frog.bmp") 
     self._cars = pygame.sprite.Group()

   def addCar(self, lane) :
      if lane == 0 :
         x = - 100
      else:
         x = self._width
      newCar = Car(x, lane)
      self._cars.add(newCar)
      self.add(newCar)

   def keyDown(self, key) :
      self._snake.keyDown(key)

   def mouseButtonDown(self, x, y) :
      self.quit()
              
   def update(self) :
      super().update()

      if self.getTicks() % 240 == 0 : # Add a new car to each lane
         self.addCar(0)
         self.addCar(1)              

      if self.getTicks() == 480 :
         self.add(self._snake) 
         self.add(self._frog) 
         
      if pygame.sprite.spritecollideany(self._snake, self._cars) :
         self._snake.die()
         
      if (pygame.sprite.collide_rect(self._snake, self._frog)): 
         self._frog.kill()
         self.add(ImageSprite(self._snake.rect.x, self._snake.rect.y, 
            "crown.bmp"))

# Start the program.
main()

