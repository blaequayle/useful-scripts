import argparse
import textwrap

from openai import OpenAI

from utils import extract_apple_ttml_transcript


def summarize_ttml(episode_number: int) -> str | None:
    """Summarize the podcast transcript from the given TTML file path.
    Requires OPENAI_API_KEY environment variable to be set."""
    print(f"Summarising episode number: {episode_number}")
    transcript = extract_apple_ttml_transcript(f"transcripts/{episode_number}.ttml")
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
    summary = response.choices[0].message.content
    print("Podcast Summary:\n", summary)
    return summary


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("episode_number", type=int)
    args = parser.parse_args()
    summarize_ttml(args.episode_number)


if __name__ == "__main__":
    main()
