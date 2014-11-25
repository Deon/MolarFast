import MolarMass


def main():
    userin = True
    while userin:
        userin = input("Please enter chemical formula ")
        result = MolarMass.get_molar_mass(userin)

        if result:
            print("%.2f g/mol" % result)
        else:
            print("Error in Formula")

main()
