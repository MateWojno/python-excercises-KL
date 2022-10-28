print("\nHow many lines will there be?:")

# check for vovels on consonants from given list
vovels = list('aeiouy')
consonants   = list("bcdfghjklmnpqrstvwxyz")
end_program = ''
# input validation - checks if input is an integer
while end_program != "q":
    try:
        number_of_lines = int(input())
    except ValueError or number_of_lines == 0:
        print("Try again")
        continue

#   control loop - to control while loop, when number of lines==control_loop loop breaks; - it was supposed to validate input but i don't have time to refactor it now.
    control_loop = 0
    line = []

    while (control_loop != number_of_lines):
        try:
            #input is in lowerCase and whitespace is stripped
            line_input = str(input("Enter your line there: ")).lower().strip()
            line.append(line_input)
            control_loop += 1
        except ValueError:
            print("Only valid words in lowercase")
            break  
#   line list is joined to a single string
    list_output= ("".join(line))

#   vovel/cons counters
    vovels_num = 0
    cons_num = 0
#   for each char[i] in range - length of joined single string it will check for vovels or consonants and assign proper value to counters
    for i in range (len(list_output)):
        if list_output[i] in vovels:
            # print("vovel") - to debug
            vovels_num += 1
            
        if list_output[i] in consonants: 
            # print("consonant") - to debug
            cons_num += 1

#   this is self explanatory - result
    print("\nNumber of vovels: " + str(vovels_num) + "\nNumber of consonants: " + str(cons_num))
    print("Press 'q' to end: ")
    end_program = input()

#   MateWojno, done in VsCode