

# Hide INFO logs for cleaner output
import logging

logging.basicConfig(level=logging.ERROR)

logging.getLogger("app.services.json_enforcer").setLevel(logging.ERROR)
logging.getLogger("app.services.llm_evaluator").setLevel(logging.ERROR)
logging.getLogger("app.services.context_manager").setLevel(logging.ERROR)
logging.getLogger("app.services.confidence_adjuster").setLevel(logging.ERROR)
logging.getLogger("app.services.plagiarism_detector_simple").setLevel(logging.ERROR)
from app.services.llm_evaluator import LLMEvaluator
from app.services.performance_analyzer import PerformanceAnalyzer
from app.schemas import EvaluationInput, ExperienceLevel, QuestionType


def main():

    evaluator = LLMEvaluator()
    analyzer = PerformanceAnalyzer()

    evaluations = []

    experience = ExperienceLevel.INTERMEDIATE

    test_cases = [

        {
            "question": "Explain Object Oriented Programming",
            "answer": "Object oriented programming includes encapsulation, inheritance and polymorphism.",
            "type": QuestionType.TECHNICAL,
            "keywords": [
                "object",
                "class",
                "encapsulation",
                "inheritance",
                "polymorphism",
                "abstraction"
            ]
        },

        {
            "question": "Describe a challenge you faced in a project",
            "answer": "During my project we faced database performance issues and solved them using indexing and optimization.",
            "type": QuestionType.BEHAVIORAL,
            "keywords": [
                "problem",
                "challenge",
                "solution",
                "team",
                "communication",
                "project"
            ]
        },

        {
            "question": "Design a URL shortener system",
            "answer": "A URL shortener maps long URLs to short unique IDs stored in a database and uses hashing for generating short links.",
            "type": QuestionType.SYSTEM_DESIGN,
            "keywords": [
                "database",
                "hashing",
                "short url",
                "mapping",
                "scalability",
                "caching",
                "api"
            ]
        },

        {
            "question": "Write Python code to reverse a string",
            "answer": "def reverse_string(s): return s[::-1]",
            "type": QuestionType.CODING,
            "keywords": [
                "python",
                "function",
                "string",
                "slice",
                "algorithm"
            ]
        },

        {
            "question": "What is Machine Learning?",
            "answer": "Machine learning is a subset of artificial intelligence where algorithms learn patterns from data.",
            "type": QuestionType.CONCEPTUAL,
            "keywords": [
                "machine learning",
                "artificial intelligence",
                "data",
                "algorithm",
                "model",
                "training"
            ]
        }
    ]

    for case in test_cases:

        test_input = EvaluationInput(
            question=case["question"],
            candidate_answer=case["answer"],
            expected_keywords=case["keywords"],
            experience_level=experience,
            question_type=case["type"],
            interview_id="test_interview",
            context=None,
            max_score=10,
            time_taken=30,
            enable_confidence_adjustment=False,
            enable_plagiarism_detection=False,
            enable_multi_turn_context=False
        )

        result = evaluator.evaluate_answer(test_input)

        print("\n===== QUESTION TEST =====")

        print("Question:", case["question"])
        print("Type:", case["type"].value)
        print("Score:", result.scores.final_score)
        print("Passed:", result.passed)

        print("\nSuggestions:")

        for s in result.suggestions:
            print("-", s)

        evaluations.append(result)

    report = analyzer.analyze(evaluations, experience)

    print("\n===== PERFORMANCE REPORT =====")

    print("Average Score:", report["average_score"])
    print("Passing Threshold:", report["passing_threshold"])
    print("Overall Result:", "PASSED" if report["overall_passed"] else "FAILED")

    print("Strongest Area:", report["strongest_area"])
    print("Weakest Area:", report["weakest_area"])
    print("Total Questions:", report["total_questions"])

    print("\nOverall Suggestions:")

    for s in report["suggestions"]:
        print("-", s)


if __name__ == "__main__":
    main()