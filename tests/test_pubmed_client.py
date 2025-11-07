from pathlib import Path
import sys

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from pubmed_client import PubMedClient, PubMedPaper


FIXTURE_DIR = Path(__file__).parent / "fixtures"


class StubResponse:
    def __init__(self, *, json_data=None, content: bytes = b"", status_code: int = 200):
        self._json = json_data or {}
        self.content = content
        self.status_code = status_code

    def json(self):
        return self._json

    def raise_for_status(self):
        if self.status_code >= 400:
            raise RuntimeError(f"HTTP {self.status_code}")


class StubSession:
    def __init__(self):
        self.requests = []
        self._queue = []

    def queue_response(self, response: StubResponse):
        self._queue.append(response)

    def get(self, url, params=None, timeout=None):
        self.requests.append({"url": url, "params": params})
        if not self._queue:
            raise AssertionError("No queued responses left")
        return self._queue.pop(0)


@pytest.fixture()
def sample_xml() -> bytes:
    return (FIXTURE_DIR / "pubmed_sample.xml").read_bytes()


def test_search_pmids_returns_id_list():
    session = StubSession()
    session.queue_response(StubResponse(json_data={"esearchresult": {"idlist": ["1", "2"]}}))
    client = PubMedClient(api_key=None, session=session)
    ids = client.search_pmids("ct", days=3, retmax=5)
    assert ids == ["1", "2"]
    assert session.requests[0]["params"]["reldate"] == 3
    assert session.requests[0]["params"]["retmax"] == 5


def test_fetch_details_parses_minimal_fields(sample_xml):
    session = StubSession()
    session.queue_response(StubResponse(content=sample_xml))
    client = PubMedClient(session=session)
    papers = client.fetch_details(["123", "456"])
    assert len(papers) == 2

    first = papers[0]
    assert isinstance(first, PubMedPaper)
    assert first.pmid == "12345678"
    assert first.title == "Deep Learning for CT Segmentation"
    assert "First abstract" in first.abstract
    assert first.journal == "Radiology AI Journal"
    assert first.pub_year == "2025"
    assert first.authors == ["Taro Sato", "Hanako Tanaka"]
    assert first.link.endswith("12345678/")

    second = papers[1]
    assert second.pub_year == "2024"
    assert len(second.authors) == 3  # clipped to 3
