import os
import importlib
import openai
import streamlit as st

# Store API key in environment variable
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="Chat with ZinoGPT")
st.title("Chat with ZinoGPT")
st.sidebar.markdown("Developed by Zine-Eddine KHENE](https://twitter.com/ZineEddineKhene)", unsafe_allow_html=True)
st.sidebar.markdown("gpt-3.5-turbo")
st.sidebar.markdown("Not optimised")
st.sidebar.markdown("May run out of OpenAI credits")


def list_bots():
    bot_files = os.listdir("bots")
    bots = [os.path.splitext(bot)[0] for bot in bot_files if bot.endswith('.py')]
    return bots


def choose_bot():
    bots = list_bots()
    print("Available bots:")
    for index, bot in enumerate(bots, 1):
        print(f"{index}. {bot}")

    choice = int(input("Choose a bot by entering its number: ")) - 1
    return bots[choice]


def select_bot():
    chosen_bot = choose_bot()
    bot_module = importlib.import_module(f"bots.{chosen_bot}")
    bot_module.main()


if __name__ == "__main__":
    select_bot()
    
st.title("Ask Zino_GPT")
query = st.text_input("What would you like to ask?", "")

if st.button("Submit"):
    response = index.query(query)
    st.write(response)
