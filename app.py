def kuku(max_dan):
    for i in range(1, max_dan + 1):
        for j in range(1, 10):
            print(
                f"{i} × {j} = {i*j}",
            )


print()

max_dan = int(input("何段までの九九を表示しますか："))
kuku(max_dan)
