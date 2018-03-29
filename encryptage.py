# -*- coding: utf-8 -*-
from random import randint
import time

namefichier = input("nom du fichier à encrypter")

fichier1 = open(namefichier+".txt","rwa+")
print "fichier 2 ouvert"

l = fichier1.readlines()

print l

s = []

for k in range(len(l)):
  a = ""
  for j in range(len(l[k])):
    if l[k][j] == " ":
      s.append(a)
      a = ""
    if l[k][j] == "\n":
      s.append(a)
      s.append("\n")
      a = ""
    if l[k][j] != " " and l[k][j] != "\n":
      a+=l[k][j]
  if a != "":
    s.append(a)
    a = ""

print s

fichier2 = open("essai.txt","rwa+")
print "fichier 2 ouvert"

z = fichier2.readlines()


fo = open("encryp.txt", 'w')

p = []


for o in s:
  m = o+"\n"
  for n in range(len(z)):
    if m == z[n]:
      p.append(z[n+1])

print p

for t in p:
  print str(t)
  fo.write(t)

fo.close
