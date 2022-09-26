"""
Developer: @skywalkerSam
Purpose: Text To Speech Generator...
Date: 12022.09.25.22:19:00

"""

from logging import exception
import pyttsx3 as pt3


print("""
                #########################################################
                        ****    Text To Speech Generator    ****
                #########################################################
                
""")

user_text = input("Enter The Text (Ex; hello world): ")
user_rate = input("\nEnter Speech Rate (default=200): ")

# Voice Engine...
engine = pt3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', user_rate)


def text_to_speech():
    engine.say(user_text)
    engine.runAndWait()


def confirmation():
    print(f"\nVoice Generated: {user_text} \nVoice Rate: {user_rate} \n")


def save_voice():
    file_name = input("\n\t Enter the filename: ")
    engine.save_to_file(user_text, file_name + ".mp3")
    engine.runAndWait()


if __name__ == '__main__':
    while True:
        try:
            text_to_speech()
            confirmation()
            proceed = input("Would you like to save current voice as an audio file (Y/N): ").lower()
            if proceed == 'y':
                try:
                    save_voice()
                    print("\n\n\t Voice saved successfully :) \n".upper())
                    break
                except:
                    print("\n\t Something went wrong! Please try again :(\n")
                    continue
            elif proceed == 'n':
                break
            else:
                print("\n\t Please select a valid option & try again :( \n")
                continue
        except KeyboardInterrupt:
            print("\n\n\n\tOperation cancelled by the user ;(\n\n")
            break
        except ValueError:
            print("\n\t Please fill the required information carefully ;(\n")
            continue
        except exception as e:
            print(e)
            print("\n\t Something went wrong! Please try again :(\n")
            continue
