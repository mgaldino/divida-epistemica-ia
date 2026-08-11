import importlib.util
import tempfile
import unittest
from pathlib import Path


PIPELINE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "pipeline.py"
SPEC = importlib.util.spec_from_file_location("interview_pipeline", PIPELINE_PATH)
PIPELINE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(PIPELINE)


class PipelineUnitTests(unittest.TestCase):
    def test_srt_timestamp(self):
        self.assertEqual(PIPELINE.format_srt_time(0), "00:00:00,000")
        self.assertEqual(PIPELINE.format_srt_time(3661.234), "01:01:01,234")

    def test_clock_timestamp(self):
        self.assertEqual(PIPELINE.format_clock(0), "00:00:00")
        self.assertEqual(PIPELINE.format_clock(3723.9), "01:02:03")

    def test_segment_validation(self):
        valid = [
            {"start": 0.0, "end": 2.0, "text": "Hello."},
            {"start": 2.1, "end": 4.0, "text": "World."},
        ]
        self.assertEqual(PIPELINE.check_segments(valid), [])
        invalid = [{"start": 3.0, "end": 2.0, "text": ""}]
        self.assertGreaterEqual(len(PIPELINE.check_segments(invalid)), 2)

    def test_translation_chunks_respect_time_blocks(self):
        segments = [
            {"start": 1.0, "end": 5.0, "text": "First."},
            {"start": 10.0, "end": 15.0, "text": "Second."},
            {"start": 301.0, "end": 305.0, "text": "Third."},
        ]
        chunks = PIPELINE.translation_chunks(segments, block_seconds=300, max_chars=1000)
        self.assertEqual(len(chunks), 3)
        self.assertEqual(chunks[0]["source_text"], "First.")
        self.assertEqual(chunks[1]["source_text"], "Second.")
        self.assertEqual(chunks[2]["source_text"], "Third.")

    def test_named_speaker_requires_evidence(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "speakers.tsv"
            path.write_text(
                "start_seconds\tend_seconds\tlabel\tconfidence\tevidence\n"
                "0\t10\tAngela\tlow\t\n",
                encoding="utf-8",
            )
            with self.assertRaises(ValueError):
                PIPELINE.load_speaker_annotations(path)

    def test_generic_speaker_is_allowed(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "speakers.tsv"
            path.write_text(
                "start_seconds\tend_seconds\tlabel\tconfidence\tevidence\n"
                "0\t10\tSpeaker 1\tmedium\tvoice cluster\n",
                encoding="utf-8",
            )
            rows = PIPELINE.load_speaker_annotations(path)
            self.assertEqual(rows[0]["label"], "Speaker 1")

    def test_render_english_outputs(self):
        payload = {
            "metadata": {"model": "test-model", "backend": "test-backend"},
            "segments": [
                {"start": 0.0, "end": 2.0, "text": "Hello."},
                {"start": 2.1, "end": 4.0, "text": "World."},
            ],
        }
        old_output = PIPELINE.OUTPUT_DIR
        old_speakers = PIPELINE.SPEAKERS_PATH
        try:
            with tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                PIPELINE.OUTPUT_DIR = root / "outputs"
                PIPELINE.SPEAKERS_PATH = root / "speakers.tsv"
                PIPELINE.render_english_outputs(payload, overwrite=False)
                self.assertEqual(
                    (PIPELINE.OUTPUT_DIR / "transcricao_ingles.txt").read_text(encoding="utf-8"),
                    "Hello.\nWorld.\n",
                )
                srt = (PIPELINE.OUTPUT_DIR / "transcricao_ingles.srt").read_text(encoding="utf-8")
                self.assertIn("00:00:00,000 --> 00:00:02,000", srt)
                markdown = (PIPELINE.OUTPUT_DIR / "transcricao_ingles.md").read_text(encoding="utf-8")
                self.assertIn("## 00:00:00–00:05:00", markdown)
                self.assertIn("Speaker não identificado", markdown)
        finally:
            PIPELINE.OUTPUT_DIR = old_output
            PIPELINE.SPEAKERS_PATH = old_speakers

    def test_network_guards_are_closed_by_default(self):
        self.assertEqual(PIPELINE.main(["download"]), 2)
        self.assertEqual(PIPELINE.main(["run"]), 2)


if __name__ == "__main__":
    unittest.main()
