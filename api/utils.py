import os
from typing import List
from typing import Dict
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file

def get_api_key():
    """
    Load the API key from environment variables.
    Returns:
        str: The API key for the game database.
    """
    api_key = os.getenv("RAWG_API_KEY")
    if not api_key:
        raise ValueError("API key not found. Please set the API_KEY environment variable.")
    return api_key

def build_url(endpoint: str) -> str:
    """
    Build the full URL for the API request.
    Args:
        endpoint (str): The API endpoint to append to the base URL.
    Returns:
        str: The full URL for the API request.
    """
    base_url = "https://api.rawg.io/api"  # The base URL of the API
    return f"{base_url}{endpoint}"

def format_game_data(games: List[Dict]) -> str:
    """
    Format the game data into a readable string.
    Args:
        games (List[dict]): A list of game dictionaries.
    Returns:
        str: A formatted string of game information.
    """
    if not games:
        return "No games found."
    
    formatted_games = []
    for game in games:
        formatted_games.append(
            f"🎮 {game['name']}\n📅 Released: {game['released']}\n"
            f"⭐ Rating: {game['rating']}\n🕹️  Platforms: {', '.join(game['platforms'])}\n"
            f"🏷️  Genres: {', '.join(game['genres'])}\n{'-' * 80}"
        )
    
    return "\n".join(formatted_games)
 