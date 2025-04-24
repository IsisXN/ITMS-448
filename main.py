import tkinter as tk
from gui import MainApplication
from api_client import APIClient
from recommendation_engine import RecommendationEngine

def main():
    root = tk.Tk()
    root.title("Smart Weather & Lifestyle Recommender")
    
    # Initialize components
    api_client = APIClient()
    recommendation_engine = RecommendationEngine(api_client)
    
    # Create main application
    app = MainApplication(root, api_client, recommendation_engine)
    
    # Run the application
    root.mainloop()

if __name__ == "__main__":
    main()