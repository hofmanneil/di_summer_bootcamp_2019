import json
import random
def generate_quiz():
    operators_list = ["+", "-", "/","*"]
    quiz = {}
    for level in range(1,11):
        key_level = "quiz math level" + " " + str(level)
        quiz[key_level] = {}
    # print(quiz)

        for question_num in range(1,11):
            question_key = "q" + str(question_num)
            quiz[key_level][question_key] = {}
            num_1 = random.randrange(level, 10*level)
            num_2 = random.randrange(level, 10*level)
            operator = random.choice(operators_list)
            if operator == "+":
                answer = num_1 + num_2
            elif operator == "-":
                answer = num_1 - num_2
            elif operator == "/":
                answer = num_1 / num_2
            elif operator == "*":
                answer = num_1 * num_2


            options = []
            for i in range(3):
                option = str(random.randrange(level, 10*level))
                while option in options:
                    option = str(random.randrange(level, 10*level))
                options.append(option)

            options.append(str(answer))
            random.shuffle(options)

            quiz[key_level][question_key]["question"] = str(num_1) + " " + operator + " " + str(num_2) + " = ?"
            quiz[key_level][question_key]["options"] = options
            quiz[key_level][question_key]["answer"] = str(answer)
    return quiz

# f = open("quiz.json", "w")
# f.write(json.dumps(quiz))
# f.close()


def random_question(input_level):

    question_level=quiz["quiz math level "+str(input_level)]
    question_number='q'+str(random.randrange(1,11))
    question=question_level[question_number]['question']
    options=question_level[question_number]['options']
    options = options[0] + "," + options[1] + "," + options[2] + "," + options[3]
    answer=question_level[question_number]['answer']

    message = "question: {}\noptions: {}\nanswer: {}\n".format(question, options, answer)
    return message



quiz=generate_quiz()
for i in range(1,5):
    print("Question {}:".format(i))
    q=random_question(3)
    print(q)