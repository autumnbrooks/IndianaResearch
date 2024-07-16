import json

# Function to read JSON data from a file
def load_json_file(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

# Load initial and new JSON data
initial_data = load_json_file('flowgpt-reviews.json')
new_data = load_json_file('new.json')

# Function to update reviews
def update_reviews(initial_data, new_data):
    for initial in initial_data:
        for new in new_data:
            if initial.get('bot_name') == new.get('bot_name'):
                initial_reviews = initial.get('reviews', [])
                new_reviews = new.get('reviews', [])
                for review in new_reviews:
                    if review and review not in initial_reviews:
                        initial_reviews.append(review)
                initial['reviews'] = initial_reviews
    return initial_data

# Update the reviews
updated_data = update_reviews(initial_data, new_data)

# Save the updated JSON data back to a file
with open('updated_data.json', 'w') as f:
    json.dump(updated_data, f, indent=4)

updated_file = load_json_file('updated_data.json')

print("Reviews updated and saved to updated_data.json")
print('\n', updated_file)
