###
#
# e2-uniqueiptv
# Generator unikalnych wartości SID
#
###

import random

# wartości domyślne
input_f = f''
player = 4097

class WrongValue(Exception):
    pass

# funkcja generująca plik z unikalnymi wartościami SID
def uniqueiptv(ifile, p):
    try:
        infile = open(f'{ifile}', 'r').read().split('\n')
        oufile = open(f'new_{ifile}', 'w')
        for line in infile:
            if "#DESCRIPTION" in line or "#NAME" in line:
                oufile.write(f'{line}\n')
            if "#SERVICE" in line and ("4097" in line or "5001" in line or "5002" in line):
                val = random.randint(1,60000)
                ch = line.split(':')
                oufile.write(f'#SERVICE {p}:{ch[1]}:{ch[2]}:{hex(val)[2:]}:{ch[4]}:{ch[5]}:{ch[6]}:{ch[7]}:{ch[8]}:{ch[9]}:{ch[10]}:{ch[11]}\n')
        oufile.close()
        return(f'Done')
    except FileNotFoundError as e:
        raise WrongValue(f'Nieprawidłowa nazwa pliku!\n{str(e)}')

# main
if __name__ == "__main__":
    try:
        input_f = input("Podaj nazwę pliku z rozszerzeniem .tv: ")
        if input_f == '':
            raise WrongValue(f'Nie podano nazwy pliku!')
        print(f'Wybierz domyślny player:')
        print(f'1. GStreamer - id 4097')
        print(f'2. exteplayer3 - id 5002')
        ch_plr = input(f'Twój wybór: ')
        match ch_plr:
            case "1":
                print("Wybrano GStreamer - id 4097")
                player = 4097
            case "2":
                print("Wybrano exteplayer3 - id 5002")
                player = 5002
            case _:
                raise WrongValue(f'Nieprawidłowa wartość!')
        print(uniqueiptv(input_f, player))
    except WrongValue as e:
        print(f'Błąd: {str(e)}')
    except Exception as e:
        print(f'{str(e)}')
