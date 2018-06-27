# 'all' and 'any' used for boolean checks
list_A = [True, True, False]
any(list_A) #yeilds True, checks for any True's
all(list_A) #yeilds False, checks for all True's. 

## Examples
nums = [1,2,3,-5]

alpha = [el for el in nums if el > 0]
print(alpha)
# want a list that contains booleans 
beta = [el > 0  for el in nums]
#beta = [ "potential list entry" for " each element" in "a-list-name"]
all(beta) #yeilds false because of -5 in nums
# or we could
print(all([el > 0  for el in nums]))