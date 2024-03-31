#definindo a origem do robo
origem_x=int(input("Digite a coordenada x do ponto de origem do robô: "))
origem_y=int(input("Digite a coordenada y do ponto de origem do robô: "))
#definindo a quantidade de segundos de movimento
Passos=int(input("Digite por quanto tempo o robô irá se movimentar: "))
#igualando a origem com o final pra iniciar o loop
final_x= origem_x 
final_y= origem_y 
#variaveis usadas para definir qual parte do loop vai rodar
cima=1
lado=0
#loop
while Passos > 0 :
  if cima==1 and lado==0 :
    final_y= final_y + 1
    
    cima=0
    lado=1
    print("O robo passou pela posição: ","(",final_x,",",final_y,")")
  elif cima==0 and lado==1:
    final_x=final_x +1
    
    cima=0
    lado=2
    print("O robo passou pela posição: ","(",final_x,",",final_y,")")
  elif cima==0 and lado==2:
    final_x=final_x +1
    
    cima=1
    lado=0
    print("O robo passou pela posição: ","(",final_x,",",final_y,")")
  #diminuindo a quantidade de passos o loop ter fim
  Passos= Passos - 1
  
#print da posição final
print("Ao final da execução o robô estará no ponto (",final_x,",",final_y,")")
  