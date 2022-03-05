# Grading Script 

This grading script serves process all submissions and return
the results. 

Step 1: Download the entire submission zip via Canvas
![Alt text](/images/download_all.png?raw=true "Download All Submissions")

Step 2: Clone this Repo

Step 3: Unzip the Submission Folder into this Repo

Step 4: create "temp" folder
![Alt text](/images/temp.png?raw=true "Temp Folder")

Step 5: Insert Tests, Makefile, and runscript into temp

Step 6: Run unzip_all_folders() in grading.py. unzip_all_folders unzips all submissions. 
In the main method in grading only uncomment the first line and then run the python script. For subsequent steps you will have to uncomment other lines and recomment previous lines.
![Alt text](/images/unzip.png?raw=true "Unzip Folders")

Step 7: Run grading.py with remove_all_makefile(). Removes all makefiles in submission folders only. 

Step 8: Run grading.py with copy_defaults_to_all_folders(). This copies  temp/tests/, Makefile, and run_tests.sh from /temp to each groups folder. This is useful because I had to add ".bak" to the sed line in each Makefile so I replaced them all. This might not be the case on other systems. I also added -Wno-LATCH to the Verilator flags to suppress the Latch warning. 

Step 9: Run grading.py with run_tests_store_results(). This will output all results into a csv (scores.csv).



