data = {
    'text': [
        'I love this place!',
        'This is terrible.',
        'I am very happy with the service.',
        'I hate waiting.',
        'What a wonderful experience!',
        'This is the worst product ever.',
        'I am extremely satisfied.',
        'Not bad, could be better.',
        'Absolutely fantastic!',
        'Really disappointed.'
    ],
    'sentiment': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]  # 1 = Positive, 0 = Negative
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Display the first few rows
df.head()
