def calculate_risk(answers, questions):
    """
    answers: dict like {"q1": "Yes", "q2": "No", ...}
    questions: list loaded from risk_questions.json
    Returns: (total_score, max_score, risk_level, flagged_habits)
    """
    total_score = 0
    max_score = 0
    flagged_habits = []

    for q in questions:
        qid = q["id"]
        weight_map = q["weight"]
        max_score += max(weight_map.values())

        user_answer = answers.get(qid)
        if user_answer is not None:
            score = weight_map.get(user_answer, 0)
            total_score += score
            if score == max(weight_map.values()) and score > 0:
                flagged_habits.append(q["flag"])

    if max_score == 0:
        percentage = 0
    else:
        percentage = (total_score / max_score) * 100

    if percentage < 30:
        risk_level = "Low Risk"
    elif percentage < 60:
        risk_level = "Moderate Risk"
    else:
        risk_level = "High Risk"

    return total_score, max_score, risk_level, flagged_habits