def create_data(file_name, data_name = "train.txt"):
    with open (data_name, mode= "w", encoding="utf8") as train_data:
        if type(file_name) == str:
            with open (file_name, mode="r", encoding="utf8") as raw_text:
                for line in raw_text:
                    if line.split("\t")[3] == "0" and line.split("\t")[3] != "Gelöscht":
                        train_data.write(line.split("\t")[4]+"\t"+line.split("\t")[5]+"\n")
        elif type(file_name) == list:
            for name in file_name:
                with open (name, mode="r", encoding="utf8") as raw_text:
                    for line in raw_text:
                        if line.split("\t")[3] == "0" and line.split("\t")[3] != "Gelöscht":
                            train_data.write(line.split("\t")[4]+"\t"+name+"\t"+line.split("\t")[5]+"\n")

            
create_data(["Maskenpflicht.txt", "Coronaimpfung.txt", "Lockdown.txt"])
