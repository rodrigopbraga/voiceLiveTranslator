Voice Live Translator

This Python script listens to your microphone input, recognizes speech, translates it to the desired language using Google Translate, and plays back the translated speech. It utilizes various libraries such as speech_recognition, google_trans_new, gtts, langdetect, and playsound.
Features

    . Listens to microphone input for speech recognition.
    . Detects the language of the recognized speech.
    . Translates the speech to the desired language using Google Translate.
    . Generates speech output in the translated language using text-to-speech (TTS) technology.
    . Plays back the translated speech.

How to Use

    . Ensure you have Python installed on your system.
    . Install the required libraries by running:
      pip install SpeechRecognition
      pip install google-trans-new
      pip install gtts
      pip install langdetect
      pip install playsound==1.2.2

Run the script by executing the following command in your terminal or command prompt:

    voiceLiveTranlator.py

    Speak into your microphone. The script will recognize your speech, translate it to the desired language, and play back the translated speech.


Here follows a list of languages supported and their index:

    'af': 'afrikaans', 'sq': 'albanian ','am': 'amharic ','ar': 'arabic ','hy': 'armenian ','az': 'azerbaijani ',
    'eu': 'basque ','be': 'belarusian ','bn': 'bengali ','bs': 'bosnian ','bg': 'bulgarian ','ca': 'catalan ',
    'ceb': 'cebuano ','ny': 'chichewa ','zh-cn': 'chinese (simplified) ','zh-tw': 'chinese (traditional) ',
    'co': 'corsican ','hr': 'croatian ','cs': 'czech ','da': 'danish ','nl': 'dutch ','en': 'english ',
    'eo': 'esperanto ','et': 'estonian ','tl': 'filipino ','fi': 'finnish ','fr': 'french ','fy': 'frisian ',
    'gl': 'galician ','ka': 'georgian ','de': 'german ','el': 'greek ','gu': 'gujarati ','ht': 'haitian creole ',
    'ha': 'hausa ','haw': 'hawaiian ','iw': 'hebrew ','he': 'hebrew ','hi': 'hindi ','hmn': 'hmong ','hu': 'hungarian ',
    'is': 'icelandic ','ig': 'igbo ','id': 'indonesian ','ga': 'irish ','it': 'italian ','ja': 'japanese ',
    'jw': 'javanese ','kn': 'kannada ','kk': 'kazakh ','km': 'khmer ','ko': 'korean ','ku': 'kurdish (kurmanji) ',
    'ky': 'kyrgyz ','lo': 'lao ','la': 'latin ','lv': 'latvian ','lt': 'lithuanian ','lb': 'luxembourgish ',
    'mk': 'macedonian ','mg': 'malagasy ','ms': 'malay ','ml': 'malayalam ','mt': 'maltese ','mi': 'maori ',
    'mr': 'marathi ','mn': 'mongolian ','my': 'myanmar (burmese) ','ne': 'nepali ','no': 'norwegian ','or': 'odia ',
    'ps': 'pashto ','fa': 'persian ','pl': 'polish ','pt': 'portuguese ','pa': 'punjabi ','ro': 'romanian ',
    'ru': 'russian ','sm': 'samoan ','gd': 'scots gaelic ','sr': 'serbian ','st': 'sesotho ','sn': 'shona ',
    'sd': 'sindhi ','si': 'sinhala ','sk': 'slovak ','sl': 'slovenian ','so': 'somali ','es': 'spanish ',
    'su': 'sundanese ','sw': 'swahili ','sv': 'swedish ','tg': 'tajik ','ta': 'tamil ','te': 'telugu ','th': 'thai ',
    'tr': 'turkish ','uk': 'ukrainian ','ur': 'urdu ','ug': 'uyghur ','uz': 'uzbek ','vi': 'vietnamese ','cy': 'welsh ',
    'xh': 'xhosa ','yi': 'yiddish ','yo': 'yoruba ','zu': 'zulu'

Additional Notes

    . This script demonstrates how to perform speech recognition, language detection, translation, and text-to-speech synthesis in real-time.
    . You can customize the desired language for translation by modifying the tlLanguage variable.
    . Ensure that your microphone is properly configured and that you have an active internet connection for speech recognition and translation to work.

If you encounter any issues or have suggestions for enhancements, please create an issue or submit a pull request. Thank you!
