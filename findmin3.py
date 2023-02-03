import pandas as pd

# https://tutorialspoint.dev/algorithm/dynamic-programming-algorithms/dynamic-programming-set-5-edit-distance
# A Dynamic Programming based Python program for edit - distance problem 
# Driver program - function editDistDP: This code is contributed by Bhavya Jain 
def editDistDP(str1, str2, m, n): 
    # Create a table to store results of subproblems 
    dp = [[0 for x in range(n+1)] for x in range(m+1)] 
  
    # Fill d[][] in bottom up manner 
    for i in range(m+1): 
        for j in range(n+1): 
  
            # If first string is empty, only option is to 
            # insert all characters of second string 
            if i == 0: 
                dp[i][j] = j    # Min. operations = j 
  
            # If second string is empty, only option is to 
            # remove all characters of second string 
            elif j == 0: 
                dp[i][j] = i    # Min. operations = i 
  
            # If last characters are same, ignore last char 
            # and recur for remaining string 
            elif str1[i-1] == str2[j-1]: 
                dp[i][j] = dp[i-1][j-1] 
  
            # If last character are different, consider all 
            # possibilities and find minimum 
            else: 
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert 
                                   dp[i-1][j],        # Remove 
                                   dp[i-1][j-1])    # Replace 
  
    return dp[m][n] 

def __main__():
    # Load a local Excel file
    with pd.ExcelFile("findmin3.xlsx") as xls:
        # Process the data on each sheet in Excel file
        for sheet in xls.sheet_names:
            data = pd.read_excel(xls, sheet, index_col=None, na_values=["NA"], header=None, skiprows=[0])

            # num_of_rows reps the number of rows by index
            num_of_rows = len(data.index)

            # Print sheet name
            print("\n\n== Now processing rows sheet named {} ==".format(sheet))
            # Cycle through each data pair in a sheet 
            # Find the num of character transformations for each data pair
            # Print the num char transformations in adjacent cell to the data pair of the sheet
            for row in range(num_of_rows):

                # call to read cell data is as follows: data[column][row]
                # we were failing to account that python counts from 0
                print("\n\nComparing input string '{0}' to target string '{1}'".format(data[0][row], data[1][row]))
                print("Number of character transformations: {}".format(editDistDP(data[0][row], data[1][row], len(data[0][row]), len(data[1][row]))))
                
            
            # # Find the average number of char transformations for a sheet
            # # Print the average number in a cell at the bottom of each sheet




__main__()