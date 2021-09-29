class DataLoader():
    def __init__(self, txt_name: str):
        self.txt_name = txt_name

    def load_data_texts(self):
        texte = []
        mein_name = self.txt_name
        with open(mein_name, encoding="utf8") as f:
            for line in f:
                if len(line.split("\t")) == 2:
                    texte.append(line.split("\t")[1])
        return texte

    def load_data_labels(self):
        labels = []
        mein_name = self.txt_name
        with open(mein_name, encoding="utf8") as f:
            for line in f:
                if len(line.split("\t")) == 2:
                    labels.append(line.split("\t")[0])
        return labels
    
    def print_ratio(self, labels: list, predictions: list):
        count = 0
        true_labels = 0
        for pair in zip(labels, predictions):
            print(pair)
            count += 1
            if pair[0] == pair[1]:
                true_labels += 1
        print(count)
        print(true_labels)
        ratio = true_labels/count
        print(f"The ratio of correctly labled sentences is {ratio}")

                
