from flask import Flask, render_template, request, url_for
from experta import *
import lab2_program

app = Flask(__name__)


Questions = {
    1: "What will be your primary use for this computer?\n",
    2: "How important is portability for you?\n",
    3: "What kind of software do you intend to use frequently?\n",
    4: "What is your budget for this PC?\n",
}

Answers = {
    1: "1 - Gaming and multimedia production\n"
      "2 - Office work and browsing\n"
      "3 - Graphic design and video editing\n"
      "4 - Programming and development\n",
    2: "1 - Very important, I need it to be lightweight and portable\n"
      "2 - Somewhat important, but performance is my priority\n"
      "3 - Not important, I will mostly use it at home or in the office\n"
      "4 - I don't care much about portability\n",
    3: "1 - Resource-intensive applications like Adobe Creative Suite\n"
      "2 - Office suites like Microsoft Office or Google Workspace\n"
      "3 - Development tools like Visual Studio Code or Android Studio\n"
      "4 - Casual software and internet browsing\n",
    4: "1 - High-end, money is not a concern\n"
      "2 - Mid-range, looking for a balance between performance and price\n"
      "3 - Budget-friendly, looking for the best value for money\n"
      "4 - Very tight, need the cheapest option available\n",
}


@app.route('/')
def index():
    return render_template('index.html', Questions=Questions, Answers=Answers)

@app.route('/recommend', methods=['POST'])
def recommend():
    answers = {}
    for key in Questions:
        answers[key] = request.form.get(str(key))

    KBase = lab2_program.KnowledgeBase()
    KBase.reset()
    for key, value in answers.items():
        KBase.declare(Fact(answ=f'{key}-{value}'))
        KBase.run()

    recommend_config = KBase.recommend_configuration()
    return render_template('recommendation.html', configuration=recommend_config,
                           Questions=Questions, Answers=Answers
                           )


if __name__ == '__main__':
    app.run(debug=True)