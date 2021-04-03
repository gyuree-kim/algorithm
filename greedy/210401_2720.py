quarter = 0 #25
dime = 0    #10
nickel = 0  #5
penny = 0   #1

n = input()
amounts =[]
for i in range(int(n)):
    amount = int(input())
    amounts.append(amount)

for amount in amounts:
    while amount != 0 :
        quarter = amount//25
        amount = amount%25
        dime = amount//10
        amount %= 10
        nickel = amount//5
        amount %= 5
        penny = amount
        amount -= penny
    print(f"{quarter} {dime} {nickel} {penny}")
