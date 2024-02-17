import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import glob
from pathlib import Path


def diary_tone():
    analyzer = SentimentIntensityAnalyzer()

    filenames = []
    positivity = []
    negativity = []

    for filename in sorted(glob.glob("diary/*.txt")):
        filepath = Path(filename)
        with open(filepath) as file:
            diary = file.read()
        scores = analyzer.polarity_scores(diary)
        filenames.append(filepath.stem)
        positivity.append(scores["pos"])
        negativity.append(scores["neg"])

    return filenames, positivity, negativity
