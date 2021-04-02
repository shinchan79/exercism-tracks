score = input("Enter the score list, separate by space: ")

score_list = score.split()
int_sc_list = []
for i in range(0, len(score_list)):
    score_list[i] = int(score_list[i])
    int_sc_list.append(score_list[i])

print("Return the highest score: " + str(max(int_sc_list)))

print("Return the last added score: " + str(score_list[-1])) 

sorted_list = sorted(int_sc_list)
print(sorted_list)
print("Return three highest scores: " + str(sorted_list[-1]) + " " +  str(sorted_list[-2]) + " " + str(sorted_list[-3])) 