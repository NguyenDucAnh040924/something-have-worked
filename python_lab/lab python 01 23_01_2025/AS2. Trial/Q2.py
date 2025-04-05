"""
Write a program that uses the random function to make the computer guess the number you think it is. For example, if you think in the beginning of
the number 68, the computer will first guess 15, you enter the answer as l (low), then machine continue to guess 87, you will enter h (high), the
computer will try again. Continue guessing. And so on until the machine guesses the number you think in your head is 68, then you enter c
(correct). The program will notify the the machine guessed correctly and exit

"""


import random

ket_qua = int(input("Enter answer: "))
guessed_number = int(input("Enter a range for guessed number: "))
while guessed_number < 1:
    guessed_number = int(input("Enter a range for guessed number: "))

def out(v,ket_qua_may_tinh):
    print(f"Is  {v} too high(h), too low(l), or correct(c): {ket_qua_may_tinh}")


# Danh sách để lưu trữ các số đã đoán
guessed_numbers = set()

while True:

    # Máy tính chọn số ngẫu nhiên, tránh các số đã đoán
    while True:
        may_tinh = random.randint(1,guessed_number)
        if may_tinh not in guessed_numbers:
            guessed_numbers.add(may_tinh)
            break

    if may_tinh < ket_qua: 
        out(may_tinh,"l")
    elif may_tinh > ket_qua:
        out(may_tinh,"h")
    else:
        out(may_tinh,"c")
        print(f"Welldone! The computer guessed your number {ket_qua} correctly!")
        print("FINISH")
        break



