from pyfiglet import Figlet
f = Figlet(font='slant')

from PyInquirer import style_from_dict, Token, prompt, Separator
from PyInquirer import Validator, ValidationError
print(f.renderText('Whatsapp -\nspammer'))
print('''
********************************************************
*                                                      *
*    Author: TH3-MA3STRO                               *
*    Instagtam: @th3_MA3STRO                           *
*    GitHub: https://www.github.com/TH3-MA3STRO        *
*    Platform: Linux                                   *
*                                                      *
********************************************************
''')

class NumberValidator(Validator):
    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message='Please enter a number',
                cursor_position=len(document.text))  # Move cursor to end


def styler():
    style = style_from_dict({
        Token.Separator: '#cc5454',
        Token.QuestionMark: '#673ab7 bold',
        Token.Selected: '#cc5454',  # default
        Token.Pointer: '#673ab7 bold',
        Token.Instruction: '',  # default
        Token.Answer: '#f44336 bold',
        Token.Question: '',
    })
    return style


def que1():

    questions = [
        {
            'type': 'list',
            'message': 'Select the type of chat:',
            'name': 'tch',
            'choices': [
                {
                    'name': 'Group'
                },
                {
                    'name': 'Contact'
                }
            ]
        },
        {
            'type': 'input',
            'message': 'Enter the Numer of messages you wish to spam:',
            'name': 'num',
            'validate': NumberValidator
        }
    ]
    answers = prompt(questions, style=styler())
    return answers
