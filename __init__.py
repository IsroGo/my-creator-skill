from mycroft import MycroftSkill, intent_file_handler


class MyCreator(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('creator.my.intent')
    def handle_creator_my(self, message):
        self.speak_dialog('creator.my')


def create_skill():
    return MyCreator()

