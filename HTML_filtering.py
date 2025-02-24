import re
import os

HTML_DIR = "HTML_files"

# This regular expression will capture:
#   RG-50. (then one of 030|106|233|344) . some digits _trs_en_cleaned.html
#   For example: "RG-50.030.0001_trs_en_cleaned.html"
pattern = re.compile(r'^RG-50\.(030|106|233|344)\.\d+_trs_en_cleaned\.html$')

mathced_by_group = {
    "030":[],
    "106":[],
    "233":[],
    "344":[]
}



for filename in os.listdir(HTML_DIR):
    # Check for a match
    match = pattern.match(filename)
    if match:
        group_num = match.group(1)  # This will be 030, 106, 233, or 344
        matches_by_group[group_num].append(filename)



# Define regex patterns for common errors
error_patterns = {
    "Metadata Pollution (URLs, Emails)": r"https?://[^\s]+|Contact\sreference@[^\s]+",
    "Incorrect <span class='page-break'> Inserts": r"<span class=\"page-break\"[^>]*></span>",
    "Mismatched Question Blocks": r"(<dialogue class=\"Question\">.*?</dialogue>){2,}",
    "Split Answers Due to Line Breaks": r"<dialogue class=\"Answer\">.*?<p>A:\s*\w+</p></dialogue>\s*<dialogue class=\"Answer\">.*?<p>\w+</p></dialogue>",
    "Corrupted Text (Gibberish)": r"\b[a-zA-Z]{15,}\b",  # Detects abnormally long non-dictionary words
    "Extraneous Tags from PDF Parsing": r"<p>\s*Interview with\s+.*?,\s+\w+\s+\d{1,2},\s+\d{4}</p>",
    "Interview Endings": r"(END OF INTERVIEW|Conclusion of Interview)"
}



def find_errors_in_file(file_path, patterns):
    """
    Returns a dictionary {pattern: count_occurrences, ...} for each pattern in the file.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    results = {}
    for pat in patterns:
        matches = re.findall(pat, content, flags=re.DOTALL)
        if matches:
            results[pat] = len(matches)
        else:
            results[pat] = 0
    return results


# Process files and track errors
error_summary = []

