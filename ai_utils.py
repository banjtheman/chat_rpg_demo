import openai
import os


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


# For outside maps
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
                "content": f"""{npc_sample_dragon}""",
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
