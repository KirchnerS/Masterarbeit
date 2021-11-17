class DataLoader():
    ## Nimmt eine Annotationsfile der Form ID+\t+DATE+\t+NODE+\t+USERNAME+\t+
    ## OPINION+\t+SENTIMENT+\t+TEXT+NEWLINE
    def __init__(self, txt_name: str):
        self.txt_name = txt_name

    def load_data_texts(self):
        #returned Liste von Texten
        texte = []
        mein_name = self.txt_name
        with open(mein_name, encoding="utf8") as f:
            for line in f:
                if len(line.split("\t")) == 7:
                    texte.append(line.split("\t")[6])
        return texte

    def load_data_labels_sentiment(self):
        #Returned Liste der Sentiment Labels
        labels = []
        mein_name = self.txt_name
        with open(mein_name, encoding="utf8") as f:
            for line in f:
                print(line, "\n")
                if len(line.split("\t")) == 7:
                    labels.append(line.split("\t")[5])
        return labels

    def load_data_labels_opinion(self):
        #Returned Liste der Opinion Labels
        labels = []
        mein_name = self.txt_name
        with open(mein_name, encoding="utf8") as f:
            for line in f:
                if len(line.split("\t")) == 7:
                    labels.append(line.split("\t")[4])
        return labels

    def print_ratio(self, labels: list, predictions: list):
        count = 0
        true_labels = 0
        for pair in zip(labels, predictions):
            count += 1
            print(pair, count)
            if pair[0] == pair[1]:
                true_labels += 1
        ratio = true_labels/count
        print(f"The ratio of correctly labled sentences is {ratio}")

                
