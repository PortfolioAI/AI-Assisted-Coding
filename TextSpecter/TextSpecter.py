import string
import tkinter as tk
from tkinter import filedialog, messagebox
from collections import Counter

COMMON_WORDS = set([
    "and", "to", "the", "of", "in", "is", "on", "for", "with", "as", "it", "at", "by", "an", "be", "or", "we", "you",
    "not", "from", "but", "are", "they", "he", "she", "we", "I", "this", "that", "have", "do", "was", "can", "will",
    "my", "your", "his", "her", "its", "our", "their", "there", "when", "where", "how", "why", "which", "who", "whom",
    "me", "us", "them"
])

CHARACTER_CATEGORIES = {
    "standard": set(string.ascii_letters + string.digits + string.punctuation),
    "whitespace": set(string.whitespace),
    "diacritics": set("áéíóúýÁÉÍÓÚÝäëïöüÿÄËÏÖÜàèìòùÀÈÌÒÙãñõÃÑÕâêîôûÂÊÎÔÛçÇ"),
    "currency": set("¢£¤¥€₹₽₺₩$")
}

def select_file():
    """Prompt the user to select a file and return the file path."""
    root = tk.Tk()
    root.withdraw()
    try:
        filepath = filedialog.askopenfilename(title="Select a text file", filetypes=[
            ("Text files", "*.txt"), ("All files", "*.*")])
        root.destroy()
        return filepath
    except Exception as e:
        messagebox.showerror("Error", f"Error while selecting the file: {e}")
        root.destroy()

def read_file(filename):
    """Read the content of the given file."""
    try:
        with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading the file: {e}")
        return None

def categorize_characters(text):
    """Categorize the characters in the given text."""
    char_freq = Counter(text)
    categories = {
        name: {char for char in charset if char in char_freq}
        for name, charset in CHARACTER_CATEGORIES.items()
    }

    uncommon_chars = set(char_freq.keys()) - set().union(*CHARACTER_CATEGORIES.values())
    categories["uncommon"] = uncommon_chars

    return categories, char_freq

def count_common_words(text):
    """Count occurrences of common words in the given text."""
    word_freq = Counter(text.lower().split())
    return {word: word_freq[word] for word in COMMON_WORDS}

def summarize_characters(filename):
    """Provide a summary of characters in the given file."""
    text = read_file(filename)
    if text is None:
        return

    categories, freq = categorize_characters(text)

    print(f"\nSummary for '{filename}':")
    print(f"\nTotal characters: {len(text)}")
    print(f"Unique characters: {len(freq)}")

    for cat, chars in categories.items():
        count = sum(freq[char] for char in chars)
        if count:
            print(f"\n{cat.title()} characters (total {count}):")
            for char in sorted(chars):
                print(f"'{char}' : {freq[char]}")

    threshold = 0.01 * len(text)
    infrequent_chars = {char: count for char, count in freq.items() if count < threshold}
    if infrequent_chars:
        print("\nInfrequent characters:")
        for char, count in sorted(infrequent_chars.items(), key=lambda x: x[1]):
            print(f"'{char}' : {count}")

    common_word_counts = count_common_words(text)
    if common_word_counts:
        print("\nCommon word counts:")
        for word, count in sorted(common_word_counts.items(), key=lambda x: x[1], reverse=True):
            print(f"{word} : {count}")

def main():
    """Main function to run the character summarizer."""
    file_path = select_file()
    if file_path:
        summarize_characters(file_path)
    else:
        print("No file selected.")
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
