# Initial data: polygon string followed by number of sides
data = [
    "Triangle",
    3,
    "Square",
    4,
    "Pentagon",
    5,
    "Hexagon",
    6,
    "Heptagon",
    7,
    "Octagon",
    8,
    "Nonagon",
    9,
    "Decagon",
    10,
    "Dodecagon",
    12,
    "Icosagon",
    20,
]

# The blacklist to remove
blacklist = ["Triangle", "Heptagon", "Dodecagon"]


def cleanse_and_reorder(data_list, blacklist):
    """Function which mutates the data_list in place to meet the desired requirements."""


if __name__ == "__main__":
    id_init = id(data)
    cleanse_and_reorder(data, blacklist)
    id_after = id(data)

    assert id_init == id_after
    assert data == [
        "Square",
        "Pentagon",
        "Hexagon",
        "Octogon",
        "Nonagon",
        "Decagon",
        "Icosagon",
        4,
        5,
        6,
        8,
        9,
        10,
        20,
    ]
