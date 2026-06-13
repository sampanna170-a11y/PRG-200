import random

random.seed(42)

friends = ["Ramesh", "Sunita", "Bikash", "Anjali", "Dipak"]
total_bill = 3750

def split_bill(friends, total):
    return total / len(friends)

def pick_lucky(friends):
    return random.choice(friends)

def final_summary(friends, total):
    share = split_bill(friends, total)
    lucky_person = pick_lucky(friends)

    print("Bill Split Summary")
    print()

    for person in friends:
        print(person, "pays NPR", share)

    lucky_total = share + 50

    print()
    print("Lucky Person:", lucky_person)
    print(lucky_person, "pays NPR", lucky_total)

final_summary(friends, total_bill)