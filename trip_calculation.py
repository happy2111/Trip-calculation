# "Этот код запрашивает у пользователя баланс, расстояние, стоимость поездки на такси и автобусе, а также количество автобусных 
# поездок. Затем программа рассчитывает, хватит ли денег на поездку на такси или автобусе, и выводит соответствующие сообщения."

# This code asks the user for the balance, distance, cost of the taxi and bus ride, and the number of bus rides. The program then
#    calculates whether there is enough money for the taxi or bus ride and displays the appropriate messages.


balance = int(input("Enter your balance: "))
distance = int(input("Enter distance in km: "))
taxi = int(input("Enter how much by taxi: "))
bus = int(input("Enter how much by bus: "))
howMany = int(input("How many bus: "))


taxi_overal = distance * taxi
bus_overal = bus * howMany


match = taxi_overal < balance
match2 = bus_overal < balance

if(match == True):
    say1 = "Bemalol Ketovir, Oq yo'l"
elif(match == False):
    say1 = "Pul topib kegin"


if(match2 == True):
    say2 = "Bemalol Ketovir, Oq yo'l"
elif(match2 == False):
    say2 = "Pul topib kegin"


print(f"\n\n\n********************************\nYour balance: {balance}\nDistance: {distance}\nBy taxi: {taxi_overal}\nBy bus: {bus_overal}\nHow many bus: {howMany}\n\n\nBy bus: {say2}\nBy taxi:{say1}\n\n********************************")

