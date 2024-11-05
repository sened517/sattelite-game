import pgzrun
import random
WIDTH=700
HEIGHT=500

lines=[]
sats=[]

for i in range(10):
  satellite=Actor("satellite")
  satellite.x=random.randint(50,650)
  satellite.y=random.randint(50,450)
  sats.append(satellite)


def draw():
  screen.blit("galaxy",(0,0))
  number=1
  for i in sats :
    i.draw()     
    screen.draw.text(str(number),(i.x,i.y+15))
    number+=1

  for i in lines:
    screen.draw.line(i[0],i[1],(255,255,255))

next=0

def on_mouse_down(pos):
  global next,lines,sats   
  if sats [next].collidepoint(pos):
    if next:
      lines.append((sats[next-1].pos,sats[next].pos)) 
    next+=1 
  else:
    lines=[]
    next=0


 









pgzrun.go()