def main(n,total=0):
    if n == 0: return total
    else:
        total *= n
        return sum(n-1, total)

if __name__ == "__main__":
    main()