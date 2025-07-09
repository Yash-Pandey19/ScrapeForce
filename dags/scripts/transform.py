def clean_data(data):
    cleaned = [item.strip() for item in data if item]
    return cleaned
