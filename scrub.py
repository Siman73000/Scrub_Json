import json
from datetime import datetime

FIELDS_TO_KEEP = [
    "id", "name", "mana_cost", "cmc", "type_line",
    "power", "toughness", "produced_mana", "set_name",
    "rarity", "artist", "png", "collector_number"
]
DATE_FIELD = "released_at"
CUTOFF_DATE = datetime(2021, 12, 31)

def filter_card_data(card):
    # Check if the card's release date exists and is after the cutoff date
    release_date_str = card.get(DATE_FIELD)
    if release_date_str:
        release_date = datetime.strptime(release_date_str, "%Y-%m-%d")
        if release_date > CUTOFF_DATE:
            filtered_data = {field: card[field] for field in FIELDS_TO_KEEP if field in card}
            return filtered_data
    return None  # Exclude cards without a release date or those released before 2021

def clean_json_file(input_file, output_file):
    with open(input_file, 'r') as infile:
        data = json.load(infile)
    
    # Filter out only the cards that meet the date requirement
    cleaned_data = [filter_card_data(card) for card in data if filter_card_data(card) is not None]
    
    with open(output_file, 'w') as outfile:
        json.dump(cleaned_data, outfile, indent=4)

input_file = 'All_MTG_Card_Info.json'
output_file = 'cleaned_cards.json'

clean_json_file(input_file, output_file)
