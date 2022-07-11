import json
import sys
import googletrans
from googletrans import Translator

def process_data(data, dest):
    for key, value in data.items():
        if isinstance(value, dict): 
            process_data(value, dest)
        else:
            result = translator.translate(value, src='en', dest=dest)
            data[key] = result.text
            print("{0} : {1}".format(key, result.text))
    return data

def main(file, code):
    source_file = open(file, 'r')
    unprocessed_data = json.load(source_file)
    source_file.close()
    print("starting translation...")
    processed_data = process_data(unprocessed_data, code)
    print("translations finished. writing to file...")
    target_file = open(code+'.json', 'w')
    json.dump(processed_data, target_file, indent=4)
    target_file.close()
    print("done writing.")

if __name__ == '__main__':
    translator = Translator()
    selected_language = input("Enter output language code(type 'help' to see all available languages): ")
    if selected_language == 'help':
        print(googletrans.LANGUAGES)
        selected_language = input("Enter output language code: ")
        main(sys.argv[1], selected_language)
    else:
        main(sys.argv[1], selected_language)