"""
Dada una nota alamacenada en una variable, imprime su equivalente;
* Mayor o iguala 0, pero menor que 5, SUSPENSO.
*Mayor o igual a 5, pero menor que 6, SUFICIENTE.
* Mayor o igual a 6, pero menor que 7, BIEN.
* Mayor o igual a 7, pero menor que 9, NOTABLE.
* Mayor o igual a 9, pero menor o igual a 10, SOBRESALIENTE.
En cualquier otro caso, imprimir el texto: NOTA NO VÁLIDA.
""" 
nota = 5
if nota>0 and nota<5:
    print("Suspenso")
elif nota>=5 and nota<6:
    print("SUFICIENTE")
elif nota>=6 and nota<7:
    print("BIEN")
elif nota>=7 and nota<9:
    print("NOTABLE")
elif nota>=9 and nota<=10:
    print("SOBRESALIENTE")
else:
    print("NOTA NO VÁLIDA")