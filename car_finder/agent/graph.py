"""
LangGraph definition for the car opportunity finder.

Graph:
  START ──► scrape ──► fipe ──► score ──► report ──► END
"""
from langgraph.graph import StateGraph, END

from agent.state import SearchState
from agent.nodes import scrape_node, fipe_node, score_node, report_node


def build_graph():
    g = StateGraph(SearchState)

    g.add_node("scrape", scrape_node)
    g.add_node("fipe",   fipe_node)
    g.add_node("score",  score_node)
    g.add_node("report", report_node)

    g.set_entry_point("scrape")
    g.add_edge("scrape", "fipe")
    g.add_edge("fipe",   "score")
    g.add_edge("score",  "report")
    g.add_edge("report", END)

    return g.compile()
