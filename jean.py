def jean(cm):
  Polegadas = cm/2.54
  pgd = open('arquivo.txt', 'a+', encoding = 'utf-8')
  pgd.write(f'{cm} cintímetros é %.3f em polegadas.\n' %(Polegadas))