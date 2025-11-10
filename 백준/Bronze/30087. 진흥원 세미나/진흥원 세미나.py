N = int(input())

def classroom_number(subject):
    if subject == "Algorithm":
        print("204")
    elif subject == "DataAnalysis":
        print("207")
    elif subject == "ArtificialIntelligence":
        print("302")
    elif subject == "CyberSecurity":
        print("B101")
    elif subject == "Network":
        print("303")
    elif subject == "Startup":
        print("501")
    elif subject == "TestStrategy":
        print("105")

for i in range(N):
    seminar_subject = input()
    classroom_number(seminar_subject)