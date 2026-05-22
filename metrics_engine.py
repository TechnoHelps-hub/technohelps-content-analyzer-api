import re
import math
from collections import Counter

def count_syllables_in_word(word: str) -> int:
    """
    Calculates the exact syllable count of a single word using structural 
    linguistic rule matching. Designed for TechnoHelps core processing engine.
    """
    word = word.lower().strip()
    if not word:
        return 0
        
    # Remove basic trailing punctuation attached to the token
    word = re.sub(r'[^\w]', '', word)
    if not word:
        return 0

    # Explicit handling for ultra-short words
    if len(word) <= 3:
        return 1

    # Match vowel groups to identify standard diphthongs and syllables
    vowel_pattern = re.compile(r'[aeiouy]+')
    syllable_count = len(vowel_pattern.findall(word))

    # Linguistic Rule: Drop silent trailing 'e' (e.g., 'code', 'more')
    if word.endswith('e'):
        if not word.endswith('le'):
            syllable_count -= 1

    return max(1, syllable_count)

def calculate_time_format(word_count: int, words_per_minute: int) -> dict:
    """
    Computes precise minute and second structures based on fixed speech/reading velocity rates.
    """
    total_seconds = int((word_count / words_per_minute) * 60)
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    
    # Generate human readable format string
    readable_string = f"{minutes} min {seconds} sec" if minutes > 0 else f"{seconds} sec"
    
    return {
        "total_seconds": total_seconds,
        "formatted": readable_string
    }

def analyze_text_structure(text: str) -> dict:
    """
    Parses complex multi-paragraph string payloads, running full readability formulas,
    calculated estimated time matrices, and executing custom stop-word filtered keyword arrays.
    """
    if not text.strip():
        return {
            "total_paragraphs": 0,
            "total_sentences": 0, 
            "total_words": 0, 
            "total_syllables": 0, 
            "flesch_score": 0.0, 
            "difficulty": "Empty Text",
            "reading_time": {"total_seconds": 0, "formatted": "0 sec"},
            "speaking_time": {"total_seconds": 0, "formatted": "0 sec"},
            "keyword_matrix": []
        }

    # 1. Capture Total Paragraphs safely
    paragraphs = [p for p in text.split('\n') if p.strip()]
    total_paragraphs = max(1, len(paragraphs))

    # 2. Text Normalization for Bulletproof Calculation Stream
    normalized_text = text.replace('\r\n', ' ').replace('\n', ' ').replace('\r', ' ')

    # 3. Structural Segment Calculations (Original un-filtered text for global tracking)
    sentences = [s for s in re.split(r'[.!?]+', normalized_text) if s.strip()]
    total_sentences = max(1, len(sentences))

    words = [w.lower() for w in re.findall(r'\b[a-zA-Z]+\b', normalized_text)]
    total_words = max(1, len(words))

    total_syllables = sum(count_syllables_in_word(w) for w in words)

    # 4. Standard Flesch Reading Ease Execution
    asl = total_words / total_sentences
    asw = total_syllables / total_words
    flesch_score = 206.835 - (1.015 * asl) - (84.6 * asw)
    flesch_score = round(max(0.0, min(100.0, flesch_score)), 2)

    if flesch_score >= 90.0:
        interpretation = "Very Easy (5th Grade level)"
    elif flesch_score >= 80.0:
        interpretation = "Easy (6th Grade level)"
    elif flesch_score >= 70.0:
        interpretation = "Fairly Easy (7th Grade level)"
    elif flesch_score >= 60.0:
        interpretation = "Standard/Moderate (8th & 9th Grade level)"
    elif flesch_score >= 50.0:
        interpretation = "Fairly Difficult (High School level)"
    elif flesch_score >= 30.0:
        interpretation = "Difficult (College level)"
    else:
        interpretation = "Very Confusing (Professional/Academic graduate level)"

    # 5. Velocity Time Computing Engine (Based on 100% original total_words count)
    reading_metrics = calculate_time_format(total_words, 225)
    speaking_metrics = calculate_time_format(total_words, 150)

    # 6. Advanced SEO Keyword Matrix Engine
    # Comprehensive standard English stop-words to eliminate formatting clutter
    stop_words = {
        "the", "a", "an", "and", "or", "but", "if", "because", "as", "until", "while",
        "of", "at", "by", "for", "with", "about", "against", "between", "into", "through",
        "during", "before", "after", "above", "below", "to", "from", "up", "down", "in",
        "out", "on", "off", "over", "under", "again", "further", "then", "once", "here",
        "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more",
        "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so",
        "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now",
        "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours",
        "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers",
        "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves",
        "is", "am", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having",
        "do", "does", "did", "doing", "would", "could", "should", "ought", "i'm", "you're",
        "he's", "she's", "it's", "we're", "they're", "i've", "you've", "we've", "they've",
        "i'd", "you'd", "he'd", "she'd", "we'd", "they'd", "i'll", "you'll", "he'll", "she'll",
        "we'll", "they'll", "isn't", "aren't", "wasn't", "weren't", "hasn't", "haven't",
        "hadn't", "doesn't", "don't", "didn't", "won't", "wouldn't", "shan't", "shouldn't", "can't"
    }

    # Isolated Filter Layer: Filter stop words AND ensure standalone broken letters (like 'n') are ignored
    filtered_words = [word for word in words if word and word not in stop_words and len(word) > 1]
    
    # Calculate keyword frequency profiles from the isolated filtered list
    word_counts = Counter(filtered_words)
    top_keywords = word_counts.most_common(10)

    # Build final response array using original total_words for accurate density percentage
    keyword_matrix = []
    for keyword, count in top_keywords:
        density_percentage = round((count / total_words) * 100, 2)
        keyword_matrix.append({
            "keyword": keyword,
            "count": count,
            "density_percent": density_percentage
        })

    return {
        "total_paragraphs": total_paragraphs,
        "total_sentences": total_sentences,
        "total_words": total_words,
        "total_syllables": total_syllables,
        "flesch_score": flesch_score,
        "difficulty": interpretation,
        "reading_time": reading_metrics,
        "speaking_time": speaking_metrics,
        "keyword_matrix": keyword_matrix
    }