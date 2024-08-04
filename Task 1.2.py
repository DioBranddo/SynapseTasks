gadgets = [
    ("Explosive batarangs", 3, True),
    ("Batarangs", 5, True),
    ("Smoke Pellets", 2, True),
    ("Batclaw", 0, False),
    ("Grapple gun", 3, True),
    ("Batsignal", 3, True)
]


def sortGadgets():
    return sorted(gadgets, key= lambda gadget: (-gadget[1], gadget[0]))


def main():
    sortedGadgets = sortGadgets()
    for gadget in sortedGadgets:
        print(f"{gadget[0]}\t{gadget[1]}")


if __name__=='__main__':
    main()