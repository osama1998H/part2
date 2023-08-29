
def new_seq(n):
    if n in [1, 2, 3, 4]:
        return 1
    return new_seq(n-1) + new_seq(n-2) + new_seq(n-3) + new_seq(n-4)


if __name__ == "__main__":
    print(new_seq(10))
