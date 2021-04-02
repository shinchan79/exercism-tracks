dna_string1 = input("Enter the first DNA string: ")
dna_string2 = input("Enter the second DNA string: ")
count = 0

l1 = list(dna_string1)
l2 = list(dna_string2)
print(l1)
print(l2)

for i, j in zip(l1, l2):
    if i != j:
        count +=1
print(f"Hamming Distance: {count}")