# translate-tool
translation helper for i18n

# dependencies

install googletrans python library with: "pip install googletrans==4.0.0-rc1"

# usage

call the script with: "python3 script.py en.json" (the translation file should be on the same folder)
it will prompt the user for the selected language code, then it will start the process of translating and generating a new file with the new translations in the same folder as the script is in.

# improvement ideas

making the translator ignore certain keywords
adding a progress bar instead of printing the translated lines
