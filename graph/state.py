from typing import TypedDict, List
class AgentState(TypedDict):
# Task is user input 
    task: str
# Plan by planner agent 
    plan: str
# Generated by Generator Agent
    generated: str
# Documents by Researcher Agent 
    content: List[str]
# Grading score by Grader Agent
    grading_score: int
# Final review & hellucination score by Reviewer Agent
    final_review: str
    hellucination_score: int
# Search number and max searches for Researcher Agent
    search_number: int
    max_searches: int
# Amount of generations throughout workflow with a limit 
    revision_number: int
    max_revisions: int