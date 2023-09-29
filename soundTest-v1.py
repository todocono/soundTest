
# Imports
import sys
import pygame

# Configuration
pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

font = pygame.font.SysFont('Arial', 40)

playing1 = False
playing2 = False
playing3 = False

# create separate Channel objects for simultaneous playback
channel1 = pygame.mixer.Channel(0) # argument must be int
channel2 = pygame.mixer.Channel(1)
channel2 = pygame.mixer.Channel(3)


pygame.mixer.init()

#############
sound1 = pygame.mixer.Sound("1.wav")
sound2 = pygame.mixer.Sound("2.wav")
sound3 = pygame.mixer.Sound("3.wav")
#############

objects = []

class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.buttonText = buttonText
        self.onclickFunction = onclickFunction
        self.onePress = onePress

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

        self.alreadyPressed = False

        objects.append(self)

    def process(self):

        mousePos = pygame.mouse.get_pos()

        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])

            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])

                if self.onePress:
                    self.onclickFunction()

                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True

            else:
                self.alreadyPressed = False

        self.buttonSurf = font.render(self.buttonText, True, (20, 20, 20))
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)


text_button1 = "Play Tracks"
def track1():
  global playing1
  if playing1 == False:
    playing1 = True
    text_button1 = "Stop All Tracks"
    customButton1.buttonText = "Stop All Tracks"
    print("Playing all sounds")
    channel1 = pygame.mixer.Sound.play(sound1)
    channel1.set_volume(0, 1)
    channel2 = pygame.mixer.Sound.play(sound2)
    channel2.set_volume(1, 0)
    channel3 = pygame.mixer.Sound.play(sound3)
    channel3.set_volume(1, 0)
  else:
    playing1 = False
    customButton1.buttonText = "Play All Tracks"
    print("Stopping all sound")
    pygame.mixer.stop()


def track2():
  global playing2
  if playing2 == False:
    playing2 = True
    print("Toggling sound 2 OFF")
    pygame.mixer.Sound.set_volume(sound2, 0)
    channel2.set_volume(0, 0)
  else:
    playing2 = False
    print("Toggling sound 2 ON")
    pygame.mixer.Sound.set_volume(sound2, 1)
    #pygame.mixer.Sound.set_volume(sound2, 1)



def track3():
  global playing3
  if playing3 == False:
    playing3 = True
    print("Toggling sound 3 OFF")
    pygame.mixer.Sound.set_volume(sound3, 0)
  else:
    playing3 = False
    print("Toggling sound 3 ON")
    pygame.mixer.Sound.set_volume(sound3, 1)

customButton1 = Button(30, 30, 400, 100, text_button1, track1)
customButton2 = Button(30, 140, 400, 100, 'Toggle Sound 2', track2)
customButton3 = Button(30, 250, 400, 100, 'Toggle Sound 3', track3)

# Game loop.
while True:
    screen.fill((20, 20, 20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for object in objects:
        object.process()

    pygame.display.flip()
    fpsClock.tick(fps)




#pygame.mixer.Channel(0).play(pygame.mixer.Sound('1.wav'))
#pygame.mixer.Channel(1).play(pygame.mixer.Sound('2.wav'))
#pygame.mixer.Channel(2).play(pygame.mixer.Sound('2.wav'))




'''from guizero import App, Text, PushButton



def track1():
  print("Playing sound 1")
  message.value = "Playing sound 1"
  #pygame.mixer.Sound.play(sound1)


def track2():
  print("Playing sound 2")
  message.value = "Playing sound 2"
  #pygame.mixer.Sound.play(sound2)


def track3():
  print("Playing sound 3")
  message.value = "Playing sound 3"
  #pygame.mixer.Sound.play(sound3)

app = App()
message = Text(app)
button1 = PushButton(app, command=track1)
button2 = PushButton(app, command=track2)
button3 = PushButton(app, command=track3)

app.display()'''