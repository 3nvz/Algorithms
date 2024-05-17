
 

s = "5F3Z-2e-9-w" 
k = 4

s = s.replace("-", "").upper()
print(s)

first_group_len = len(s) % k
print(first_group_len, "first g length")
      
reformatted = s[:first_group_len]
     
for i in range(first_group_len, len(s), k):
    if reformatted:
        reformatted += "-"
    reformatted += s[i:i+k]