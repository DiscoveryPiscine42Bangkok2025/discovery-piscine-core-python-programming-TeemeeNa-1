from checkmate import checkmate

def main():
    print("Enter your board (empty line to finish):")

    rows = []
    while True:
        line = input()
        if line == "":
            break
        rows.append(line)

    board = "\n".join(rows)
    checkmate(board)

if __name__ == "__main__":
    main()