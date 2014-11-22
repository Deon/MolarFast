import MolarMass

def main ():
    result = MolarMass.get_molar_mass(raw_input("Please enter chemical formula "))

    if result:
        print "%.2f g/mol"%result
    else:
        print "Error in Formula"

main ()
