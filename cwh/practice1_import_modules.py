# import pyjokes
# joke= pyjokes.get_joke()
# print(joke)


# #text to speech module

# import pyttsx3
# engine = pyttsx3.init()
# # engine.say("muchas gracias aficion esta para vosotros  siuuuuuuuuuuu ")
# engine.say("terii maa ki chu")
# engine.runAndWait()


# directory listing using OS module
import os

def print_directory_contents(path='C:/Users/vishv'):
    try:
        # Use os.scandir to iterate over directory entries
        with os.scandir(path) as entries:
            for entry in entries:
                print(entry.name)
    except FileNotFoundError:
        print(f"The directory {path} does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory {path}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
print_directory_contents()  # Prints contents of the current directory
# print_directory_contents('/path/to/directory')  # Prints contents of a specified directory


