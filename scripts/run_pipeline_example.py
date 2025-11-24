from pipelines.text_processing import clean_text
from pipelines.embeddings import fit_tfidf

def main():
    print("Running pipeline example...")
    sample_text = "This is a TEST article."
    cleaned = clean_text(sample_text)
    print(f"Original: {sample_text}")
    print(f"Cleaned: {cleaned}")

if __name__ == "__main__":
    main()