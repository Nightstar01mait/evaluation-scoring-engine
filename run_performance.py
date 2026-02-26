from app.services.llm_evaluator import LLMEvaluator
from app.services.performance_analyzer import PerformanceAnalyzer
from app.schemas import EvaluationInput, ExperienceLevel, QuestionType

print("\n=== STARTING FULL SYSTEM TEST ===\n")

evaluator = LLMEvaluator()
evaluations = []

levels = [
    ExperienceLevel.FRESHER,
    ExperienceLevel.INTERMEDIATE,
    ExperienceLevel.ADVANCED
]

for level in levels:
    test_input = EvaluationInput(
        question="Explain OOP concepts",
        candidate_answer="OOP includes encapsulation, inheritance and polymorphism.",
        expected_keywords=["encapsulation", "inheritance", "polymorphism"],
        experience_level=level,
        question_type=QuestionType.TECHNICAL,
        enable_confidence_adjustment=False,
        enable_plagiarism_detection=False,
        enable_multi_turn_context=False
    )

    result = evaluator.evaluate_answer(test_input)
    evaluations.append(result)

    print("--------------")
    print("Experience Level:", level.value)
    print("Technical:", result.scores.technical_accuracy)
    print("Clarity:", result.scores.concept_clarity)
    print("Keyword:", result.scores.keyword_coverage)
    print("Communication:", result.scores.communication)
    print("Final Score:", result.scores.final_score)

# Performance analysis
analyzer = PerformanceAnalyzer()
report = analyzer.analyze(evaluations)

print("\n=== PERFORMANCE REPORT ===")
print(report)

print("\n=== TEST COMPLETE ===")