import pathlib
import unittest

from utils import extract_apple_ttml_transcript


class TestExtractAppleTTMLTranscriptIntegration(unittest.TestCase):
    def test_truncates_after_additions_and_corrections(self):
        fixture_path = (
            pathlib.Path(__file__).parent / "sample_additions_and_corrections.ttml"
        )
        output = extract_apple_ttml_transcript(str(fixture_path))
        expected = "\n".join(
            [
                "Correction one: we misstated the date.",
                "Addition two: new resource link posted.",
            ]
        )
        self.assertEqual(output, expected)
