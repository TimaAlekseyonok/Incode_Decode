class Roter:
    def __init__(self, position1, position2, position3):
        self.position1 = position1
        self.position2 = position2
        self.position3 = position3

    def true_position(self):
        return self.position1 + self.position2 + self.position3

    def smena_rotera(self):
        self.position1 += 1
        if self.position1 > 26:
            self.position1 -= 26
            self.position2 += 1
            if self.position2 > 26:
                self.position2 -= 26
                self.position3 += 1
                if self.position3 > 26:
                    self.position3 -= 26
        # print(f'The rotors were switched, now the positions of the rotors are as follows: {self.position1}, {self.position2}, {self.position3}')


while True:
    try:
        position_roter1 = int(input('Input rotor 1 position (1-26): '))
        if position_roter1 < 1 or position_roter1 > 26:
            print('Position must be between 1 and 26.')
        else:
            break
    except ValueError:
        print('Please input an integer.')

while True:
    try:
        position_roter2 = int(input('Inpup roter 2 position (1-26): '))
        if position_roter2 < 1 or position_roter2 > 26:
            print('Position must be between 1 and 26.')
        else:
            break
    except ValueError:
        print('Please input an integer.')

while True:
    try:
        position_roter3 = int(input('Inpup roter 3 position (1-26): '))
        if position_roter3 < 1 or position_roter3 > 26:
            print('Position must be between 1 and 26.')
        else:
            break
    except ValueError:
        print('Please input an integer.')

roters = Roter(position_roter1, position_roter2, position_roter3)

while True:
    try:
        what_do_you_want = input('Encode or Decode: ')
        if what_do_you_want.upper() == 'ENCODE' or what_do_you_want.upper() == 'EN':
            message = input('Input message: ')
            encode_massage = []

            for symbol in message:
                if symbol == ' ':
                    encode_massage.append(symbol)
                    roters.smena_rotera()
                else:
                    encode = (ord(symbol.upper()) - 65 + roters.true_position()) % 26 + 65
                    encode_massage.append(chr(encode))
                    roters.smena_rotera()

            print(''.join(encode_massage))
            break

        elif what_do_you_want.upper() == 'DECODE' or what_do_you_want.upper() == 'DE':
            decode = input('Decode: ')
            decode_massage = []

            for de_symbol in decode:
                if de_symbol == ' ':
                    decode_massage.append(de_symbol)
                    roters.smena_rotera()
                else:
                    de_code = (ord(de_symbol.upper()) + 65 - roters.true_position()) % 26 + 65
                    decode_massage.append(chr(de_code))
                    roters.smena_rotera()
            print(''.join(decode_massage))
            break
        else:
            print('You should choose what you want to Encode or Decode')
    except:
        break