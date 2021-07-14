#PyPoll

# Incorporate the Dependencies
import csv
import os

#files to load and Output
file_to_load = os.path.join(".", "Resources","election_data.csv")
file_to_output = os.path.join(".","Analysis","election_analysis.txt")

#Total Vote Counter
total_votes = 0

#Candidate Option and Vote Counter
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

#Read in CSV and Convert it into a list
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    
    #read the header
    header = next(reader)
    #print(header)
    for row in reader:
         
        # Add to total vote count
        total_votes = total_votes + 1
        
        #Extract the Candidate Name from each Row
        candidate_name = row[2]
        
        #If Candidate does not Match any existing Candidate....
        #(In a Way our loop is discovering Candidates as it goes)
        
        if candidate_name not in candidate_options:
            # Add Candidate to List of Candidates in the Running
            candidate_options.append(candidate_name)
            
            # begin tracking that Candidate Voter Count
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
        
with open(file_to_output, "w") as txt_file:
    #print the final vote count
    
    election_results = (
        "\n\nElection Results\n" +
        "-------------------\n" +
        "Total Votes: "+ str(total_votes) + "\n" +
        "-------------------\n"
    )
    
    # save the final vote count to text file
    
    txt_file.write(election_results)
    
    #determine the winner by loop through the counts
    
    for candidate in candidate_votes:
        
        #Retrive Vote Count and Percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100
        
        #determine winning vote count and candidate
        if(votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
            
        #print each candidate vote count and percentage to end
        
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        
        #print(voter_output, end="")
        
        txt_file.write(voter_output)
        
    #print winning candidates
    winning_candidate_summary = (
        f"-------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------\n"
    )
    #print(winning_candidate_summary)
    
    #Save the winning candiate name to text file
    txt_file.write(winning_candidate_summary)