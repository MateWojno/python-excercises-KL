# list is stored in given_list list variable
given_list = [4, 0, 5, 0, 3, 0, 0, 5]

#those two lists will be used to store operations on main list
non_zero_list = []
zeros_list = []

# in for loop for each index(from given_list) in range of given_list length there will be a separation of numbers greater than 0 - those will be stored in non_zero_list and the others (zeros) in zeros_list
for i in range(len(given_list)):
    if given_list[i] !=0:
        non_zero_list.append(given_list[i])
    else:
        zeros_list.append(given_list[i])
# result is non_zero_list + zeros_list, so the non zero will be on the left side, zeros on the right side - you can swap them to do it otherwise
result = (non_zero_list + zeros_list)
print(result)
# i prefer writing in my own IDE (VsCode)
# MateWojno