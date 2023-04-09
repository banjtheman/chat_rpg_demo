import openai
import os
import random
import utils

# Set open AI Key
openai.api_key = os.environ["OPEN_AI_KEY"]

# Perhaps will have a generator for each type of map
# TODO generate map tiles

sample_query = "Generate a 10x10 map with a 6 tile wide dirt road that starts at (2,0) and stretches to (7,0), The road is repeated for every row in the map. The rest of the tiles are grass."
sample_array = [
    2816,
    2816,
    3200,
    3200,
    3200,
    3200,
    3200,
    3200,
    2816,
    2816,
    2816,
    2816,
    3200,
    3200,
    3200,
    3200,
    3200,
    3200,
    2816,
    2816,
    2816,
    2816,
    3200,
    3200,
    3200,
    3200,
    3200,
    3200,
    2816,
    2816,
    2816,
    2816,
    3200,
    3200,
    3200,
    3200,
    3200,
    3200,
    2816,
    2816,
    2816,
    2816,
    3200,
    3200,
    3200,
    3200,
    3200,
    3200,
    2816,
    2816,
    2816,
    2816,
    3200,
    3200,
    3200,
    3200,
    3200,
    3200,
    2816,
    2816,
    2816,
    2816,
    3200,
    3200,
    3200,
    3200,
    3200,
    3200,
    2816,
    2816,
    2816,
    2816,
    3200,
    3200,
    3200,
    3200,
    3200,
    3200,
    2816,
    2816,
    2816,
    2816,
    3200,
    3200,
    3200,
    3200,
    3200,
    3200,
    2816,
    2816,
    2816,
    2816,
    3200,
    3200,
    3200,
    3200,
    3200,
    3200,
    2816,
    2816,
]


sample_query_2 = "Generate a 10x10 map with a 4 tile wide dirt road that starts at (2,0) and stretches to (5,0), The road is repeated for every row in the map. The rest of the tiles are grass."

sample_array_2 = [
    2816,
    2816,
    3200,
    3200,
    3200,
    3200,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    3200,
    3200,
    3200,
    3200,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    3200,
    3200,
    3200,
    3200,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    3200,
    3200,
    3200,
    3200,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    3200,
    3200,
    3200,
    3200,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    3200,
    3200,
    3200,
    3200,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    3200,
    3200,
    3200,
    3200,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    3200,
    3200,
    3200,
    3200,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    3200,
    3200,
    3200,
    3200,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    3200,
    3200,
    3200,
    3200,
    2816,
    2816,
    2816,
    2816,
]

sample_query_3 = "Generate a 10x10 map with a 2x2 lake in the middle of the map. There should be a dirt road around the perimeter of the lake. The rest of tiles are grass."

sample_array_3 = [
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    3200,
    3200,
    3200,
    3200,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    3200,
    2336,
    2336,
    3200,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    3200,
    2336,
    2336,
    3200,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    3200,
    3200,
    3200,
    3200,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
    2816,
]


npc_sample_query = "Generate 5 NPCs for a medieval castle town"

npc_sample = [
    {
        "name": "Sir Reginald",
        "role": "knight",
        "gender": "male",
        "dialogue": "Greetings, traveler! I am Sir Reginald, a knight in service of the king. If you seek adventure, you've come to the right place.",
    },
    {
        "name": "Sister Elara",
        "role": "cleric",
        "gender": "female",
        "dialogue": "Blessings upon you, weary traveler. I am Sister Elara, a humble cleric tending to the sick and injured. May the light guide your path.",
    },
    {
        "name": "Old Man Cedric",
        "role": "villager",
        "gender": "male",
        "dialogue": "Ah, a new face in town! I'm Old Man Cedric, and I've lived here all my life. If you need any advice, don't hesitate to ask.",
    },
    {
        "name": "Lady Isabella",
        "role": "mage",
        "gender": "female",
        "dialogue": "Greetings, traveler. I am Lady Isabella, a mage studying the arcane arts. Be careful with magic - it can be as dangerous as it is powerful.",
    },
    {
        "name": "Young Tim",
        "gender": "male",
        "role": "villager",
        "dialogue": "Hi there! I'm Young Tim. I love exploring the castle and finding secret passages. Maybe we can explore together sometime!",
    },
]

npc_sample_dragon_query = "Generate 3 NPCs for a medieval castle town by a river, the main quest, is for the heroes to slay an evil dragon across the river "

npc_sample_dragon = [
    {
        "name": "Sir Gareth",
        "role": "knight",
        "gender": "male",
        "dialogue": "Greetings, brave one! I am Sir Gareth, entrusted with the task of slaying the evil dragon across the river. Join me in this noble quest!",
    },
    {
        "name": "Mystic Marina",
        "role": "mage",
        "gender": "female",
        "dialogue": "Hello, traveler. I am Mystic Marina, a mage researching the dragon's weaknesses. Together, we can bring an end to its reign of terror.",
    },
    {
        "name": "Fisherman Fergus",
        "role": "villager",
        "gender": "male",
        "dialogue": "Ahoy, adventurer! I'm Fisherman Fergus. The dragon's presence has made fishing near impossible. Please, help us restore peace to our town.",
    },
]


# NPC Map, hmm this is slighty annoying


# Cleric Actor1  Male 7, Female 8
# Villager Actor 1 Male 0, female 3
# Mage Actor3    2 - male 3- female
# Knights Actor3 6- male  7 -female

npc_map = {
    "cleric": {"actor": "Actor1", "male": 6, "female": 7},
    "villager": {"actor": "Actor1", "male": 0, "female": 3},
    "mage": {"actor": "Actor3", "male": 2, "female": 3},
    "knight": {"actor": "Actor3", "male": 6, "female": 7},
}


# Thank you chatgpt :)
def split_text(text, max_length):
    # Split the input text into a list of words
    words = text.split()
    # Initialize an empty list to store the lines of text
    lines = []
    # Initialize an empty list to store the words for the current line
    current_line = []

    # Iterate through each word in the list of words
    for word in words:
        # Check if adding the current word to the current line would keep its length within the limit
        if len(" ".join(current_line + [word])) <= max_length:
            # If so, append the word to the current line
            current_line.append(word)
        else:
            # Otherwise, join the words in the current line with spaces, and append the result to the list of lines
            lines.append(" ".join(current_line))
            # Start a new line with the current word
            current_line = [word]

    # After iterating through all words, add the last line to the list of lines
    if current_line:
        lines.append(" ".join(current_line))

    # Return the list of lines
    return lines


def gen_npc(npc, index):
    curr_index = index + 1
    npc_role = npc["role"]
    npc_gender = npc["gender"]
    npc_name = npc["name"]
    npc_dialogue = npc["dialogue"]

    split_n = 45

    npc_text = split_text(npc_dialogue, split_n)
    # A place holder to replace latter
    for npc_index, text in enumerate(npc_text):
        text = text.replace("'", "LOLCATSNBURGER")
        npc_text[npc_index] = text

    # print(npc_text)

    example_event = {
        "id": 2,
        "name": "EV002",
        "note": "",
        "pages": [
            {
                "conditions": {
                    "actorId": 1,
                    "actorValid": False,
                    "itemId": 1,
                    "itemValid": False,
                    "selfSwitchCh": "A",
                    "selfSwitchValid": False,
                    "switch1Id": 1,
                    "switch1Valid": False,
                    "switch2Id": 1,
                    "switch2Valid": False,
                    "variableId": 1,
                    "variableValid": False,
                    "variableValue": 0,
                },
                "directionFix": False,
                "image": {
                    "tileId": 0,
                    "characterName": "Actor3",
                    "direction": 2,
                    "pattern": 0,
                    "characterIndex": 6,
                },
                "list": [
                    {
                        "code": 101,
                        "indent": 0,
                        "parameters": ["Actor3", 6, 0, 2, "Knight"],
                    },
                    # {"code": 401, "indent": 0, "parameters": ["Command me"]},
                    # {"code": 0, "indent": 0, "parameters": []},
                ],
                "moveFrequency": 3,
                "moveRoute": {
                    "list": [{"code": 0, "parameters": []}],
                    "repeat": True,
                    "skippable": False,
                    "wait": False,
                },
                "moveSpeed": 3,
                "moveType": 0,
                "priorityType": 1,
                "stepAnime": False,
                "through": False,
                "trigger": 0,
                "walkAnime": True,
            }
        ],
        "x": 1,
        "y": 0,
    }

    example_event["id"] = curr_index
    example_event[
        "name"
    ] = f"EV00{curr_index}"  # TODO will need to change if more than 9 events
    example_event["pages"][0]["image"]["characterName"] = npc_map[npc_role][
        "actor"
    ]  # actor type
    example_event["pages"][0]["image"]["characterIndex"] = npc_map[npc_role][
        npc_gender
    ]  # npc gender

    example_event["pages"][0]["list"][0]["parameters"][0] = npc_map[npc_role][
        "actor"
    ]  # actor type
    example_event["pages"][0]["list"][0]["parameters"][1] = npc_map[npc_role][
        npc_gender
    ]  # actor gender
    example_event["pages"][0]["list"][0]["parameters"][4] = npc_name  # NPC Name

    # example_event["pages"][0]["list"][1]["parameters"][0] = npc_dialogue  # diaglogue

    # Add all text events in the char intervals
    for curr_text in npc_text:
        text_json = {
            "code": 401,
            "indent": 0,
            "parameters": [f"{curr_text}"],
        }  # diaglogue
        example_event["pages"][0]["list"].append(text_json)
    example_event["pages"][0]["list"].append({"code": 0, "indent": 0, "parameters": []}) # final parm thats in all chats
 
    # TODO will need to place the NPCs some where that make sense
    example_event["x"] = random.randint(0, 9)
    example_event["y"] = random.randint(0, 9)

    return example_event


def create_npc_events(npcs):
    events = [
        "null",
    ]
    for index, npc in enumerate(npcs):
        print("Creating NPC event")

        npc_event = gen_npc(npc, index)
        events.append(npc_event)

    new_string = (
        str(events)
        .replace("True", "true")
        .replace("False", "false")
        .replace("'null'", "null")
    )
    new_string = new_string.replace("'", '"')
    new_string = new_string.replace("LOLCATSNBURGER", "'")

    return new_string


# For npcs
def generate_chatgpt_npcs(query: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # GPT3.5 is good enough since its just text generation
        messages=[
            {
                "role": "system",
                "content": "You are an RPG Maker Map Generation Bot. Your role is to generate text for NPCs in a given area based on a user's query. There are 4 types of NPCs, for this game: knight cleric, villager, and mage Do not provide an explanation, just the array for the NPCs. The output is used in a python application and any explanation text will break the system.",
            },
            {
                "role": "user",
                "content": f"""{npc_sample_query}""",
            },
            {
                "role": "assistant",
                "content": f"""{npc_sample}""",
            },
            {
                "role": "user",
                "content": f"""{npc_sample_dragon_query}""",
            },
            {
                "role": "assistant",
                "content": f"""{npc_sample_dragon}""",
            },
            {
                "role": "user",
                "content": f"""{query}""",
            },
        ],
    )

    # print(response)
    # question = response["choices"][0]["text"].strip(" \n")
    game_map = response["choices"][0]["message"]["content"].strip(" \n")

    return game_map


# For outside maps
def generate_chatgpt_map(query: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are an RPG Maker Map Generation Bot. Your role is to generate two dimensional maps e.g (x,y coordinates) for RPG Maker based games based on a user's query. You must provide a tile for each coordinate of the map. The user will also provide the number of tiles. The value 2816 represents a grass tile and the value 3200 represents a dirt road tile and 2336 represents a water tile. Do not provide an explanation, just the array for the user. The output is used in a python application and any explanation text will break the system.",
            },
            {
                "role": "user",
                "content": f"""\n\Query:\n{sample_query}`"\nNumber of tiles: 100\n\Array format:[Tile1,Tile2,..,TileN]""",
            },
            {
                "role": "assistant",
                "content": f"""{sample_array}""",
            },
            {
                "role": "user",
                "content": f"""\n\Query:\n{sample_query_2}`"\nNumber of tiles: 100\n\Array format:[Tile1,Tile2,..,TileN]""",
            },
            {
                "role": "assistant",
                "content": f"""{sample_array_2}""",
            },
            {
                "role": "user",
                "content": f"""\n\Query:\n{sample_query_3}`"\nNumber of tiles: 100\n\Array format:[Tile1,Tile2,..,TileN]""",
            },
            {
                "role": "assistant",
                "content": f"""{sample_array_3}""",
            },
            {
                "role": "user",
                "content": f"""\n\Query:\n{query}`"\nNumber of tiles: 100\n\Array format:[Tile1,Tile2,..,TileN]""",
            },
        ],
    )

    # print(response)
    # question = response["choices"][0]["text"].strip(" \n")
    game_map = response["choices"][0]["message"]["content"].strip(" \n")

    return game_map


# Test
# print("hello?")
# npc_string = create_npc_events(npc_sample_dragon)
# print(npc_string)
# test_map = utils.read_from_file("test_map.json")
# test_map = test_map.replace('"events": []', f'"events":{npc_string}')
# utils.write_to_file("test_map2.json", test_map)
