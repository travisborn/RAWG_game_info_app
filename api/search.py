import requests
from dotenv import load_dotenv
import os
from .utils import get_api_key, build_url

def search_game(game_name: str, page_size: int = 3):
    """
    Search for games by name.
    Args:
        game_name (str): The name of the game to search for.
        page_size (int): The number of results to return per page.
    Returns:
        list: A list of games matching the search criteria.
    """

    # Validate input parameters
    if not game_name or game_name.strip() == "":
        raise ValueError("Game name must not be empty.")
    if page_size <= 0:
        raise ValueError("Page size must be a positive integer.")

    # Build query parameters
    params = {
        "search": game_name,
        "page_size": page_size,
        "key": get_api_key()
    }

    # Build the URL for the API request
    url = build_url("/games")

    # Make the API request with error handling
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
    except requests.exceptions.RequestException as e:
        raise Exception(f"API request failed: {e}")
    
    # Parse the response data
    games = data.get("results", [])
    if not games:
        print("No games found matching the search criteria.")
        return []
    
    results = [] # Initialize results list
    # Extract relevant information from each game
    for game in games:
        results.append({
            "id": game.get("id"),
            "name": game.get("name"),
            "released": game.get("released"),
            "rating": game.get("rating"),
            "platforms": [platform["platform"]["name"] for platform in game.get("platforms", [])],
            "genres": [genre["name"] for genre in game.get("genres", [])]
        })

    return results