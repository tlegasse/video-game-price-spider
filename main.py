import product_data_query
import csv_builder
import sys
import os

if not os.path.isdir('data'):
    os.makedirs('data')

if len(sys.argv) == 1:
    sys.exit("Please sypply an argument or -h for help")

available_console_strings = {
    "brand-nintendo": [
        "nes",
        "super-nintendo",
        "nintendo-64",
        "gamecube",
        "wii",
        "wii-u",
        "nintendo-switch",
        "gameboy",
        "gameboy-color",
        "gameboy-advance",
        "nintendo-ds",
        "nintendo-3ds",
        "virtual-boy"
    ],
    "brand-playstation": [
        "playstation",
        "playstation-2",
        "playstation-3",
        "playstation-4",
        "playstation-5",
        "psp",
        "playstation-vita"
    ],
    "brand-sega": [
        "sega-master-system",
        "sega-genesis",
        "sega-cd",
        "sega-32x",
        "sega-saturn",
        "sega-dreamcast",
        "sega-game-gear",
        "sega-pico"
    ]
}


def print_help():
    print("""Options:\n-h              Show help.\n-b              Update documents by brand\n-c              Update documents by console\n\n =============================================\nAvailable brands:\n""")

    for brand in available_console_strings:
        print(f"  {brand}")

    print("\nAvailable consoles:")

    for brand in available_console_strings:
        for console in available_console_strings[brand]:
            print(f"  {console}")

if sys.argv[1] == '-h' or sys.argv[1] == '--help':
    print_help()

items_to_query = sys.argv[1:]

def update_by_console(console: str):
    console_data_query = product_data_query.ProductDataQuery()
    console_data_query.set_console(console)

    print(f"Querying {console}")
    console_data_query.call_data()

    console_csv_builder = csv_builder.CsvBuilder(console_data_query.get_product_data(),console)
    console_csv_builder.write_product_data_to_csv()

searching_brands = True

for item in items_to_query:
    if item == '-b':
        searching_brands = True
        continue
    elif item == '-c':
        searching_brands = False
        continue

    if searching_brands and item in available_console_strings:
        for console in available_console_strings[item]:
            update_by_console(console)

    elif not searching_brands:
        for brand in available_console_strings:
            if item not in available_console_strings[brand]:
                continue

            update_by_console(item)

