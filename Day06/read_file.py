file = open("Day06/test_data/testcases.txt",'r')
test_cases  =file.read()
print(test_cases)
file.close()

file = open("Day06/test_data/testcases.txt",'r')
test_cases =file.readlines()
for num in range(1,len(test_cases)+1):
    print(f"Executing Test Case {num}:  {test_cases[num-1].strip()}")
file.close()



file = open("Day06/test_data/testcases.txt",'r')
test_cases =file.readlines()
for num, test_case in enumerate(test_cases, start=1):
    print(f"Executing Test Case {num}: {test_case.strip()}")
file.close()



