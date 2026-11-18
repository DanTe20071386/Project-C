from random_word import RandomWords

r = RandomWords()
rand = r.get_random_word()


def hang():
    guess_let = []
    mistakes = len(rand)
    empty = ["_"] * len(rand)
    print("This is hangman game"), print(
        f"\nthe secret word has {len(rand)} letters and you can {mistakes} mistakes"
    )
    while mistakes > 0 and "_" in empty:
        print("============================")
        print("\n", end="")
        for let in empty:
            print(let, end="")
        print()
        print(f"\nmistakes remaining is {mistakes}")
        print("\nguess let :", end="")
        for i, let in enumerate(guess_let):
            if i < len(guess_let) - 1:
                print(let + ",", end="")
            else:
                print(let, end="")
        print()
        guess = input("\nenter a let : ").lower()
        if len(guess) != 1:
            print("\nenter a one let!!!")
            continue
        if guess in guess_let:
            print("\nthis let you choose before")
            continue
        guess_let.append(guess)
        if guess in rand:
            print("\ncorrect letter add!!!")
            for i, let in enumerate(rand):
                if let == guess:
                    empty[i] = guess
        else:
            print("\nthis let is wrong")
            mistakes -= 1
    if "_" not in empty:
        print("\nyou are win!!! and save the man :)")
        print("\nrand word was : ", end="")
        for let in empty:
            print(let, end="")
        print()
    else:
        print("\nyou are lose!!! and kill the man :("), print(
            f"\ntrue rand word was = {rand}"
        )


hang()
