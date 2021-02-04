

def is_unique(s):
    for i in range(0,len(s)-1):
        for j in range(i+1,len(s)):
            if s[i] == s[j]:
                return False
    return True
        


def main():
    print(is_unique("asdff"))



if __name__ == "__main__":
    main()
