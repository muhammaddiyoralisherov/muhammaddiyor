def cash_machine_behavior(L1 , L2):
    
    person_1 = 3
    person_2 =3
    
    for action1, action2 in zip(L1,L2):
        if action1 =="share"and action2 =="share":
            person_1 +=2
            person_2 +=2
        elif action1 =="share" and action2 =="steal":
            person_1 +=3
            person_2 +=0
        elif action1 =="steal" and action2 =="steal":
            person_1 +=1
            person_2 +=1
            
            return person_1 ,person_2
L1 = input("Birinchi odamning harakatlarini kiriting (masalan, ['share', 'steal']): ").strip('[]').replace(" ", "").split(',')
L2 = input("Birinchi odamning harakatlarini kiriting (masalan, ['share', 'steal']): ").strip('[]').replace(" ", "").split(',')
result = cash_machine_behavior(L1 ,L2)
print(f"Birinchi odam: {result[0]} tanga, Ikkinchi odam: {result[1]} tanga")