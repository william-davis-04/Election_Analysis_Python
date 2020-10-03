import csv
import os
#Assign a variable for the file to load and the path.
file_to_load = os.path.join('Resources', 'election_results.csv')
#Assign a variable to save the file to a path. 
file_to_save = os.path.join('analysis', 'election_analysis.txt')

#1. Inititalize a total vote counter. 
total_votes= 0

#Candidate Options
candidate_options = []

#Declare the empty dictionary.
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0



#open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read the header row.
    headers = next(file_reader)

    #Print each row in the CSV file.
    for row in file_reader: 
        #Add to the total vote count.
        total_votes += 1

        #Print the candidate name from each row.
        candidate_name = row[2]

        #If the candidate does not match any existing candidate....
        if candidate_name not in candidate_options:
            #Add it to the list of candidates.
            candidate_options.append(candidate_name)

            #Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
            #Add a vote to that candidate's count each loop
        candidate_votes[candidate_name]+= 1
    #Determine the percentage of votes for each candidate.
    #Iterate through the candidate list. 
    for candidate in candidate_votes:
        #Retrieve vote count of a candidate. 
        votes = candidate_votes[candidate]
        #Calculate the percentage of votes.
        vote_percentage = int(votes) / int(total_votes) * 100

        #To do: print out each candidate's name, vote count, and percentage of votes.
        #votes to the terminal.

        #Determine winning vote count and candidate
        #Determine if the votes is greater than the winning count.
        if(votes > winning_count) and (vote_percentage > winning_percentage):
            #If true then set winning_count = votes and winning_percent = #vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate
    winning_percentage_summary = (
        f'----------------------\n'
        f'Winner:  {winning_candidate}\n'
        f'Winning Vote Count: {winning_count:,}\n'
        f'Winning Percentage: {winning_percentage:.1f}%\n'
        f'----------------------\n'
        )
    #To Do: print out the winning candidate, vote count, and percentage to terminal.
        #Print Candidate % of votes 
    print(winning_percentage_summary)
        
    


