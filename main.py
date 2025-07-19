from api.search import search_game
from api.utils import format_game_data

def main():
    """
    Main function to run the game search and display results.
    """
    # Get user input for the game name and page size
    game_name = input("Enter the name of the game to search for: ").strip()
    if not game_name:
        print("Game name cannot be empty.")
        return
    page_size = input("Enter the number of results to return per page (default is 3): ").strip()
    page_size = int(page_size) if page_size.isdigit() else 3

    try:
        # Search for games using the provided name and page size
        games = search_game(game_name, page_size)
        
        # Format and display the game data
        formatted_data = format_game_data(games)
        print(formatted_data)
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()