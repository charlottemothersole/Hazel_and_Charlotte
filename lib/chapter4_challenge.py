def get_most_common_letter(text):
    counter = {}
    new_text = text.replace(' ','')
    for char in new_text:
        print('char',char)
        counter[char] = counter.get(char, 0) + 1
        print('counter[char]',counter[char])
    letter = sorted(counter.items(), key=lambda item: item[1])[-1][0]
    # list=[[0,1],2,3]
    # list[0]
    # t: 1
    # print('letter',letter)
    return letter
    print('counter',counter)

    # counter = {}
    # for char in text:
    #     counter[char] = counter.get(char, 0) + 1
    # letter = sorted(counter.items(), key=lambda item: item[1])[0][1]
    # return letter
    


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")