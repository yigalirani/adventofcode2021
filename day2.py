def ex1():
  horiz=depth=0
  for line in open('input2.txt').readlines():
    dir,amount=line.split(' ')
    amount=int(amount)
    if dir=='forward':
      horiz+=amount
    if dir=='down':
      depth+=amount
    if dir=='up':
      depth-=amount
  print(horiz*depth)
def ex2():
  horiz=depth=aim=0
  for line in open('input2.txt').readlines():
    dir,amount=line.split(' ')
    amount=int(amount)
    if dir=='forward':
      horiz+=amount
      depth+=aim*amount
    if dir=='down':
      aim+=amount
    if dir=='up':
      aim-=amount
  print(horiz*depth)
ex1()
ex2()

