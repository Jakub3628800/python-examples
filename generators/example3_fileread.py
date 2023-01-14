"""
File object in python can be iterated trough, because it acts a generator
of lines from the file! The following is a demonstration where we look for
a specific line in a file.
"""


def find_line_in_file(filename: str, match: str) -> bool:
    """Match a line in file."""
    f = open(filename, "r")

    for line in f:
        if line.strip("\n") == match:
            print("found it!")
            f.close()
            return True

    f.close()
    return False


found = find_line_in_file(filename="longfile.txt", match="ten")
print(found)
