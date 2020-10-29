#Based on 1395
cities = {
    "Tehran": 13267637,
    "Razavi Khorasan": 6434501,
    "Isfahan": 5120850,
    "Fars": 4851274,
    "Khuzestan": 4710509,
    "East Azerbaijan": 3909652,
    "Mazandaran": 3283582,
    "West Azerbaijan": 3265219,
    "Kerman": 3163718,
    "Sistan and Baluchestan": 2775014,
    "Alborz": 2712400,
    "Gilan": 2530696,
    "Kermanshah": 1952434,
    "Golestan": 1868619,
    "Hormozgan": 1776415,
    "Lorestan": 1760649,
    "Hamadan": 1758268,
    "Kurdistan": 1603011,
    "Markazi": 1429475,
    "Qom": 1292283,
    "Qazvin": 1273761,
    "Ardabil": 1270420,
    "Bushehr": 1163400,
    "Yazd": 1138533,
    "Zanjan": 1057461,
    "Chaharmahal and Bakhtiari": 947763,
    "North Khorasan": 863092,
    "South Khorasan": 768898,
    "Kohgiluyeh and Boyer-Ahmad": 713052,
    "Semnan": 702360,
    "Ilam": 580158
}


def calculate_seats(num):
    return int(num / 700000)


if __name__ == '__main__':

    lj = 30

    print("State".ljust(lj),
          "Population".ljust(lj),
          "Senate".ljust(lj),
          "House of Representatives".ljust(lj),
          "Congress".ljust(lj)
    )

    for x, y in cities.items():
        senate = 2
        house_of_representatives = calculate_seats(y)
        congress = house_of_representatives + senate
        print(x.ljust(lj),
              str(y).ljust(lj),
              str(senate).ljust(lj),
              str(house_of_representatives).ljust(lj),
              str(congress).ljust(lj)
        )
