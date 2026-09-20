from colorama import Fore
import matplotlib.pyplot as plt
import time
aylar=[]
paralar=[]
plt.xlabel=("months")
plt.ylabel=("money")
plt.title=("Annual money change")

time.sleep(0.7)

print(Fore.CYAN+"The purpose of the program is to see how much money you will have after 1 year ")

time.sleep(0.8)
print("It will go as 1 2 3 4... and so on. Please wait...")

time.sleep(0.8)
print(Fore.RED+"-"*50)
#QUESTIONS
time.sleep(0.8)
mevcut_bara=int(input(Fore.BLUE+"Enter how much money you currently have saved up..(NUMERICAL)"))

time.sleep(0.8)
print(Fore.RED+"-"*50)

time.sleep(0.7)
aylik_gelir=int(input(Fore.BLUE+"Enter your monthly income...(numerical)"))

time.sleep(0.7)
print(Fore.RED+"-"*50)

time.sleep(0.7)
aylik_getiri=int(input(Fore.BLUE+"What is your monthly return?(percentage)"))
#MACHINE
print("Calculating...")
time.sleep(2)
ay=1
while ay<=12:
    mevcut_bara+=aylik_gelir
    mevcut_bara+=mevcut_bara*(aylik_getiri/100)

    aylar.append(ay)
    paralar.append(mevcut_bara)
    ay += 1

plt.plot(aylar,paralar)
plt.show()