from rich.console import Console

console=Console()

Qs=[
    ("what is your favorite color", ["A: purple" , "B: red","c: yellow","D:blue"],"A"),
    ("what do you do for living", ["A:doctor","B:engineer","c:business","D:lawer"],"B"),
    ("what is your favorite food",["A:pizza","B:salad","C:pasta","D:stake"],"C"),

]
score=0
index=1
NORMAL_SCORE=10
HIGH_SCORE=20
PENALTY=3
correct_answers=0
for Q,answers,correct in Qs:
    console.print(Q, style ="red on white")
    for answer in answers:
        console.print(f"{answer}\n", style="green")
    user_answer=input("Your answer (A/B/C/D):").strip().upper()
    if user_answer==correct:
        correct_answers+=1
        if index==len(Qs):
            score+= HIGH_SCORE
        else:
         score += NORMAL_SCORE
        console.print("correct/n")
    else:
        score-=PENALTY
        console.print(f"wrong The correct answer is {correct}.\n")
    index+=1
console.print(f"your final score is {score}")
console.print(f"your final percentage is :{correct_answers / len(Qs) * 100}")




