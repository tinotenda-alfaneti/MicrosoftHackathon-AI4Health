from tkinter import *
from chat_bot import *
 
# GUI
root = Tk()
root.title("Automate Health Chatbot")
root.geometry("900x800")
 
BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"
 
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"
 
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
        txt.insert(END, "\nAI -> Sorry, we don't have facilities that can help you in Upper East Region.")
    else:       
        txt.insert(END, "\nAI -> Here are the facilities we are recommending for you:\n " + ",".join(centre_recommendation))
   
    e.delete(0, END)
 
 
lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20, height=1).grid(
    row=0)
 
txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)
 
scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)
 
e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)
 
send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
              command=chat).grid(row=2, column=1)
 
root.mainloop()
