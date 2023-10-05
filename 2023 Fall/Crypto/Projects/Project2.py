
from enigma.rotors.rotor import Rotor
from enigma.plugboard import Plugboard
from enigma.machine import EnigmaMachine

def Original_code():

    rL = Rotor('my rotor1', 'EKMFLGDQVZNTOWYHXUSPAIBRCJ', ring_setting=0, stepping='Q')
    rM = Rotor('my rotor2', 'BDFHJLCPRTXVZNYEIWGAKMUSQO', ring_setting=5, stepping='V')
    rR = Rotor('my rotor3', 'ESOVPZJAYQUIRHXLNFTGKDCMWB', ring_setting=10, stepping='J')

    reflector = Rotor('my reflector', 'YRUHQSLDPXNGOKMIEBFZCWVJAT')

    pb = Plugboard.from_key_sheet('AK BZ CG DL FU HJ MX NR OY PW')

    machine = EnigmaMachine([rL, rM, rR], reflector, pb)

    machine.set_display('UPS')       # set rotor positions or use its default
    position = machine.get_display()    # read rotor position
    print(position)

    # Encrypt A letter
    # print(machine.key_press('C'))
    # Encrypt a text
    print(machine.process_text('Enigma machine is powerful for Q'))


def Problem4_1(ciphertext=None):
    # changed Rotor 1 ring_setting from 0 to 22
    rL = Rotor('my rotor1', 'EKMFLGDQVZNTOWYHXUSPAIBRCJ', ring_setting=22, stepping='Q')
    rM = Rotor('my rotor2', 'BDFHJLCPRTXVZNYEIWGAKMUSQO', ring_setting=5, stepping='V')
    rR = Rotor('my rotor3', 'ESOVPZJAYQUIRHXLNFTGKDCMWB', ring_setting=10, stepping='J')

    reflector = Rotor('my reflector', 'YRUHQSLDPXNGOKMIEBFZCWVJAT')

    pb = Plugboard.from_key_sheet('AK BZ CG DL FU HJ MX NR OY PW')

    machine = EnigmaMachine([rL, rM, rR], reflector, pb)

    machine.set_display('UPS')       # set rotor positions or use its default
    position = machine.get_display()    # read rotor position
    print(position)

    # Encrypt A letter
    # print(machine.key_press('C'))
    # Encrypt a text
    if ciphertext !=None:
        print(machine.process_text(ciphertext))
    else: print(machine.process_text('Enigma machine is powerful for Q'))
  

def Problem4_2():

    rL = Rotor('my rotor1', 'EKMFLGDQVZNTOWYHXUSPAIBRCJ', ring_setting=0, stepping='Q')
    # changed Rotor 2 ring_setting from 5 to 19
    rM = Rotor('my rotor2', 'BDFHJLCPRTXVZNYEIWGAKMUSQO', ring_setting=19, stepping='V')
    rR = Rotor('my rotor3', 'ESOVPZJAYQUIRHXLNFTGKDCMWB', ring_setting=10, stepping='J')

    reflector = Rotor('my reflector', 'YRUHQSLDPXNGOKMIEBFZCWVJAT')

    pb = Plugboard.from_key_sheet('AK BZ CG DL FU HJ MX NR OY PW')

    machine = EnigmaMachine([rL, rM, rR], reflector, pb)

    machine.set_display('UPS')       # set rotor positions or use its default
    position = machine.get_display()    # read rotor position
    print(position)

    # Encrypt A letter
    # print(machine.key_press('C'))
    # Encrypt a text
    print(machine.process_text('Enigma machine is powerful for Q'))


def Problem4_3():
    rL = Rotor('my rotor1', 'EKMFLGDQVZNTOWYHXUSPAIBRCJ', ring_setting=0, stepping='Q')
    rM = Rotor('my rotor2', 'BDFHJLCPRTXVZNYEIWGAKMUSQO', ring_setting=5, stepping='V')
    # changed Rotor 3 ring_setting from 10 to 8
    rR = Rotor('my rotor3', 'ESOVPZJAYQUIRHXLNFTGKDCMWB', ring_setting=8, stepping='J')

    reflector = Rotor('my reflector', 'YRUHQSLDPXNGOKMIEBFZCWVJAT')

    pb = Plugboard.from_key_sheet('AK BZ CG DL FU HJ MX NR OY PW')

    machine = EnigmaMachine([rL, rM, rR], reflector, pb)

    machine.set_display('UPS')       # set rotor positions or use its default
    position = machine.get_display()    # read rotor position
    print(position)

    # Encrypt A letter
    # print(machine.key_press('C'))
    # Encrypt a text
    print(machine.process_text('Enigma machine is powerful for Q'))

def Problem4_4():

    # changed Rotor 1 stepping from Q to P
    rL = Rotor('my rotor1', 'EKMFLGDQVZNTOWYHXUSPAIBRCJ', ring_setting=0, stepping='P')
    rM = Rotor('my rotor2', 'BDFHJLCPRTXVZNYEIWGAKMUSQO', ring_setting=5, stepping='V')
    rR = Rotor('my rotor3', 'ESOVPZJAYQUIRHXLNFTGKDCMWB', ring_setting=10, stepping='J')

    reflector = Rotor('my reflector', 'YRUHQSLDPXNGOKMIEBFZCWVJAT')

    pb = Plugboard.from_key_sheet('AK BZ CG DL FU HJ MX NR OY PW')

    machine = EnigmaMachine([rL, rM, rR], reflector, pb)

    machine.set_display('UPS')       # set rotor positions or use its default
    position = machine.get_display()    # read rotor position
    print(position)

    # Encrypt A letter
    # print(machine.key_press('C'))
    # Encrypt a text
    print(machine.process_text('Enigma machine is powerful for Q'))

def Problem4_5():

    rL = Rotor('my rotor1', 'EKMFLGDQVZNTOWYHXUSPAIBRCJ', ring_setting=0, stepping='Q')
    rM = Rotor('my rotor2', 'BDFHJLCPRTXVZNYEIWGAKMUSQO', ring_setting=5, stepping='A')
    rR = Rotor('my rotor3', 'ESOVPZJAYQUIRHXLNFTGKDCMWB', ring_setting=10, stepping='J')

    # Changed Reflector
    reflector = Rotor('my reflector', 'TRUNHQSLDPXIGOKMBFZCWVJAYE')

    pb = Plugboard.from_key_sheet('AK BZ CG DL FU HJ MX NR OY PW')

    machine = EnigmaMachine([rL, rM, rR], reflector, pb)

    machine.set_display('UPS')       # set rotor positions or use its default
    position = machine.get_display()    # read rotor position
    print(position)

    # Encrypt A letter
    # print(machine.key_press('C'))
    # Encrypt a text
    print(machine.process_text('Enigma machine is powerful for Q'))

def Problem4_6():

    rL = Rotor('my rotor1', 'EKMFLGDQVZNTOWYHXUSPAIBRCJ', ring_setting=0, stepping='Q')
    rM = Rotor('my rotor2', 'BDFHJLCPRTXVZNYEIWGAKMUSQO', ring_setting=5, stepping='V')
    # changed Rotor 3 stepping from J to I
    rR = Rotor('my rotor3', 'ESOVPZJAYQUIRHXLNFTGKDCMWB', ring_setting=10, stepping='I')

    reflector = Rotor('my reflector', 'YRUHQSLDPXNGOKMIEBFZCWVJAT')

    pb = Plugboard.from_key_sheet('AK BZ CG DL FU HJ MX NR OY PW')

    machine = EnigmaMachine([rL, rM, rR], reflector, pb)

    machine.set_display('UPS')       # set rotor positions or use its default
    position = machine.get_display()    # read rotor position
    print(position)

    # Encrypt A letter
    # print(machine.key_press('C'))
    # Encrypt a text
    print(machine.process_text('Enigma machine is powerful for Q'))

def Problem4_7():

    rL = Rotor('my rotor1', 'EKMFLGDQVZNTOWYHXUSPAIBRCJ', ring_setting=0, stepping='Q')
    rM = Rotor('my rotor2', 'BDFHJLCPRTXVZNYEIWGAKMUSQO', ring_setting=5, stepping='V')
    rR = Rotor('my rotor3', 'ESOVPZJAYQUIRHXLNFTGKDCMWB', ring_setting=10, stepping='J')

    reflector = Rotor('my reflector', 'YRUHQSLDPXNGOKMIEBFZCWVJAT')
    
    pb = Plugboard.from_key_sheet('AK BZ CG DL FU HJ MX NR OY PW')

    machine = EnigmaMachine([rL, rM, rR], reflector, pb)
    # changed rotor positions
    machine.set_display('PAY')       # set rotor positions or use its default
    position = machine.get_display()    # read rotor position
    print(position)

    # Encrypt A letter
    # print(machine.key_press('C'))
    # Encrypt a text
    print(machine.process_text('Enigma machine is powerful for Q'))

'''-------------------------Problem 5---------------'''
def problem5():
    Problem4_1('KFRZGEDTWEJWHLSFBZEVFRFCBRDLKOTM')


def prob6_helper(r1,):

    rL = Rotor('my rotor1', 'EKMFLGDQVZNTOWYHXUSPAIBRCJ', ring_setting=0, stepping='Q')
    rM = Rotor('my rotor2', 'BDFHJLCPRTXVZNYEIWGAKMUSQO', ring_setting=5, stepping='V')
    rR = Rotor('my rotor3', 'ESOVPZJAYQUIRHXLNFTGKDCMWB', ring_setting=10, stepping='J')

    reflector = Rotor('my reflector', 'YRUHQSLDPXNGOKMIEBFZCWVJAT')

    pb = Plugboard.from_key_sheet('AK BZ CG DL FU HJ MX NR OY PW')

    machine = EnigmaMachine([rL, rM, rR], reflector, pb)

    machine.set_display('UPS')       # set rotor positions or use its default
    position = machine.get_display()    # read rotor position
    print(position)

    # Encrypt A letter
    # print(machine.key_press('C'))
    # Encrypt a text
    print(machine.process_text('Enigma machine is powerful for Q'))

def problem6():
    nums = ['0','1','2','3','4','5','6','7','8','9']
    ciphertext = 'WVUVJCSQBFLWSGTHDREWOSXYIAYEUBHHXY'
    known_p = 'ATTACK AT 5PM AT ATLANTIC Z ISLAND'
    new_known_p = []

    for item in known_p:
        if item == ' ':
            new_known_p.append('X')
        elif item in nums:
            new_known_p.append('X')
        else: new_known_p.append(item)

    new_known_p = "".join(new_known_p)





#Problem4_1()
#Problem4_2()
#Problem4_3()
#Problem4_4()
#Problem4_5()
#Problem4_6()
#Problem4_7()
#problem5()
problem6()



