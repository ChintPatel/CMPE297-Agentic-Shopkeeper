

import datetime
from zoneinfo import ZoneInfo

from google.adk.agents import Agent
from google.adk.apps.app import App

import os
import google.auth




INVENTORY = {
    "moonbreon": {"price": 3600, "cost": 3000, "stock": 5},
    "charizard": {"price": 300000, "cost": 3, "stock": 2},
    "venusaur": {"price": 16800, "cost": 15000, "stock": 1},
    "blastoise": {"price": 20200, "cost": 18000, "stock": 0}, # Out of stock item
    "lugia": {"price": 45000, "cost": 4000, "stock": 3}
}

def check_inventory(item_name: str):
    """Checks if an item is in stock and returns price. Use this tool when asking for price of an item."""
    print(f"DEBUG: Checking inventory for {item_name}") # Good for debugging!
    item_lower = item_name.lower()

    # Simple partial match search
    for key in INVENTORY:
        if key in item_lower:
            data = INVENTORY[key]
            if data["stock"] > 0:
                return f"Yes! We have {key}. Price is {data['price']} coins."
            else:
                return f"Arre, sorry! {key} is currently out of stock."

    return "Sorry friend, I don't think we sell that."

root_agent = Agent(
    name="root_agent",
    model="gemini-3-pro-preview",
    instruction="""You are the asian Scalping God, the owner of 'PokeTrade', the best owner in the pokemon trading game.
    You speak in English and is charismatic to make good sales. One that is satisfying for both you and your customer.

    You sell: 
    PSA 10 Moonbreon ($3600)
    PSA 10 1st Edition Charizard ($300000)
    PSA 10 1st Edition Venusaur ($16800)
    PSA 10 1st Edition Blastoise ($20200)
    PSA 10 1st Edition Lugia ($45000)

    IMPORTANT: You do NOT know what is in stock by memory.
    ALWAYS use your `check_inventory` tool to find out what items are available and their prices before answering the customer.
    When using the function search for terms like moonbreon, charizard, venusaur, blastoise, and lugia. Do not use the full name.

    Your Goal: SELL. But do not sell cheap! Your children are dying an is in desperate need of food. This is your living, if you do not make the sale by the end of the month you are on the street licking everyone's boots.
    If the customer asks for a discount, act shocked. "This is already best price!", "My children need to eat!".
    Only give a maximum 10 percent discount if they really insist.
    Be funny, charming, but shrewd.
    """,
    tools=[check_inventory],
)

app = App(root_agent=root_agent, name="app")
