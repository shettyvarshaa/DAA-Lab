def knapSack(W, wt, val, n): 
    if n == 0 or W == 0: 
        return 0     
    if wt[n - 1] > W: 
        return knapSack(W, wt, val, n - 1)     
    return max(val[n - 1] + knapSack(W - wt[n - 1], wt, val, n - 1), knapSack(W, wt, val, n - 1)) 

profit = [130, 100, 120] 
weight = [10, 20, 30] 
print("Profit = ", profit)
print(f"Weight = {weight}")

n = len(profit) 
W = 50 
print(f"Knapsack Capacity = {W}")
print("Maximum Profit =",knapSack(W, weight, profit, n)) 	 

#OUTPUT
'''
    Profit =  [130, 100, 120]
    Weight = [10, 20, 30]
    Knapsack Capacity = 50
    Maximum Profit = 250
'''