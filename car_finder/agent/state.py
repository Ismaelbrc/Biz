"""Graph state shared between all nodes."""
from typing import TypedDict, Optional


class SearchState(TypedDict):
    locations:     list[dict]
    filters:       dict
    raw_cars:      list[dict]
    enriched:      list[dict]
    scored:        list[dict]
    opportunities: list[dict]
    report_html:   Optional[str]
    report_json:   Optional[str]
    stats:         dict
    errors:        list[str]
