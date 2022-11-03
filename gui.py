from tkinter import *
from chat_bot import *
from PIL import Image, ImageTk
 
# GUI
root = Tk()
root.title("Automate Health Chatbot")
root.geometry("800x700")
ico = Image.open('mdoc-logo.png')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)
root.config(padx=15, pady=15)
 
BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"
 
FONT = "century 14"
FONT_BOLD = "century 13 bold"
 
# Send function 
def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
            
    return numpy.array(bag)

def chat():

    send = "You -> " + e.get()
    txt.insert(END, "\n" + send)
 
    inp = e.get().lower()

    if inp.lower() in ("exit", "bye", "end", "quit", "clear"):
        txt.delete("1.0", "end")
        txt.insert(END, "Goodbye. I hope I managed to be of help to you.\n\n")
        e.delete(0, END)
        return


    if inp.lower() in ("hello", "hi", "hie", "sup", "greetings"):
        txt.insert(END, "\n\nHello, I am your health assistant.\nPlease type the symptoms you are having.\n\n")
        e.delete(0, END)
        return

    if inp.lower() in ("", " ") or inp.isdigit() or len(inp) <= 3:
        txt.insert(END, "\n\nSorry I did not get the symptoms you entered.\n\n")
        e.delete(0, END)
        return



    results = model.predict([bag_of_words(inp, words)])
    results_index = numpy.argmax(results)
    tag = labels[results_index]
    centre_recommendation = []
    for tg in data["DiseaseSymptom"]:
        if tg['Disease'] == tag:
            responses = tg['Response']

    for centre, diseases in disease_facility.items():
        if tag in diseases:
            centre_recommendation.append(centre)
        if len(centre_recommendation) > 3:
            break;
    
    if len(centre_recommendation) == 0:
        txt.insert(END, "\n\nSorry, we don't have facilities that can help you in Upper East Region.\n\n")
    else:       
        txt.insert(END, "\n\nHere are the facilities we are recommending for you: " + ",".join(centre_recommendation) + "\n\n")
   
    e.delete(0, END)
 
 
lable1 = Label(root, fg="black", text="Welcome to AutomateHealth's chatbot demo", font=FONT_BOLD, width=60, height=1).grid(
    row=0, column=0, columnspan=2, pady=5)
 
txt = Text(root, bg="black", fg="green", font=FONT, width=70)
txt.grid(row=1, column=0, columnspan=2)
txt.insert(END, "Hello, I am your health assistant.\nPlease type the symptoms you are having.\n\n")
 
# scrollbar = Scrollbar(txt)
# scrollbar.place(relheight=1, relx=0.974)
 
e = Entry(root, bg="black", fg="white", font=FONT, width=65)
e.grid(row=2, column=0)
e.insert(0, 'Enter your symptoms here')
 
send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
              command=chat).grid(row=2, column=1)
 
root.mainloop()
