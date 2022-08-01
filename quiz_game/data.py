question_Data_Gk = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {
        "text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home "
                "to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.",
     "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]


question_Data_Cartoon = [
    {"text": "Oggy's brother's name is Jack. ", "answer": "True"},
    {"text": "Nobita likes Sijuka.", "answer": "True"},
    {"text": "[HARD] Shin-chan will be 30 yrs old after 30 yrs from now.", "answer": "False"},
    {"text": "Tom wants get married to Jerry.", "answer": "False"},
    {"text": "Doremon is a dog.", "answer": "False"},
    {"text": "Shin-chan has a baby sister.", "answer": "True"},
    {"text": "Minions are pink in color.", "answer": "False"},
    {"text": "Courage the cowardly dog is actually Brave.", "answer": "True"},
    {"text": "Shin chan falls in love everytime with different girls but not of his age ( all greater>his age )",
     "answer": "True"},
    {"text": "Popeye the sailer man eats Vimal pan masala when he wants to get powerful.", "answer": "False"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}

]


class Question:
    # we create object of question class and store that object in the quest list
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


# noinspection PyBroadException
try:
    # Try catch exception handling concepts are used when the devices is offline thus there are two datasets
    class Return_Question_Bank:
        def __init__(self, category):
            print(category)
            obj = Question_Api()
            obj.category_selection(category=category)
            # print(obj.data['results'][0]['question'])

            self.quest = []
            for i in range(0, 10):
                self.quest.append(
                    Question(obj.data['results'][i]['question'], obj.data['results'][i]['correct_answer']))


    import json
    from urllib.request import urlopen


    class Question_Api:

        def __init__(self, category='film'):
            """
                :param category: which categories of questions you choose
                """

            self.question_bank = None
            self.api_Link = "https://opentdb.com/api.php?amount=10&category=10&difficulty=easy&type=boolean"
            self.data = None
            self.category = category

        def category_selection(self, category='film'):
            """

                :param category: category is given when user selects it from UI
                :return:
                """
            self.category = category
            if self.category == 'Gk':
                self.api_Link = "https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=boolean"

            elif self.category == 'Animal':
                self.api_Link = "https://opentdb.com/api.php?amount=10&category=27&difficulty=easy&type=boolean"

            elif self.category == 'Science':
                self.api_Link = "https://opentdb.com/api.php?amount=10&category=17&difficulty=easy&type=boolean"


            # elif self.category == 'Cartoon':
            #     self.api_Link = "https://opentdb.com/api.php?amount=10&category=32&difficulty=easy&type=boolean"

            try:
                webpage = urlopen(self.api_Link)
                self.data = json.load(webpage)
                self.data_preprocessing()
            except Exception as e:
                Offline_Dataset()
                print(e)



        def data_preprocessing(self):
            """
                here data preprocessing is done of the question as it contains html format types insteed of apostropies

                question ank is the list of object of the distionary of the data set
                :return: None
                """
            self.question_bank = []
            for i in range(0, 10):
                text1 = self.data['results'][i]['question'].replace("&quot;", "''")
                #
                text = text1.replace("&#039;", "'")
                self.data['results'][i]['question'] = text


# noinspection PyBroadException
except Exception:
    print("exception")


class Offline_Dataset:
    def __init__(self, offline_Type='Cartoon'):
        print("exception occured")
        self.quest = []
        self.offline_Type = offline_Type
        self.set_question_dataset()

    def get_quest(self):
        return self.quest

    def set_question_dataset(self):
        print(self.offline_Type)
        if self.offline_Type == "Gk":
            for i in range(0, 10):
                self.quest.append(Question(question_Data_Gk[i]["text"], question_Data_Gk[i]["answer"]))

        elif self.offline_Type == "Cartoon":
            for i in range(0, 10):
                self.quest.append(Question(question_Data_Cartoon[i]["text"], question_Data_Cartoon[i]["answer"]))


