number = int(input("Enter a number to see its multiplication table:"))
news = [1,2,3,4,5,6,7,8,9,10]
for news in range(1,11):
    x = number
    y = news
    z = number*news
    
    print(f"{x} * {y} = {z}")