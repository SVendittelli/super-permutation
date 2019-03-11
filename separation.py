def main():
    # Read a text file containing the superpermutation
    checkFile("n=7 5906.txt")


def checkFile(file_name: str):
    """Read a given file and check the symbol separation of superpermutation within.

    Parameters
    ----------
    file_name : str
        The file name of the superpermutation to check the symbol separtion of
    """
    superperm = open(file_name, "r").read()
    print("Length:", len(superperm))
    symbolSepartion(superperm)


def symbolSepartion(superperm: str) -> None:
    """Check a given superpermutation with length n for the separation of all of each of it's symbols.

    Parameters
    ----------
    superperm : str
        The superpermutation to check the symbol separtion of
    """

    # Obtain a list of all the symbols used in the superpermutation
    symbols = list(set(superperm))
    symbols.sort()

    for symbol in symbols:
        # For each symbol, construct an array of the indices of them in the superpermutation
        indices = [i + 1 for i, char in enumerate(superperm) if char == symbol]

        count = len(indices)
        if (count == 1):
            print("symbol: {0}    count: {1}".format(symbol, count))
            # print("symbol:", symbol, "    count:", count)
            continue
        else:
            # Set the minimum and maximum separations to be impossible values
            min_sep = len(superperm) + 1
            max_sep = -1

        # Iterative over all the indices in sequential pairs and check the distance between them
        for a, b in zip(indices[:-1], indices[1:]):
            difference = b - a
            if difference < min_sep:
                min_loc = a
            if difference > max_sep:
                max_loc = a
            min_sep = min(min_sep, b - a)
            max_sep = max(max_sep, b - a)

        # Print the results
        print("symbol: {0}    count: {1} min: {2} at position {3} max: {4} at position {5}".format(
            symbol, str(count).ljust(6), min_sep, str(min_loc).ljust(6), max_sep, max_loc))


if __name__ == "__main__":
    main()
