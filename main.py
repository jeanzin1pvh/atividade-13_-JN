from jean import *
while True:
  try:
    jl = float(input('Digite o valor em centímetros: '))
    break
  except:
    continue
jean(jl)