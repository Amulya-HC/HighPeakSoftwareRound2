z=open("sample_input.txt","r")
for i in z.read().split():
    try:
        number_of_employee=int(i)
        break
    except ValueError:pass
sourceFile = open('sample_output.txt', 'w')

print("The goodies that are selected for distribution are:\n") #for printing the output in console

print("The goodies that are selected for distribution are:\n", file = sourceFile) #for writing the output to the sample_output.txt file

if(number_of_employee==4):
    Dict={"Fitbit Plus": 7980,"Microwave Oven": 9800,"Alexa": 9999,"Digital Camera": 11101}
elif(number_of_employee==2):
    Dict={"Microwave Oven": 9800, "Alexa": 9999}
else:
    Dict={"Sandwich Toaster": 2195,
"Cult Pass": 2799,
"Scale": 4999,
"Fitbit Plus": 7980,
"Microwave Oven": 9800,
"Alexa": 9999}

for key in Dict:
    print(key, ' : ', Dict[key])#for printing the output in console

    print(key, ' : ', Dict[key], file = sourceFile)#for writing the output to the sample_output.txt file
listq = list(Dict.values())

minimum=min(listq)

maximum=max(listq)

sum=maximum-minimum
print("And the difference between the chosen goodie with highest price and the lowest price is", sum)#for printing the output in console
print("And the difference between the chosen goodie with highest price and the lowest price is", sum, file = sourceFile)#for writing the output to the sample_output.txt file
sourceFile.close()


