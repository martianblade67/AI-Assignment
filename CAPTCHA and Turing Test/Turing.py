import random

QUESTIONS = [
    ("Color of the sky?", ["blue"]),
    ("Legs on a dog?", ["4", "four"]),
    ("What do you write with?", ["pen", "pencil"]),
    ("Day after Monday?", ["tuesday"]),
    ("Is water wet? (yes/no)", ["yes"]),
]




def run_turing_test(n=3):
    questions = random.sample(QUESTIONS, n)
    score = sum(input(f"{q}\n> ").strip().lower() in a for q, a in questions)
    print(f"Score: {score}/{n}")
    print("Passed!" if score == n else "Failed!")
    return score == n




if __name__ == "__main__":
    run_turing_test()