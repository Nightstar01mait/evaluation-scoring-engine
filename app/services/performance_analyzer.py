from typing import List
from app.schemas import EvaluationOutput, ExperienceLevel


class PerformanceAnalyzer:

    @staticmethod
    def analyze(evaluations: List[EvaluationOutput], experience_level: ExperienceLevel) -> dict:

        if not evaluations:
            return {"error": "No evaluations provided"}

        total = len(evaluations)

        avg_score = sum(e.scores.final_score for e in evaluations) / total
        tech_avg = sum(e.scores.technical_accuracy for e in evaluations) / total
        clarity_avg = sum(e.scores.concept_clarity for e in evaluations) / total
        keyword_avg = sum(e.scores.keyword_coverage for e in evaluations) / total
        comm_avg = sum(e.scores.communication for e in evaluations) / total

        areas = {
            "technical_accuracy": tech_avg,
            "concept_clarity": clarity_avg,
            "keyword_coverage": keyword_avg,
            "communication": comm_avg
        }

        strongest = max(areas, key=areas.get)
        weakest = min(areas, key=areas.get)

        # Experience-based overall threshold
        passing_threshold = {
            "fresher": 5.0,
            "intermediate": 6.0,
            "advanced": 7.0
        }.get(experience_level.value, 5.0)

        overall_passed = avg_score >= passing_threshold

        # Collect suggestions
        all_suggestions = []
        for e in evaluations:
            for s in e.suggestions:
                if s not in all_suggestions:
                    all_suggestions.append(s)

        return {
            "average_score": round(avg_score, 2),
            "strongest_area": strongest,
            "weakest_area": weakest,
            "total_questions": total,
            "overall_passed": overall_passed,
            "passing_threshold": passing_threshold,
            "suggestions": all_suggestions
        }