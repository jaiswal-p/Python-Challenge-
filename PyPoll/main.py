import os
import csv

# Path to collect data from the resources folder
ElectionData = os.path.join("..","PyPoll","Resources","election_data.csv")
fileId = open('output.txt', 'w')

# define the function and have it accept the pypoll data
def electionAnalysis(Pypoll):
    # Total number of vote cast in election
    TvoteCast= 0
    Candidate = []
    Total_Vote =[]

    for row in Pypoll:
        # Total vote cast
        TvoteCast+=1

         # List of candidate
        if row[2] not in Candidate:
            Candidate.append(row[2])

            #List of total individial candidate vote
            Total_Vote.append(0)
        for i,c in enumerate(Candidate):
            if c == row[2]:
                Total_Vote[i]+=1

    print("Election Results Analysis")
    fileId.write("Election Results Analysis")
    print("...............................................")
    fileId.write("...............................................")
    print(f"Total vote: {TvoteCast}")
    fileId.write(f"Total vote: {TvoteCast}")
    print("..................................................")
    fileId.write("..................................................")

    winner = ''
    max_vote = 0
    # Percentage of candidate vote
    for i in range(len(Total_Vote)):
        percentage_of_vote =(Total_Vote[i]/TvoteCast) *100
        print('{}: {:.3f}% ({})'.format(Candidate[i], percentage_of_vote, Total_Vote[i]))
        fileId.write('{}: {:.3f}% ({})'.format(Candidate[i], percentage_of_vote, Total_Vote[i]))
        # Comparing which candidae got the maximum vote
        if Total_Vote[i] > max_vote:
            max_vote = Total_Vote[i]
            winner = Candidate[i]
    #print(f" List of cndidate who received vote: {Candidate}")
    #print(f"Total vote for each candidate {Total_Vote}")
    print("........................................................")
    fileId.write("........................................................")
    print(f"winner: {winner}")
    fileId.write(f"winner: {winner}")

    fileId.close()

#Read the csv file
with open(ElectionData,"r") as csvfile:
    # split the data as comma deliminated
    csvreader = csv.reader(csvfile,delimiter =',')
    print(csvreader)
    csv_header =next(csvreader)
    #print(csv_header)

    electionAnalysis(csvreader)
