from api.search import search_game
from api.utils import format_game_data

def main():
    """
    Main function to run the game search and display results.
    """
    try:
        game_name = input("Enter the name of the game to search for: ").strip()
        page_size = int(input("Enter the number of results to return (default is 3): ") or 3)
        
        # Search for games
        games = search_game(game_name, page_size)
        
        # Format and display the game data
        formatted_data = format_game_data(games)
        print(formatted_data)
    
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")