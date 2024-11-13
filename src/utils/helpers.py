import os

def load_ascii_art():
    ascii_file = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'assets', 'ascii_art.txt')
    try:
        with open(ascii_file, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except Exception as e:
        print(f"Error loading ASCII art: {e}")
        return ""