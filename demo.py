import speech_recognition as sr
import spacy
nlp = spacy.load("en_core_web_sm")
from spacy.matcher import PhraseMatcher
matcher = PhraseMatcher(nlp.vocab)
matcher1 = PhraseMatcher(nlp.vocab)
matcher2 = PhraseMatcher(nlp.vocab)
#bot = ChatBot('Bot')
  
#trainer = ListTrainer(bot)

def BMI(height, weight):
    bmi = weight/(height**2)
    return bmi



r=sr.Recognizer()
print(sr.Microphone.list_microphone_names())

matcher1 = PhraseMatcher(nlp.vocab)

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source,duration=1)
    # r.energy_threshold()
    print("say anything : ")
    audio= r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(text)
    except:
        print("sorry, could not recognise")

while True:
    doc3 = nlp(text)
    phrase_list = ['BMI','bmi','Body mass index']
    phrase_patterns = [nlp(text) for text in phrase_list]

        # Pass each Doc object into matcher (note the use of the asterisk!):
    matcher.add('BMI', None, *phrase_patterns)
    matches = matcher(doc3)
    string_id=0

    phrase_list1 = ['image','Image']
    phrase_patterns1 = [nlp(text) for text in phrase_list1]

        # Pass each Doc object into matcher (note the use of the asterisk!):
    matcher1.add('image', None, *phrase_patterns1)
    matches1 = matcher1(doc3)
    string_id1=0

    phrase_list2 = ['voice','audio']
    phrase_patterns2 = [nlp(text) for text in phrase_list2]

        # Pass each Doc object into matcher (note the use of the asterisk!):
    matcher2.add('image', None, *phrase_patterns2)
    matches2 = matcher2(doc3)
    string_id2=0
    
    for match_id, start, end in matches:
        string_id = nlp.vocab.strings[match_id]  # get string representation
        span = doc3[start:end]                    # get the matched span
        #print(match_id, string_id, start, end, span.text)

    for match_id1, start1, end1 in matches1:
        string_id1 = nlp.vocab.strings[match_id1]  # get string representation
        span = doc3[start1:end1]

    for match_id2, start2, end2 in matches2:
        string_id2 = nlp.vocab.strings[match_id2]  # get string representation
        span = doc3[start2:end2]

    if text == 'OK' or text == 'ok':
        print('Bot: bye')
        break

    elif string_id!=0:
        Height = float(input("Bot: Enter height : "));
        Weight = float(input("Bot: Enter Weight : "));

        bmi = BMI(Height, Weight)
        print("Bot: The BMI is", format(bmi), "so ", end='')

        if (bmi < 18.5):
            print("underweight")
            break
                  
        elif ( bmi >= 18.5 and bmi < 24.9):
            print("Healthy")
            break 
        elif ( bmi >= 24.9 and bmi < 30):
            print("overweight")
            break
    elif string_id1!=0:
        import imag

