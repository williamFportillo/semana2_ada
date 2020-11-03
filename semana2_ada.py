# -*- coding: utf-8 -*-
"""semana2_ADA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cMlWl8NWB7-4u7rR3g7LohaWQ3bhCjEN

Divide y Venceras
"""

def search(lista,v,l,r):
  if (r-l)<=10:
    return BusquedaIterativa;
  else: 
    c=((r+t)/2)
    if (v<lista[c]):
      search(lista,v,l,c);
    elif (v>lista[c]):
      search(lista,v,c,r);
    else:
      return true

# T(n) = C + 2 * T (n/2)

"""BUSQUEDA BINARIA"""

def biSearch(lista, x):
    if len(lista) == 0:
      return False
    else:
        mid = len(lista) // 2
        if lista[mid] == x:
            return True
        else:
          if x > lista[mid]:
            return biSearch(lista[mid+1:],x)
          else:
            return biSearch(lista[:mid],x)

n = [2,10,17,25,38,55,89,99,120,150]
biSearch(n, 120)

"""MERGE_SORT"""

def merge_sort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        izq = arr[:mid]
        der = arr[mid:]
        izq = merge_sort(izq)
        der = merge_sort(der)
        arr =[]

        while len(izq)>0 and len(der)>0:
            if izq[0]<der[0]:
                arr.append(izq[0])
                izq.pop(0)
            else:
                arr.append(der[0])
                der.pop(0)
        for i in izq:
            arr.append(i)
        for i in der:
            arr.append(i)

    return arr

a = [12, 11, 13, 5, 6, 7 , 18 , 20 , 15]
print(merge_sort(a))

"""PUNTOS MAXIMOS."""

import math
def mezclar(l1, l2):
  if l1 != None and l2 != None:
    merge_sort(l1+l2)
    print(l1 + l2)
  else:
    if l1 != None:
      merge_sort(l1)
      print(l1)
    else:
      merge_sort(l2)
      print(l2)
def maxPoints(lista, sl, sr):
        if sl == sr:
          return [lista[sl][1]]
        if sl+1 == sr:
          if lista[sl][0] > lista[sr][0] and lista[sl][1] > lista[sr][1]:
            return [lista[sl][1]]
          if lista[sr][0] > lista[sl][0] and lista[sr][1] > lista[sl][1]:
            return [lista[sr][1]]
          else:
            return [lista[sl][1],lista[sr][1]]
        dividir = math.ceil((sl + sr) / 2)
        l1 = maxPoints(lista, sl, dividir)
        l2 = maxPoints(lista, dividir+1, sr)
        mezclar(l1,l2)

nums = [(0,1),(1,2),(2,1),(3,3),(4,4)]
maxPoints(nums,0,len(nums)-1)