import textwrap

from openai import OpenAI

from utils import extract_apple_ttml_transcript


def summarize_ttml(path: str) -> str:
    """Summarize the podcast transcript from the given TTML file path.
    Requires OPENAI_API_KEY environment variable to be set."""
    transcript = extract_apple_ttml_transcript(path)
    client = OpenAI()
    prompt = textwrap.dedent(f"""
        You are a podcast summarizer.
        Summarize the following transcript into 3-4 key areas, each with 2-3 bullet points.
        Focus on practical takeaways i.e. dos and don'ts, tips.
        Do not add anything that is not in the transcript.
        Do not summarise topics unrelated to waste, reuse, recycling.
        Transcript:
        {transcript}
    """)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    summary = summarize_ttml("transcripts/73.ttml")
    print("Podcast Summary:\n", summary)
