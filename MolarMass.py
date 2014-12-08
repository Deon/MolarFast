__author__ = 'Deon Hua and Timothy Mui'

elementDict = {"H":1.0079,"He":4.0026,"Li":6.941,"Be":9.0122,"B":10.811,"C":12.0107,"N":14.0067,"O":15.9994,\
               "F":18.9984,"Ne":20.1797,"Na":22.9897,"Mg":24.305,"Al":26.9815,"Si":28.0855,"P":30.9738,"S":32.065,\
               "Cl":35.453,"Ar":39.948,"K":39.0983,"Ca":40.078,"Sc":44.9559,"Ti":47.867,"V":50.9415,"Cr":51.9961,\
               "Mn":54.938,"Fe":55.845,"Co":58.9332,"Ni":58.6934,"Cu":63.546,"Zn":65.39,"Ga":69.723,"Ge":72.64,\
               "As":74.9216,"Se":78.96,"Br":79.904,"Kr":83.8,"Rb":85.4678,"Sr":87.62,"Y":88.9059,"Zr":91.224,\
               "Nb":92.9064,"Mo":95.94,"Tc":98,"Ru":101.07,"Rh":102.9055,"Pd":106.42,"Ag":107.8682,"Cd":112.411,\
               "In":114.818,"Sn":118.71,"Sb":121.76,"Te":127.6,"I":126.9045,"Xe":131.293,"Cs":132.9055,"Ba":137.327,\
               "La":138.9055,"Ce":140.116,"Pr":140.9077,"Nd":144.24,"Pm":145,"Sm":150.36,"Eu":151.964,"Gd":157.25,\
               "Tb":158.9253,"Dy":162.5,"Ho":164.9303,"Er":167.259,"Tm":168.9342,"Yb":173.04,"Lu":174.967,"Hf":178.49,\
               "Ta":180.9479,"W":183.84,"Re":186.207,"Os":190.23,"Ir":192.217,"Pt":195.078,"Au":196.9665,"Hg":200.59,\
               "Tl":204.3833,"Pb":207.2,"Bi":208.9804,"Po":209,"At":210,"Rn":222,"Fr":223,"Ra":226,"Ac":227,\
               "Th":232.0381,"Pa":231.0359,"U":238.0289,"Np":237,"Pu":244,"Am":243,"Cm":247,"Bk":247,"Cf":251,\
               "Es":252,"Fm":257,"Md":258,"No":259,"Lr":262,"Rf":261,"Db":262,"Sg":266,"Bh":264,"Hs":277,"Mt":268}


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
