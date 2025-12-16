import xml.etree.ElementTree as ET


def extract_apple_ttml_transcript(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    # namespaces used in the document
    ns = {
        "ttml": "http://www.w3.org/ns/ttml",
        "podcasts": "http://podcasts.apple.com/transcript-ttml-internal",
        "ttm": "http://www.w3.org/ns/ttml#metadata",
    }

    transcript_sentences = []

    # Find sentence-level spans
    sentence_spans = root.findall('.//ttml:span[@podcasts:unit="sentence"]', ns)

    for sentence in sentence_spans:
        words = []
        for word in sentence.findall('.//ttml:span[@podcasts:unit="word"]', ns):
            if word.text:
                words.append(word.text)
        transcript_sentences.append(" ".join(words))

    # Only keep content after the "Additions and Corrections" marker sentence
    marker = "additions and corrections"
    for idx, text in enumerate(transcript_sentences):
        if marker in text.lower():
            transcript_sentences = transcript_sentences[idx + 1 :]
            break

    return "\n".join(transcript_sentences)


if __name__ == "__main__":
    print(extract_apple_ttml_transcript("transcripts/72.ttml"))
