"""=================================================================================================
Institute....: Universidad Técnica Nacional
Headquarters.: Pacífico
Career.......: Tecnologías de Información
Course.......: ITI-411 - Programación III
Period.......: I-2022
Documents....: Exam_01 - 01_Stack
Goals........: Using stack class
Professor....: Jorge Ruiz (york)
Student......:
================================================================================================="""
from cls_Stack import cls_Stack

print()
print("Stack implementation")
print("=================================")

# Create stack instance
pilita = cls_Stack()

# Load data chunk into stack while this not full
for letra in "Cuquita":
    if not pilita.full():
        pilita.push(letra)
    else:
        break

while not pilita.empty():
    print(pilita.pop())

