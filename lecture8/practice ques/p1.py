#check the Anagram strings or not
# EX "SILENT" , "ELTNTS"
def is_anagram(str1,str2):
    return sorted(str1.lower()) == sorted(str2.lower())
input_str=input("Enter a string:")
output_str=input("enter a string:")
if is_anagram(input_str,output_str):
    print(f"{output_str} is an anagram of {input_str}")
else:
    print(f"{output_str} is not an of {input_str}")