from typing import List
from app.schemas import EvaluationOutput

class PerformanceAnalyzer:

    @staticmethod
    def analyze(evaluations: List[EvaluationOutput]) -> dict:
        if not evaluations:
            return {"error": "No evaluations provided"}

        total = len(evaluations)

        avg_score = sum(e.scores.final_score for e in evaluations) / total
        tech_avg = sum(e.scores.technical_accuracy for e in evaluations) / total
        clarity_avg = sum(e.scores.concept_clarity for e in evaluations) / total
        keyword_avg = sum(e.scores.keyword_coverage for e in evaluations) / total
        comm_avg = sum(e.scores.communication for e in evaluations) / total

        strongest = max({
            "technical_accuracy": tech_avg,
            "concept_clarity": clarity_avg,
            "keyword_coverage": keyword_avg,
            "communication": comm_avg
        }, key=lambda x: {
            "technical_accuracy": tech_avg,
            "concept_clarity": clarity_avg,
            "keyword_coverage": keyword_avg,
            "communication": comm_avg
        }[x])

        weakest = min({
            "technical_accuracy": tech_avg,
            "concept_clarity": clarity_avg,
            "keyword_coverage": keyword_avg,
            "communication": comm_avg
        }, key=lambda x: {
            "technical_accuracy": tech_avg,
            "concept_clarity": clarity_avg,
            "keyword_coverage": keyword_avg,
            "communication": comm_avg
        }[x])

        return {
            "average_score": round(avg_score, 2),
            "strongest_area": strongest,
            "weakest_area": weakest,
            "total_questions": total
        }