def a():
    print("Answer all questions with 'yes' or 'no'")
    q1 = input("Does it have canines: ").lower()
    if q1 == ("no"):
        q2 = input("Does it have feathers: ").lower()
        if q2 == ("yes"):
            print("Your dinosawr is Cantremember")
        elif q2 == ("no"):
            print("Your dinosawr is Oviraptor")
        else:
            print("Invallid entry!")
    elif q1 == ("yes"):
        q3 = input("Is it roadent like: ").lower()
        if q3 == ("yes"):
            print("Your dinosawr is Heterodontosaurus")
        elif q3 == ("no"):
            print("Your dinosawr is Therizinosaur")
        else:
            print("Invallid entry!")
    else:
        print("Invallid entry!")
a()