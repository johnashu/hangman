
count = 0

while count < 10:
    in_text = input("type something:").upper()
    print(in_text)

    if in_text == 'Y':
        print('yes')
        count += 1
    else:
        print('no')
        count += 1
