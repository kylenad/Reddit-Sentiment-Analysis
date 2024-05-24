import re
import emoji

def preprocess(text):
    # Remove URLs entirely
    text = re.sub(r'https?://\S+|www\.\S+', '', text)

    # Uniformly replace Reddit user mentions with 'u/user' or completely remove them
    text = re.sub(r'\bu/[\w-]+', 'user', text)

    # Remove emojis from the entire text
    text = emoji.replace_emoji(text, replace='')

    return text

# Example usage
text = "Hello u/someone, check this out: https://example.com and enjoy the emoji 👏😊👍!"
clean_text = preprocess(text)
print(clean_text)