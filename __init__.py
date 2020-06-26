from mycroft import MycroftSkill, intent_file_handler


class IntroducingJarvis(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('jarvis.introducing.intent')
    def handle_jarvis_introducing(self, message):
        self.speak_dialog('jarvis.introducing')


def create_skill():
    return IntroducingJarvis()

