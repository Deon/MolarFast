__author__ = 'Deon Hua and Timothy Mui'

#Data obtained from NIST
elementDict = {"H": 1.00794000, "He": 4.00260200, "Li": 6.94100000, "Be": 9.01218200, "B": 10.81100000, "C": 12.01070000, "N": 14.00670000, "O": 15.99940000, "F": 18.99840320, "Ne": 20.17970000, "Na": 22.98976928, "Mg": 24.30500000, "Al": 26.98153860, "Si": 28.08550000, "P": 30.97376200, "S": 32.06500000, "Cl": 35.45300000, "Ar": 39.94800000, "K": 39.09830000, "Ca": 40.07800000, "Sc": 44.95591200, "Ti": 47.86700000, "V": 50.94150000, "Cr": 51.99610000, "Mn": 54.93804500, "Fe": 55.84500000, "Co": 58.93319500, "Ni": 58.69340000, "Cu": 63.54600000, "Zn": 65.38000000, "Ga": 69.72300000, "Ge": 72.64000000, "As": 74.92160000, "Se": 78.96000000, "Br": 79.90400000, "Kr": 83.79800000, "Rb": 85.46780000, "Sr": 87.62000000, "Y": 88.90585000, "Zr": 91.22400000, "Nb": 92.90638000, "Mo": 95.96000000, "Tc": 98.00000000, "Ru": 101.07000000, "Rh": 102.90550000, "Pd": 106.42000000, "Ag": 107.86820000, "Cd": 112.41100000, "In": 114.81800000, "Sn": 118.71000000, "Sb": 121.76000000, "Te": 127.60000000, "I": 126.90447000, "Xe": 131.29300000, "Cs": 132.90545190, "Ba": 137.32700000, "La": 138.90547000, "Ce": 140.11600000, "Pr": 140.90765000, "Nd": 144.24200000, "Pm": 145.00000000, "Sm": 150.36000000, "Eu": 151.96400000, "Gd": 157.25000000, "Tb": 158.92535000, "Dy": 162.50000000, "Ho": 164.93032000, "Er": 167.25900000, "Tm": 168.93421000, "Yb": 173.05400000, "Lu": 174.96680000, "Hf": 178.49000000, "Ta": 180.94788000, "W": 183.84000000, "Re": 186.20700000, "Os": 190.23000000, "Ir": 192.21700000, "Pt": 195.08400000, "Au": 196.96656900, "Hg": 200.59000000, "Tl": 204.38330000, "Pb": 207.20000000, "Bi": 208.98040000, "Po": 209.00000000, "At": 210.00000000, "Rn": 222.00000000, "Fr": 223.00000000, "Ra": 226.00000000, "Ac": 227.00000000, "Th": 232.03806000, "Pa": 231.03588000, "U": 238.02891000, "Np": 237.00000000, "Pu": 244.00000000, "Am": 243.00000000, "Cm": 247.00000000, "Bk": 247.00000000, "Cf": 251.00000000, "Es": 252.00000000, "Fm": 257.00000000, "Md": 258.00000000, "No": 259.00000000, "Lr": 262.00000000, "Rf": 265.00000000, "Db": 268.00000000, "Sg": 271.00000000, "Bh": 272.00000000, "Hs": 270.00000000, "Mt": 276.00000000, "Ds": 281.00000000, "Rg": 280.00000000, "Cn": 285.00000000}

def get_molar_mass(raw_formula):
    if check_formula(raw_formula):
        return calculate_molar(parse_formula(raw_formula))
    else:
        return None


def check_formula(raw_formula):
    elements = parse_formula(raw_formula)
    for x in elements:
        try:
            elementDict[x[0]]
        except KeyError:
            return False
    return True


def parse_formula(raw_formula):
    raw_formula = "".join(raw_formula.split())

    if raw_formula and bracket_check(raw_formula):
        formula = []
        elements = []
        x = 0

        #Checker for the first char
        if raw_formula[x].isdigit():  # Digit
            number = raw_formula[x]

            while x+1 < len(raw_formula) and raw_formula[x+1].isdigit():
                x += 1
                number += raw_formula[x]

            x_formula = int(number)

        elif raw_formula[x].isalpha():  # Letter
            formula += raw_formula[x]
            x_formula = 1
        elif raw_formula[x] == "(":  # Open Bracket
            x_formula = 1
        else:  # Anything else
            return [["!", 0]]

        x += 1

        while x < len(raw_formula):  # Goes through each character of raw_formula (except for ones covered already)
            if raw_formula[x] == "(":
                if formula:
                    elements.extend(parse_elements(formula, x_formula))
                    formula = []

            elif raw_formula [x] == ")":
                if x+1 < len(raw_formula) and raw_formula[x+1].isdigit():
                    x += 1
                    number = raw_formula[x]

                    while x+1 < len(raw_formula) and raw_formula[x+1].isdigit():
                        x += 1
                        number += raw_formula[x]

                    x_subformula = int(number)
                else:
                    x_subformula = 1

                elements.extend(parse_elements(formula, x_formula*x_subformula))
                formula = []

            elif raw_formula[x] == "*":
                elements.extend(parse_elements(formula, x_formula))
                formula = []

                if x+1 < len(raw_formula) and raw_formula[x+1].isdigit():
                    x += 1
                    number = raw_formula[x]

                    while x+1 < len(raw_formula) and raw_formula[x+1].isdigit():
                        x += 1
                        number += raw_formula [x]

                    x_formula = int(number)

                else:
                    x_formula = 1

            elif raw_formula[x].isalpha() or raw_formula[x].isdigit():
                formula += raw_formula[x]

            else:
                return [["!", 0]]

            x += 1

        if formula:
            elements.extend(parse_elements(formula, x_formula))

        return elements
    else:
        return [["!", 0]]

'''
Called by parse_formula to return arrays of element names and their multiplier.
'''

def parse_elements (formula, x_formula):
    elements = []
    element = ""
    multiplier = 1
    x = 0

    while x < len(formula):
        if formula[x].isupper():  # Capital Letter
            if element:
                elements.append([element,multiplier*x_formula])
                multiplier = 1

            element = formula[x]

        elif element and formula[x].islower():  # Lower Case
            try:  # Must be uppercase letter before lowercase letter
                if formula[x-1].isupper():
                    element += formula[x]
                else:
                    return [["!",0]]
            except IndexError:
                return [["!",0]]

        elif formula[x].isdigit(): #Digit
            number = formula[x]

            while x+1 < len(formula) and formula[x+1].isdigit():
                x += 1
                number += formula [x]

            multiplier = int(number)

        else:
            return [["!",0]]
        x += 1
    elements.append([element,multiplier*x_formula])

    return elements


def calculate_molar(elements):
    mass = 0
    for x in elements:
        mass += elementDict[x[0]]*x[1]

    return mass


def bracket_check(input_string):
    brackets = []

    for x in input_string:
        if x == "(":
            brackets.extend(x)

        elif x == ")":
            if len(brackets) == 0:
                return False
            elif brackets.pop() == "(":
                continue
            else:
                return False

    if len(brackets) == 0:
        return True
    else:
        return False
