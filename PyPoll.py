# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes.
county_votes = {}
county_list = []
candidate_options = []
candidate_votes = {}
# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
largest_county=""
county_max_votes = 0
county_max_pct = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
    ####county analysis
        #get list of county names
        county_name = row[1]
        #add new unique names to list
        if county_name not in county_list:
            county_list.append(county_name)
            #initialize vote count of new names to zero
            county_votes[county_name] = 0
        #increment for vote for each county
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage    
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    # Save the winning candidate's results to the text file.
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
    
######county reporting 
    # report out county summary info, how many votes and what percentage of each county.
    county_header = f"County Breakdown:\n-------------------\n"
    print(county_header)
    txt_file.write (county_header)
    for county_name in county_votes:   
        votes = county_votes[county_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        county_summary = (f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(county_summary)
        txt_file.write(county_summary)
        #print_highest county turnout
        # Determine largest vote count, largestg percentage, and largest county.
        if (votes > county_max_votes) and (vote_percentage > county_max_pct):
            county_max_votes = votes
            largest_county = county_name
            county_max_pct = vote_percentage

    largest_county_summary = (
        f"-------------------------\n"
        f"Largest County: {largest_county}\n"
        f"Largest County Vote Count: {county_max_votes:,}\n"
        f"Largest Percentage: {county_max_pct:.1f}%\n"
        f"-------------------------\n")
    # Save the winning candidate's results to the text file.
    print(largest_county_summary )
    txt_file.write(largest_county_summary)
    