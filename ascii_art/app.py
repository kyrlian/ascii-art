
def print_unicode_range(u_start, u_end, c_sep="", c_end="\n"):
    """
    Prints the Unicode characters between start and end.
    """
    for i in range(u_start, u_end):
        print(chr(i),end=c_sep)
    print(c_end)

def print_monograms(c_sep):
    """ 
    print all yijing monograms unicode characters
    """
    print_unicode_range(0x268A, 0x268F,c_sep)

def print_trigrams(c_sep):
    """ 
    print all yijing trigrams unicode characters
    """
    print_unicode_range(0x2630, 0x2637,c_sep)

def print_hexagrams(c_sep):
    """ 
    print all yijing hexagrams unicode characters
    """
    print_unicode_range(0x4dc0, 0x4dff,c_sep)

def main():
    print_monograms(" ")
    print_trigrams(" ")
    print_hexagrams(" ")

    

if __name__ == "__main__":
    main()
