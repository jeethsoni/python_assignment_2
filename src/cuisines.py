from pprint import pprint


def main():
    cuisine_dict = {}
    cuisines = ["mexican", "italian", "thai"]
    mexican = ["enchiladas", "burrito", "tacos al pastor", "elote", "tamales"]
    italian = ["Risotto", "Pizza", "Pasta", "Lasagne", "Gelato"]
    thai = ["Pad Thai", "Tom Yum Goong ", "Kaeng Lueang", "Gaeng Daeng", "Gaeng Keow Wan Gai "]  # noqa

    for cuisine in range(len(cuisines)):
        if (cuisines[cuisine] == "mexican"):
            cuisine_dict[cuisines[cuisine]] = mexican
        elif (cuisines[cuisine] == "italian"):
            cuisine_dict[cuisines[cuisine]] = italian
        else:
            cuisine_dict[cuisines[cuisine]] = thai

    pprint(cuisine_dict, width=50, indent=2, sort_dicts=False) 


if __name__ == "__main__":
    main()
