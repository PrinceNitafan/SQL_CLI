Name: Prince Nitafan
Email: pnitafan2020@gmail.com

Note: this program requires the pyodbc library to be installed.
Run the file 'runProgram.py' on a command line to start the application.
You can run this on CSIL device's Command Prompt.

This SQL CLI program works with Microsoft's SQL Server.
The following variables needs to be filled in before running the program:
    DB_host = ''; DB_name = ''; DB_user = ''; DB_password = '';

Additionally, there are some triggers that can be used if wanted/needed.
// Read the notes in Triggers.txt for each trigger's functionality

// For more info on variable constraints, primary keys, etc, check the SQL_code.txt file
// pre-made data files (in datafiles folder) for these tables are provied by SFU CMPT 354 staff.
Tables: 
    business = (business_id, name, address, city, postal_code, stars, review_count) 
    checkin = (checkin_id, business_id, date) 
    tip = (tip_id, user_id, business_id, date, compliment_count) 
    review = (review_id, user_id, business_id, stars, useful, funny, cool, date) 
    user_yelp = (user_id, name, review_count, yelping_since, useful, funny, cool, fans, average_stars) 
    friendship = (user_id, friend) 
