from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Iterable, List, Optional, Sequence
import xml.etree.ElementTree as ET

import requests


PUBMED_BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"


@dataclass
class PubMedPaper:
    pmid: str
    title: str
    abstract: str
    journal: str
    pub_year: Optional[str]
    authors: List[str]
    authors_total: int
    affiliations: List[str]
    link: str

    def to_dict(self) -> dict:
        return asdict(self)


class PubMedClient:
    def __init__(self, api_key: Optional[str] = None, session: Optional[requests.Session] = None) -> None:
        self.api_key = api_key.strip() if api_key else None
        self.session = session or requests.Session()

    def search_pmids(self, query: str, *, days: int = 7, retmax: int = 40) -> List[str]:
        params = {
            "db": "pubmed",
            "term": query,
            "retmax": retmax,
            "sort": "pub+date",
            "reldate": days,
            "retmode": "json",
        }
        if self.api_key:
            params["api_key"] = self.api_key
        resp = self.session.get(f"{PUBMED_BASE_URL}/esearch.fcgi", params=params, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        return data.get("esearchresult", {}).get("idlist", [])

    def fetch_details(self, pmids: Sequence[str]) -> List[PubMedPaper]:
        if not pmids:
            return []
        params = {
            "db": "pubmed",
            "id": ",".join(pmids),
            "retmode": "xml",
        }
        if self.api_key:
            params["api_key"] = self.api_key
        resp = self.session.get(f"{PUBMED_BASE_URL}/efetch.fcgi", params=params, timeout=60)
        resp.raise_for_status()
        root = ET.fromstring(resp.content)
        papers: List[PubMedPaper] = []
        for article in root.findall(".//PubmedArticle"):
            parsed = self._parse_article(article)
            if parsed:
                papers.append(parsed)
        return papers

    def get_recent_papers(self, query: str, *, days: int = 7, retmax: int = 40) -> List[PubMedPaper]:
        pmids = self.search_pmids(query, days=days, retmax=retmax)
        return self.fetch_details(pmids)

    def _parse_article(self, article: ET.Element) -> Optional[PubMedPaper]:
        art = article.find(".//Article")
        if art is None:
            return None
        title = self._get_text(art.find("ArticleTitle"))
        abstract = self._join_texts(art.findall(".//AbstractText"))
        journal = self._get_text(art.find(".//Journal/Title"))
        pub_year = self._extract_year(art.find(".//JournalIssue/PubDate"))
        pmid_el = article.find(".//PMID")
        pmid = self._get_text(pmid_el)
        link = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/" if pmid else ""
        author_elements = art.findall(".//Author")
        authors, authors_total = self._extract_authors(author_elements)
        affiliations = self._extract_affiliations(author_elements)
        return PubMedPaper(
            pmid=pmid,
            title=title,
            abstract=abstract,
            journal=journal,
            pub_year=pub_year,
            authors=authors,
            authors_total=authors_total,
            affiliations=affiliations,
            link=link,
        )

    @staticmethod
    def _get_text(el: Optional[ET.Element]) -> str:
        return el.text.strip() if el is not None and el.text else ""

    @staticmethod
    def _join_texts(elements: Iterable[ET.Element]) -> str:
        return "\n".join(
            [el.text.strip() for el in elements if el is not None and el.text]
        )

    @staticmethod
    def _extract_year(pub_date: Optional[ET.Element]) -> Optional[str]:
        if pub_date is None:
            return None
        year = pub_date.find("Year")
        if year is not None and year.text:
            return year.text.strip()
        medline = pub_date.find("MedlineDate")
        if medline is not None and medline.text:
            return medline.text.strip().split(" ")[0]
        return None

    @staticmethod
    def _author_name(author: ET.Element) -> str:
        collective = author.findtext("CollectiveName", default="").strip()
        if collective:
            return collective
        last = author.findtext("LastName", default="")
        fore = author.findtext("ForeName", default="")
        full = " ".join(part for part in [fore.strip(), last.strip()] if part)
        return full.strip()

    @classmethod
    def _extract_authors(
        cls,
        author_elements: Iterable[ET.Element],
        max_authors: int = 3,
    ) -> tuple[List[str], int]:
        all_authors: List[str] = []
        for author in author_elements:
            name = cls._author_name(author)
            if name:
                all_authors.append(name)
        total = len(all_authors)
        return all_authors[:max_authors], total

    @staticmethod
    def _extract_affiliations(
        author_elements: Iterable[ET.Element],
        *,
        max_affiliations: int = 5,
    ) -> List[str]:
        seen: set[str] = set()
        affiliations: List[str] = []
        for author in author_elements:
            for aff in author.findall(".//AffiliationInfo/Affiliation"):
                text = (aff.text or "").strip()
                if not text:
                    continue
                if text in seen:
                    continue
                seen.add(text)
                affiliations.append(text)
                if len(affiliations) >= max_affiliations:
                    return affiliations
        return affiliations


__all__ = ["PubMedClient", "PubMedPaper"]
