import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def MainApplication():
    # Root window
    root = tk.Tk()
    root.title("Weather App")
    root.geometry("700x400")

    # Entry fields and button
    tk.Label(root, text="Enter City:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    city_entry = tk.Entry(root)
    city_entry.grid(row=0, column=1, padx=5, pady=5, sticky="we")

    tk.Label(root, text="Your Interest:").grid(row=0, column=2, padx=5, pady=5, sticky="e")
    interest_entry = tk.Entry(root)
    interest_entry.grid(row=0, column=3, padx=5, pady=5, sticky="we")

    get_data_btn = tk.Button(root, text="Get data")
    get_data_btn.grid(row=0, column=4, padx=5, pady=5)

    # Tabs for Weather, Air Quality, Events, News
    notebook = ttk.Notebook(root)
    notebook.grid(row=1, column=0, columnspan=3, rowspan=4, padx=10, pady=10, sticky="nsew")

    weather_tab = ttk.Frame(notebook)
    air_tab = ttk.Frame(notebook)
    events_tab = ttk.Frame(notebook)
    news_tab = ttk.Frame(notebook)

    notebook.add(weather_tab, text="Weather")
    notebook.add(air_tab, text="Air Quality")
    notebook.add(events_tab, text="Events")
    notebook.add(news_tab, text="News")

    # Weather tab content
    tk.Label(weather_tab, text="Temperature:").grid(row=0, column=0, sticky="e")
    tk.Label(weather_tab, text="🌡️", font=("Arial", 24)).grid(row=0, column=1)

    tk.Label(weather_tab, text="Condition:").grid(row=1, column=0, sticky="e")
    tk.Label(weather_tab, text="⛅", font=("Arial", 24)).grid(row=1, column=1)

    tk.Label(weather_tab, text="Humidity:").grid(row=2, column=0, sticky="e")
    tk.Label(weather_tab, text="💧", font=("Arial", 24)).grid(row=2, column=1)

    # Tips section with Notes and Recommendations
    tips_frame = ttk.LabelFrame(root, text="Tips")
    tips_frame.grid(row=1, column=3, columnspan=2, rowspan=3, padx=10, pady=10, sticky="nsew")

    tips_notebook = ttk.Notebook(tips_frame)
    notes_tab = ttk.Frame(tips_notebook)
    recommend_tab = ttk.Frame(tips_notebook)

    tips_notebook.add(notes_tab, text="Notes:")
    tips_notebook.add(recommend_tab, text="Recomendations:")
    tips_notebook.pack(expand=True, fill="both")

    notes_text = tk.Text(notes_tab, height=10)
    notes_text.pack(expand=True, fill="both", padx=5, pady=5)

    recommend_text = tk.Text(recommend_tab, height=10)
    recommend_text.pack(expand=True, fill="both", padx=5, pady=5)

    # Buttons
    restart_btn = tk.Button(root, text="Restart")
    restart_btn.grid(row=4, column=0, padx=5, pady=5)

    exit_btn = tk.Button(root, text="Exit", command=root.quit)
    exit_btn.grid(row=4, column=3, padx=5, pady=5)

    about_btn = tk.Button(root, text="About", command=lambda: messagebox.showinfo("About", "Weather App GUI Demo"))
    about_btn.grid(row=4, column=4, padx=5, pady=5)

    root.columnconfigure(1, weight=1)
    root.columnconfigure(3, weight=1)
    root.rowconfigure(1, weight=1)

    root.mainloop()
