title_list = ["egy","kettő","három"]
table = ([["one","dos","fgt"],
          ["drei","vier44","anyu"],
          ["cinco","seis","sdifhhsjd"]])

longest_data_list = []
for row in range(len(table[0])):
    longest_data_list.append(len(table[0][row]))
    for column in range(len(title_list)):
        if longest_data_list[row] < len(table[column][row]):
            longest_data_list[row] = len(table[column][row])

print(longest_data_list)

for i in range(len(longest_data_list)):
    longest_data_list[i] += 2
    
# for i in range(len(table)):
#     for j in range(len(table[i])):
#         print('|', end = '')
#         number_of_spaces = round((longest_data_list[j] - len(table[i][j])) / 2)
#         for spaces in range(number_of_spaces):
#             print(' ', end = '')
#         print(table[i][j], end = '')
#         number_of_spaces = ((longest_data_list[j] - len(table[i][j])) / 2) 
#         if number_of_spaces != round(number_of_spaces):
#             number_of_spaces -= 1    
#         number_of_spaces = round(number_of_spaces)
#         for spaces in range(number_of_spaces):
#             print(' ', end = '')
#     print('')
line_lenght = 0

for k in longest_data_list:
    line_lenght += k
line_lenght += len(table) * 3 + 3

for k in range(line_lenght):
    print('-', end = '')
print('')  

print("|", end = '')
for i in range(len(title_list)):
    print("| {:^{space_length}} ".format(title_list[i], space_length=longest_data_list[i]), end = '')
print('||')
for k in range(line_lenght):
    print('-', end = '')
print('')  

for i in range(len(table)):
    print("|", end = '')
    for j in range(len(table[i])):
        print("| {:^{space_length}} ".format(table[i][j], space_length=longest_data_list[j]), end = '')
    print("||")
    for k in range(line_lenght):
        print('-', end = '')
    print('')    
    