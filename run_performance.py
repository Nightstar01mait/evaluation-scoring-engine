from app.services.llm_evaluator import LLMEvaluator
from app.services.performance_analyzer import PerformanceAnalyzer
from app.schemas import EvaluationInput, ExperienceLevel, QuestionType

evaluator = LLMEvaluator()

evaluations = []

test_cases = [

    {
        "question": "Explain Object Oriented Programming",
        "answer": "Object oriented programming includes encapsulation, inheritance and polymorphism.",
        "type": QuestionType.TECHNICAL
    },

    {
        "question": "Describe a challenge you faced in a project",
        "answer": "In my project we had performance issues in database queries which we solved using indexing.",
        "type": QuestionType.BEHAVIORAL
    },

    {
        "question": "Design a URL shortener system",
        "answer": "A URL shortener system uses a database to map short URLs to long URLs and uses hashing to generate unique IDs.",
        "type": QuestionType.SYSTEM_DESIGN
    },

    {
        "question": "Write Python code to reverse a string",
        "answer": "def reverse_string(s): return s[::-1]",
        "type": QuestionType.CODING
    },

    {
        "question": "What is Machine Learning?",
        "answer": "Machine learning is a subset of artificial intelligence where systems learn patterns from data.",
        "type": QuestionType.CONCEPTUAL
    }

]

for case in test_cases:

    test_input = EvaluationInput(
        question=case["question"],
        candidate_answer=case["answer"],
        expected_keywords=[
            "encapsulation",
            "inheritance",
            "polymorphism",
            "database",
            "machine learning"
        ],
        experience_level=ExperienceLevel.INTERMEDIATE,
        question_type=case["type"],
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


# Performance report
analyzer = PerformanceAnalyzer()
report = analyzer.analyze(evaluations)

print("\n===== FINAL PERFORMANCE REPORT =====")
print("Average Score:", report["average_score"])
print("Strongest Area:", report["strongest_area"])
print("Weakest Area:", report["weakest_area"])
print("Total Questions:", report["total_questions"])