import pygame

class GameBase:
   def __init__(self, width, height):
      pygame.init()
      self._width = width
      self._height = height
 
      self._display = pygame.display.set_mode((self._width, self._height))
      self._clock = pygame.time.Clock()
      self._framesPerSecond = 30
      self._sprites = pygame.sprite.LayeredUpdates()
      self._ticks = 0
      pygame.key.set_repeat(1, 120)
  
   def mouseButtonDown(self, x, y):
      return
 
   def keyDown(self, key) :
      return
    
   def update(self) :
      self._sprites.update()
    
   def draw(self) :
      self._sprites.draw(self._display)
    
   def add(self, sprite) :
      self._sprites.add(sprite)
        
   def getTicks(self):
      return self._ticks
        
   def quit(self) :
      pygame.quit()        
    
   def run(self):
      while True:
         for event in pygame.event.get() :
            if event.type == pygame.QUIT :
               self.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN :                    
               self.mouseButtonDown(event.pos[0], event.pos[1])
            elif event.type == pygame.KEYDOWN :
               self.keyDown(event.key)
                    
         self.update()
         WHITE = (255, 255, 255)
         self._display.fill(WHITE)
         self.draw()
         pygame.display.update()
         self._clock.tick(self._framesPerSecond)
         self._ticks += 1
    
class ImageSprite(
      pygame.sprite.Sprite):
   def __init__(self, x, y, filename) :
      super().__init__()
      self.loadImage(x, y, filename)
 
   def loadImage(self, x, y, filename) :
      img = pygame.image.load(filename).convert()
      MAGENTA = (255, 0, 255)
      img.set_colorkey(MAGENTA)
      self.image = img
      self.rect = self.image.get_rect()
      self.rect.x = x
      self.rect.y = y - self.rect.height
     
   def moveBy(self, dx, dy) :
      self.rect.x += dx
      self.rect.y += dy
 

