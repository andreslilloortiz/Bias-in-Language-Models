import pandas as pd
import re
import os

# ==========================================
# 1. CONFIGURATION & DICTIONARIES
# ==========================================

# Base dictionary mapping gendered terms to their neutral equivalents.
# Note: All keys MUST be lowercase for the regex lookup to work correctly.
BASE_REPLACEMENTS = {
    # Pronouns
    'she': 'they', 'he': 'they', 'her': 'their', 'his': 'their', 'hers': 'theirs',
    'him': 'them', 'herself': 'themselves', 'himself': 'themselves',

    # Nouns (Adults)
    'man': 'person', 'woman': 'person', 'men': 'people', 'women': 'people',
    'guy': 'person', 'guys': 'people', 'male': 'person', 'female': 'person',
    'males': 'people', 'females': 'people', 'lady': 'person', 'ladies': 'people',
    'gentleman': 'person', 'gentlemen': 'people',

    # Childhood
    'boy': 'child', 'girl': 'child', 'boys': 'children', 'girls': 'children',

    # Family
    'father': 'parent', 'mother': 'parent', 'dad': 'parent', 'mom': 'parent',
    'brother': 'sibling', 'sister': 'sibling', 'son': 'child', 'daughter': 'child',

    # Couples
    'husband': 'spouse', 'wife': 'spouse', 'boyfriend': 'partner', 'girlfriend': 'partner',

    # Titles (Removed entirely to neutralize)
    'mr.': '', 'mrs.': '', 'ms.': '', 'miss': ''
}

# ==========================================
# 2. REGEX COMPILATION (OPTIMIZATION)
# ==========================================

def build_regex_and_lookup(proper_nouns_path):
    """
    Loads proper names, merges them with the base replacements,
    and compiles a single, highly optimized regex pattern.
    """
    lookup_dict = BASE_REPLACEMENTS.copy()

    # Load proper names from the CSV and map them to the '[NAME]' token
    print(f"Loading proper nouns from '{proper_nouns_path}'...")
    try:
        nouns_df = pd.read_csv(proper_nouns_path)
        for name in nouns_df['Name'].dropna():
            name_clean = str(name).strip().lower()
            lookup_dict[name_clean] = '[NAME]'
    except FileNotFoundError:
        print(f"Warning: File '{proper_nouns_path}' not found. Proceeding without proper names.")

    # Sort words by length in descending order.
    # This is CRUCIAL so the regex matches 'herself' before 'her', preventing partial replacements.
    words = sorted(lookup_dict.keys(), key=len, reverse=True)

    # Escape special characters (like the '.' in 'mr.') and join with the OR operator '|'
    escaped_words = [re.escape(w) for w in words]
    pattern_string = r'\b(' + '|'.join(escaped_words) + r')\b'

    # Compile the giant regex pattern (case-insensitive)
    giant_regex = re.compile(pattern_string, re.IGNORECASE)

    return giant_regex, lookup_dict

# Compile the specific pattern for Reddit demographics (e.g., "21m", "27f")
# \d{1,2} matches 1 or 2 digits, [mf] matches 'm' or 'f'
REDDIT_DEMO_REGEX = re.compile(r'\b\d{1,2}[mf]\b', re.IGNORECASE)

# ==========================================
# 3. TEXT PROCESSING FUNCTIONS
# ==========================================

def neutralize_text(text, giant_regex, lookup_dict):
    """
    Applies the neutralization rules to a single string using O(1) text traversal.
    """
    # Handle NaN or non-string values safely
    if not isinstance(text, str):
        return text

    # Helper function to dynamically fetch the replacement from the dictionary
    def get_replacement(match):
        # match.group(1).lower() gets the matched word and forces it to lowercase
        # so it accurately matches the keys in our lookup_dict
        return lookup_dict[match.group(1).lower()]

    # 1. Replace all pronouns, nouns, and proper names in one single pass
    text = giant_regex.sub(get_replacement, text)

    # 2. Replace Reddit demographic markers with the neutral word 'age'
    text = REDDIT_DEMO_REGEX.sub('age', text)

    # Optional: Clean up multiple spaces that might appear after deleting titles like 'mr.'
    text = re.sub(r'\s+', ' ', text).strip()

    return text

# ==========================================
# 4. MAIN EXECUTION
# ==========================================

def main():
    proper_nouns_file = 'proper_nouns_EN.csv'

    # List of datasets to process
    files_to_process = [
        'selfharm/selfharm_1.csv',
        'selfharm/selfharm_2.csv',
        'selfharm/selfharm_augmented.csv',
        'selfharm/selfharm_augmented2.csv'
    ]

    # Initialize the regex engine
    giant_regex, lookup_dict = build_regex_and_lookup(proper_nouns_file)

    print("\nStarting the gender scrubbing process...\n")

    for filepath in files_to_process:
        if not os.path.exists(filepath):
            print(f"Skipping '{filepath}' (File not found).")
            continue

        print(f"Processing '{filepath}'...")
        df = pd.read_csv(filepath)

        # Apply the neutralization to the relevant columns if they exist
        columns_to_neutralize = ['title', 'body', '0']

        for col in columns_to_neutralize:
            if col in df.columns:
                # Use a lambda to pass our pre-compiled regex and dictionary
                df[col] = df[col].apply(lambda x: neutralize_text(x, giant_regex, lookup_dict))

        # Define the output filename and save the cleaned dataset
        output_name = filepath.replace('.csv', '_neutral.csv')
        df.to_csv(output_name, index=False)
        print(f"  -> Saved cleaned dataset as '{output_name}'")

    print("\nThe entire mitigation process has been successfully completed.")

if __name__ == "__main__":
    main()