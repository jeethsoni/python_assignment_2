"""
A python script to construct a dictionary of some of the world's
finest cuisines and store it in json document (prettified)

@usage python3 cuisines.py
"""
import json


def main():
    # empty cuisine dictionary
    cuisine_dict = {}

    # values of the cuisines
    cuisines = ["mexican", "italian", "thai"]
    mexican = ["enchiladas", "burrito", "tacos al pastor", "elote", "tamales"]
    italian = ["Risotto", "Pizza", "Pasta", "Lasagne", "Gelato"]
    thai = ["Pad Thai", "Tom Yum Goong ", "Kaeng Lueang", "Gaeng Daeng", "Gaeng Keow Wan Gai "]  # noqa

    # loop through every item in cuisines and if matches add to the dictionary
    for cuisine in range(len(cuisines)):
        if (cuisines[cuisine] == "mexican"):
            cuisine_dict[cuisines[cuisine]] = mexican
        elif (cuisines[cuisine] == "italian"):
            cuisine_dict[cuisines[cuisine]] = italian
        else:
            cuisine_dict[cuisines[cuisine]] = thai

    # open the json file and dump the dictionary
    with open("cuisines.json", "w") as wf:
        json.dump(cuisine_dict, wf, indent=4)


if __name__ == "__main__":
    main()
