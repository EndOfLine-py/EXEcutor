#####################
#     EXEcutor      #
#    by Endlassy    #
#                   #
# Clicker like game #
# Pour Casio 90+E   #
#                   #
#####################
import random

global exe
global critch
global total
exe = 1
critch = 5
total = 1

global prix_crit
global prix_exe
global mega_crit
prix_exe = 50
prix_crit = 250

prix_mega = 2500
mega_crit = False

def clear():
  for i in range(5):
    print("\n")

def printui():
  print(" =====EXEcutor======")
  print("Total : "+str(total)+" EXE")
  print("Crit% : "+str(critch))
  print("EXE/e : "+str(exe))
  print("   Shop with 's'")

def printshop(c, mega):
  print(" =======Shop========")
  print("0. Exit")
  print("Total : "+str(total)+" EXE")
  print("1. +EXE/e : "+str(prix_exe)+" EXE")
  if c >= 100:
    print("   Crit% maxed")
  else:
    print("2. +Crit% : "+str(prix_crit)+" EXE")
  if mega == True:
    print("  Mega Crit bought")
  else:
    print("3. Mega Crit : "+str(prix_crit)+" EXE")

def crit(critch, mega):
  if mega == True and random.randint(0,100) <= 1:
    print("!!!MEGA CRIT!!!")
    return 10
  else:
    if critch > 0 and random.randint(0,100) <= critch:
      print("CRIT!")
      return 2
    else:
      return 1

def secret():
  global exe
  global total
  global critch
  global mega_crit
  exe = 99999
  total = 1
  critch = 100
  mega_crit = True

def secret2():
  clear()
  while True:
    print("pti malin a regarder")
    print("le code source x)")
    print("en tout cas gg")
    print("made by lassy with love")
    input("EXE pour quitter")
    break

def shop():
  clear()

  global prix_crit
  global prix_exe
  global exe
  global total
  global critch
  global mega_crit

  while True:
    printshop(critch, mega_crit)
    b = str(input("> "))
    if b == "1": # +exe
      if total >= prix_exe:
        total = total - prix_exe
        exe = exe + 1
        prix_exe = prix_exe + 50
      else:
        pass
    elif b == "2": # +crit %
      if total >= prix_crit:
        if critch >= 100:
          pass
        total = total - prix_crit
        critch = critch + 5
        prix_crit = prix_crit + 250
    elif b == "3": # mega crit
      if total >= prix_mega:
        if mega_crit == True:
          pass
        else:
          total = total - prix_mega
          mega_crit = True
      else:
        pass
    elif b == "0":
      clear()
      break
    else:
      pass

clear()

while True:
  printui()
  a = str(input("> "))
  if str(a) == "":
    total = total + exe * crit(critch, mega_crit)
  elif str(a) == "s":
    shop()
  elif str(a) == "1337":
    secret()
  elif str(a) == "abcde123":
    secret2()
  else:
    pass
  clear()