from essentials.scraper import overwrite_cards

# add a card to the cards_to_scrape list to scrape it
# if it's an onyx aswell, add it to the onyx_cards_to_scrape list

onyx_cards_to_scrape = ["Golem"]
cards_to_scrape = [
    "Golem",
    "Turkey Day",
    "Carver of Doom",
    "Harvest",
    "Plymouth Rock",
    "Robot Turkey",
    "Turkey Zombie",
    "Arcane Golem",
]


overwrite_cards(cards_to_scrape, onyx_cards_to_scrape)
