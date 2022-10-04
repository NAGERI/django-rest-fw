def solution(x): # foobar.withgoogle.com
    # Your code here    
    asci_u = 97    # a 96+13 = midpoint
    asci_mid = 110 # n
    asci_l = 122   # z  midpoint + 13 = 122
    bigger = []
    biggest = []
    accurate_char = 0
    list_str =  x.split()
    for string in list_str:
        one = string.split()
        rev_word = []
        
        for on in one[0]:
            # print(ord(on))
            n_fmt = ord(on)
            if asci_u > n_fmt < asci_l:
                print(on)
                rev_word.append(on)
                continue
            else:
                # add difference from 97 or 122 midpoint 109 ord/ord
                if n_fmt <= asci_mid:
                    accurate_char = (asci_l - (n_fmt - asci_u))
                    # print(accurate_char)
                elif n_fmt >= asci_mid:
                    accurate_char = (asci_u + (asci_l - n_fmt))
                    # print(accurate_char)
                else:
                    print(on)
                    # accurate_char = n_fmt
                rev_word.append(chr(accurate_char))
        bigger.append("".join(rev_word))
    biggest.append(" ".join(bigger))
    return "".join(biggest)
    '''
    You've caught two of your fellow minions passing coded notes back and forth -- while they're on duty, no less! Worse, you're pretty sure it's not job-related -- they're both huge fans of the space soap opera ""Lance & Janice"". You know how much Commander Lambda hates waste, so if you can prove that these minions are wasting time passing non-job-related notes, it'll put you that much closer to a promotion. 

    Fortunately for you, the minions aren't exactly advanced cryptographers. In their code, every lowercase letter [a..z] is replaced with the corresponding one in [z..a], while every other character (including uppercase letters and punctuation) is left untouched.  That is, 'a' becomes 'z', 'b' becomes 'y', 'c' becomes 'x', etc.  For instance, the word ""vmxibkgrlm"", when decoded, would become ""encryption"".

    Write a function called solution(s) which takes in a string and returns the deciphered string so you can show the commander proof that these minions are talking about ""Lance & Janice"" instead of doing their jobs.

    def solution(x):
    asci_u = 97    # a
    asci_mid = 110 # n
    asci_l = 122   # z
    bigger = []
    biggest = []
    accurate_char = 0
    list_str =  x.split()
    for string in list_str:
        one = string.split()
        rev_word = []
        
        for on in one[0]:
            n_fmt = ord(on)
            if asci_u > n_fmt < asci_l:
                rev_word.append(on)
                continue
            else:
                if n_fmt <= asci_mid:
                    accurate_char = (asci_l - (n_fmt - asci_u))
                elif n_fmt >= asci_mid:
                    accurate_char = (asci_u + (asci_l - n_fmt))
                else:
                    print(on)
                rev_word.append(chr(accurate_char))
        bigger.append("".join(rev_word))
    biggest.append(" ".join(bigger))
    return "".join(biggest)
    '''