# -*- coding: utf-8 -*-
from random import randint
import time
fichier = open("listmot.txt","rwa+")
print "fichier ouvert"

attente = 0

l = fichier.readlines()
print len(l)

s = []

for j in range(len(l)):
  a = ""
  for k in range(len(l[j])):
    if l[j][k] == "	" or l[j][k] == "\n":
          a+="\n"
          break
    a+=l[j][k]
  s.append(a)
  attente = attente + 1
  print attente*1./(295063)*100

fo = open("essai.txt", 'w')
for l in range(len(s)):
  print (l*1./295063)*100
  fo.write(s[l])
  for m in range(50):
    fo.write(str(randint(0,9)))
  fo.write("\n")
fo.close()

print "terminé"
