from experta import *


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


class KnowledgeBase(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        # Confidence measures
        self.performance_confidence = 0
        self.portability_confidence = 0
        self.budget_confidence = 0

    @Rule(Fact(answ="1-1") | Fact(answ="2-1") | Fact(answ="3-1") | Fact(answ="4-1"))
    def gaming_multimedia(self):
        self.performance_confidence += 0.3

    @Rule(Fact(answ="1-2") | Fact(answ="2-2") | Fact(answ="3-2") | Fact(answ="4-2"))
    def office_browsing(self):
        self.portability_confidence += 0.2

    @Rule(Fact(answ="1-3") | Fact(answ="2-3") | Fact(answ="3-3") | Fact(answ="4-3"))
    def graphic_design_video_editing(self):
        self.performance_confidence += 0.2

    @Rule(Fact(answ="1-4") | Fact(answ="2-4") | Fact(answ="3-4") | Fact(answ="4-4"))
    def programming_development(self):
        self.performance_confidence += 0.1

    @Rule(Fact(answ="2-1") | Fact(answ="3-1") | Fact(answ="4-1"))
    def very_important_portability(self):
        self.portability_confidence += 0.3

    @Rule(Fact(answ="2-2") | Fact(answ="3-2") | Fact(answ="4-2"))
    def somewhat_important_portability(self):
        self.portability_confidence += 0.2

    @Rule(Fact(answ="2-3") | Fact(answ="3-3") | Fact(answ="4-3"))
    def not_important_portability(self):
        self.portability_confidence += 0.1

    @Rule(Fact(answ="1-1") | Fact(answ="1-2") | Fact(answ="1-3") | Fact(answ="1-4"))
    def high_end_budget(self):
        self.budget_confidence += 0.3

    @Rule(Fact(answ="2-1") | Fact(answ="2-2") | Fact(answ="2-3") | Fact(answ="2-4"))
    def mid_range_budget(self):
        self.budget_confidence += 0.2

    @Rule(Fact(answ="3-1") | Fact(answ="3-2") | Fact(answ="3-3") | Fact(answ="3-4"))
    def budget_friendly(self):
        self.budget_confidence += 0.1

    def recommend_configuration(self):
        if self.performance_confidence > self.portability_confidence and self.performance_confidence > self.budget_confidence:
            return "High-performance PC"
        elif self.portability_confidence > self.performance_confidence and self.portability_confidence > self.budget_confidence:
            return "Portable PC"
        elif self.budget_confidence > self.performance_confidence and self.budget_confidence > self.portability_confidence:
            return "Budget-friendly PC"
        else:
            return "Balanced PC"



KBase = KnowledgeBase()
KBase.reset()

for question_key in Questions:
    # print(Questions[question_key])
    # user_input = input(Answers[question_key])
    # answer = str(question_key) + "-" + user_input
    # KBase.declare(Fact(answ=answer))
    KBase.run()

recommended_configuration = KBase.recommend_configuration()
# print("Recommended PC configuration: " + recommended_configuration)

# print(Questions[1])
# print(Questions[2])