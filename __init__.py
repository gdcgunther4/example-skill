from mycroft import MycroftSkill, intent_file_handler


class Example(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('example.intent')
    def handle_example(self, message):
        self.speak_dialog('example')


def create_skill():
    return Example()

