import pandas as pd

# Load the video game data from a CSV file
video_game_data = pd.read_csv('video_games_raw.csv')

# ask user for a row number to inspect
while True:
    try:
        row_number = int(input("Enter a row number to inspect: "))
    except ValueError:
        print("Please enter a whole number.")
        continue

    if 0 <= row_number < len(video_game_data):
        break

# Display the selected row
print(video_game_data.iloc[row_number])


# Update status
# check to see if the status is valid
while True:
    try:
        status_row = input("Please enter a new status: ")
        if not status_row in ["Backlog", "Playing", "Completed", "Dropped"]:
            raise ValueError("Status cannot be empty.")
    except ValueError:
        print("Please enter a valid status.")
        continue

# update the status in the DataFrame
    if status_row in ["Backlog", "Playing", "Completed", "Dropped"]:
        video_game_data.at[row_number, 'Status'] = status_row
        break

# Add a new column for recommended status
video_game_data["Recommended"] = "No"


# Update recommended status
video_game_data.loc[
    (video_game_data["Rating"] >= 8) &
    (video_game_data["Price"] <= 40),
    "Recommended"
] = "Yes"


# Filter recommended games
recommended_games = video_game_data.query('Recommended == "Yes"')

# Display recommended games
print("Recommended Games:")
print(recommended_games[['Title', 'Price', 'Rating']])

# Save the updated catalog to a new CSV file
video_game_data.to_csv('video_games_cleaned.csv', index=False) 

print("The catalog has been updated.")
print("Saved as video_games_cleaned.csv.")





