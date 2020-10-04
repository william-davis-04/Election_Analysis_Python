import csv
import os
#Assign a variable for the file to load and the path.
file_to_load = os.path.join('Resources', 'election_results.csv')
#Assign a variable to save the file to a path. 
file_to_save = os.path.join('analysis', 'election_analysis_challenge.txt')

#1. Inititalize a total vote counter. 
total_votes= 0

#Candidate Options
candidate_options = []

#County Options
county_options = []

#Declare the empty dictionary.
candidate_votes = {}

#Declare County empty dictionary.
county_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Define Largest County Voting
Largest_turnout_count = 0
Largest_turnout_percentage = 0
Largest_turnout_county = ""

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

        #Print the county name from each row
        county_name = row[1]

        #If the candidate does not match any existing candidate....
        if candidate_name not in candidate_options:
            #Add it to the list of candidates.
            candidate_options.append(candidate_name)

            #Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
            #Add a vote to that candidate's count each loop
        candidate_votes[candidate_name]+= 1
        #If the candidate does not match any existing candidate....
        if county_name not in county_options:
            #Add it to the list of counties.
            county_options.append(county_name)
            #Begin tracking total vote's per county.
            county_votes[county_name] = 0
            #Add a vote to that candidate's count each loop
        county_votes[county_name]+= 1
    #Save the results to our text file.
    with open(file_to_save,'w') as txt_file:
            election_results = (
                f'\nElection Results\n'
                f'-------------------------\n'
                f'Total Votes: {total_votes:,}\n'
                f'------------- Results by Candidate --------------\n')
            print(election_results, end="")
            txt_file.write(election_results)
        #Determine the percentage of votes for each candidate.
        #Iterate through the candidate list. 
            for candidate in candidate_votes:
            #Retrieve vote count of a candidate. 
                votes = candidate_votes[candidate]
            #Calculate the percentage of votes.
                vote_percentage = int(votes) / int(total_votes) * 100
                candidate_results = (f'{candidate}: {vote_percentage:.1f}% ({votes:,})\n')
            #Print each candidates votes and percentage to the terminal
                print(candidate_results)
            #write to the text file
                txt_file.write(candidate_results)
            #Determine winning vote count and candidate
            #Determine if the votes is greater than the winning count.
                if(votes > winning_count) and (vote_percentage > winning_percentage):
                    #If true then set winning_count = votes and winning_percent = #vote_percentage
                    winning_count = votes
                    winning_percentage = vote_percentage
                    winning_candidate = candidate
                winning_candidate_summary = (
                f'-----------------------------------------\n'
                f'Winner:  {winning_candidate}\n'
                f'Winning Vote Count: {winning_count:,}\n'
                f'Winning Percentage: {winning_percentage:.1f}%\n'
                f'--------- Results by County -------------\n'
                )
                #Print Candidate % of votes
                print(winning_candidate_summary)
                #save winning candidate sumarrary to the text file. 
            txt_file.write(winning_candidate_summary)
        #Determine the percentage of votes for each County.
        #Iterate through the County list. 
            for county in county_votes:
            #Retrieve vote count of a candidate. 
                votes_per_county = county_votes[county]
            #Calculate the percentage of votes.
                vote_percentage_per_county = int(votes_per_county) / int(total_votes) * 100
                county_results = (f'{county}: {vote_percentage_per_county:.1f}% ({votes_per_county:,})\n')
            #Print each candidates votes and percentage to the terminal
                print(county_results)
            #Header for county 
                county_header = (f'- Results by County -')
            #write to the text file
                txt_file.write(county_results)
            #Determine the county with the highest amount of votes
            #Determine if the votes is greater than the winning count.
                if(votes_per_county > Largest_turnout_count) and (vote_percentage_per_county > Largest_turnout_percentage):
                    #If true then set winning_count = votes and winning_percent = #vote_percentage
                    Largest_turnout_count = votes_per_county
                    Largest_turnout_percentage = vote_percentage_per_county
                    Largest_turnout_county = county
                Largest_turnout_county_Summary = (
                f'----------------------\n'
                f'County with the largest voter turnout:  {Largest_turnout_county}\n'
                f'Amount of votes: {Largest_turnout_count:,}\n'
                f'Percentage of votes among counties: {Largest_turnout_percentage:.1f}%\n'
                f'----------------------\n'
                )
                #Print County % of votes
                print(Largest_turnout_county_Summary)
                #save Largest turnout by county to the text file. 
            txt_file.write(Largest_turnout_county_Summary)
           
        

    
            


                
            


