import pandas as pd
myschedule = pd.DataFrame({"Mardi": ["", "Math1 (1001_Germain (40p)) ", "CI 1 (1001_Germain (40p)) ", "INIT JAVA (2036_Germain (38p)) "],
                           "Mercredi": ["", "UE Futsal niveau 1 (Centre Sportif Universitaire Jean Sarrailh)", "", ""], 
                            "Jeudi": ["IS1 (Halles aux Farines (532C_Halle)) ", "CI 1 (2A_Halle(276p)) ", "IPF 1 (1001_Germain (40p)) ", "Math1 (1003_Germain (39p)) "],
                            "Vendredi": ["Math1 (1001_Germain (40p)) ", "IS1 (5C_Halle (147p)) ", "IPF 1 (Halles aux Farines (532C_Halle)) ", ""]},
                            index= ["8:30 - 10:30", "10:45 - 12:45 (Sport 12:00 - 14:00)", "14:00 - 16:00", "16:15 - 18:15"])
myschedule.to_csv("schedule.csv", index= True)