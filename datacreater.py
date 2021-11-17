#Nimmt entweder ne Liste and File namen oder nur eine file und appended 
#in eine Train.txt datei

class DataCreator ():
    def __init__(self, file_name):
        self.file_name = file_name
        
    def create_data(self, data_name = "train.txt"):
        with open (data_name, mode= "w", encoding="utf8") as train_data:
            if type(self.file_name) == str:
                with open (self.file_name, mode="r", encoding="utf8") as raw_text:
                    for line in raw_text:
                        if line.split("\t")[3] == "0" and line.split("\t")[3] != "Gelöscht":
                            train_data.write(line.split("\t")[0]+"\t"+line.split("\t")[1]+"\t"+line.split("\t")[3]+"\t"+line.split("\t")[4]+"\t"+line.split("\t")[5]+"\n")
            elif type(self.file_name) == list:
                for name in self.file_name:
                    with open (name, mode="r", encoding="utf8") as raw_text:
                        for line in raw_text:
                            if line.split("\t")[3] == "0" and line.split("\t")[3] != "Gelöscht":
                                train_data.write(name+"\t"+line.split("\t")[0]+"\t"+line.split("\t")[1]+"\t"+line.split("\t")[3]+"\t"+line.split("\t")[4]+"\t"+line.split("\t")[5]+"\n")

            


if __name__ == "__main__":
    Texte = DataCreator(["Impfung.txt", "MaskenpflichtV2.txt", "Lockdown.txt"])
    Texte.create_data()
