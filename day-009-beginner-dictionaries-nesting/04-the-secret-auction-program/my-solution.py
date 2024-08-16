from typing import TypedDict, List


class AuctionData(TypedDict):
    name: str
    bid: float


auction_data: List[AuctionData] = []

have_person_to_bid = True

while have_person_to_bid:
    name = input("What is your name: ")
    bid = float(input("What is your bid: "))

    auction_data.append({
        "name": name,
        "bid": bid,
    })

    have_person_to_bid = input(
        "Have more people to bid? y or n: "
    ).lower() == 'y'


auction_data.sort(key=lambda data: data["bid"], reverse=True)

winner = auction_data[0]

print(f"{winner['name']} is the winner! the bid was: {winner['bid']}")
