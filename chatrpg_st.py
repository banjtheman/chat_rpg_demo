"""
Purpose:
    ChatRPG streamlit UI
"""

# Python imports
from typing import Type, Union, Dict, Any, List
import time
import datetime
import os

# 3rd party imports
import streamlit as st
import utils
import streamlit.components.v1 as components

import utils
import ai_utils
import aws_utils

# embed streamlit docs in a streamlit app
st.set_page_config(layout="wide")

S3_BUCKET = os.environ["S3_BUCKET"]
JSON_OBJECT = os.environ["S3_OBJECT"]


def gen_aws_map(query):
    game_map = ai_utils.generate_chatgpt_map(query)

    print(game_map)
    game_map_array = eval(game_map)

    print(len(game_map_array))

    # Cap at a 100
    final_array = game_map_array[0:100]

    # Pad
    if len(final_array) < 100:
        # add grass
        while len(final_array) < 100:
            final_array.append(2816)

    # Update json file
    map_json_loc = "test_map.json"

    map_data = utils.load_json(map_json_loc)

    # Replace vals using for loop
    for index, val in enumerate(final_array):
        map_data["data"][index] = val

    # Gen NPCs
    hardcoded_npc_query = "Generate 3 NPCs for a medieval castle town"
    npcs = ai_utils.generate_chatgpt_npcs(hardcoded_npc_query)
    
    # TODO add NPCs to the map
    

    # Save the file
    utils.save_json(map_json_loc, map_data)

    # Upload to s3
    aws_utils.upload_file_to_s3_public(map_json_loc, S3_BUCKET, JSON_OBJECT)


def gen_local_map(query):
    game_map = ai_utils.generate_chatgpt_map(query)

    print(game_map)
    game_map_array = eval(game_map)

    print(len(game_map_array))

    # Cap at a 100
    final_array = game_map_array[0:100]

    # Pad
    if len(final_array) < 100:
        # add grass
        while len(final_array) < 100:
            final_array.append(2816)

    # Update json file
    map_json_loc = "example_game/ChatRPG_Demo/data/Map002.json"

    map_data = utils.load_json(map_json_loc)

    # Replace simple for loop
    for index, val in enumerate(final_array):
        map_data["data"][index] = val

    # Save the file
    utils.save_json(map_json_loc, map_data)


def sidebar() -> None:
    """
    Purpose:
        Shows the side bar
    Args:
        N/A
    Returns:
        N/A
    """

    st.sidebar.image(
        "https://assets-global.website-files.com/5efc0159f9a97ba05a8b2902/5f1a78b157e7c963621e7a91_latest-edition-rpg-maker-mz.jpg",
        use_column_width=True,
    )

    st.sidebar.markdown(
        "ChatRPG uses RPGMaker MZ and ChatGPT to create playable Role Playing Games (RPG) based on your prompt. **NOTE: Still testing expect errors**"
    )


def app() -> None:
    """
    Purpose:
        Controls the app flow
    Args:
        N/A
    Returns:
        N/A
    """

    # Spin up the sidebar
    sidebar()
    # Load questions

    sample_quries = [
        "Generate a 10x10 map with a long dirt road near a river. There should also be lush green grass around the map",
        "Generate a 10x10 map with a 6 tile wide dirt road that starts at (2,0) and stretches to (7,0), The road is repeated for every row in the map. The rest of the tiles are grass.",
        "Generate a 10x10 map with a 2x2 lake in the middle of the map. There should be a dirt road around the perimeter of the lake. The rest of tiles are grass.",
    ]

    sample_query = st.selectbox("Sample queries", sample_quries)

    query = st.text_input("Query:", sample_query)

    if st.button("Submit Query"):
        with st.spinner("Generating..."):
            
            # Gen Game
            gen_aws_map(query)




            timestamp = datetime.datetime.now().timestamp()

            # game_url = f"http://127.0.0.1:8080?timestamp={timestamp}"
            st.subheader(query)
            game_url = f"https://banjo-public-test-bucket.s3.amazonaws.com/chatrpg_test/ChatRPG+Demo/index.html?timestamp={timestamp}"

            st.write(
                f'<iframe width="100%" frameborder="0" style="overflow: hidden;height: 100vh" src="'
                + game_url
                + '"></iframe>',
                unsafe_allow_html=True,
            )


def main() -> None:
    """
    Purpose:
        Controls the flow of the streamlit app
    Args:
        N/A
    Returns:
        N/A
    """

    # Start the streamlit app
    st.title("ChatRPG")
    st.subheader("Generate RPG Games with AI")
    app()


if __name__ == "__main__":
    main()
