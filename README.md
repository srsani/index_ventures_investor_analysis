# Investor analysis:

During the past three decades, there have been significant increases in both the number of startup companies and the total amount of interest and activities in this sector. Companies such as Google, Skype, Dropbox, etc. are examples of success stories. My client, Index Ventures, is a one of the oldest, largest and most successful Venture Capital (VC) firms in Europe. My project was to provide them with different metrics and insight on the investor’s ecosystem by using the available data from Crunchbase’s API so that they would be able to implement my findings into their internal web-app tool. During my project, I worked with the available data on over 44K investors and over 0.5M startup companies. You can see a summery of my results in the attached presentation file ('Sohrab_Sani_ASI.pdf') and this [post](https://medium.com/@RedjaiSani/index-ventures-ranking-the-performance-of-venture-capital-firms-d36faf653466)

The notebooks and codes in this repository are organized a numerical order:

- 0_0_0_requirements.sh:
 	- Running this file install anaconda and install all the packages which is necessary throughout this project.  First this file needs to become excitable buy typing “chmod +x 0_requirements.sh”. Afterwards but typing “sudo ./ 0_requirements.sh” all the packages will be installed. This process take something between 10 to 15 min.

- 0_0_downloading_datasets.ipynb:
 	 - This notebook shows how to save all the tables to “.csv” files for feather data analysis.

-   0_1_exploratory_data_analysis_generating_new_datasets.ipynb:
	- This notebook goes over some preliminary data analysis on “companies_funding” table.
	- Make correction to USD funds by using “Consumer Price Index”
	- Fix some of the round type naming issues.
	- Finally make a new data set from “companies_funding” and “companies_status”.

- 0_2_investor_data.py:
	- This scrip generates two csv file based on Investor’s and the description of companies that are English.

- 0_3_textdata_tags.ipynb:
	- Generats data set for NLP

- 0_4_tag_vector.ipynb:
	- Generate vector representation from 3271 unique tags.

-  1_0_0_Ranking_Investors_Exit_Score.ipynb:
	- Explains how the “Exit Score” is calculated and provide this score for 44552 investors based on their investments outcome over the past 20 years.

- 1_0_1_Exit_Score_To_SQL_5_10_20.py:
	- Generates “Exit Score” for the past 5,10 and 30 years and upload the table to the DB

- 1_1_0_Ranking_investors_based_on_seed_venture_A-2.ipynb:
	- Explains how the “Operating Score” is calculated and provide this score for 27903 based on their “seed to “venture A” investments in the past 20 years.

-	2_1_0_tag_UMAP_HDBSCAN.ipynb:
  - This note book uses the data that is generated by “0_4_tag_vector.ipynb” and by performing UMAP and HDBSCAN provides a platform for generating new tags.

-	2_1_1new_tag_name_map_generator.py:
  - This script generates a “clustername.p” file which is required to cluster and clean tags for companies and investors.  

-	2_2_0_new_tag_generator.py:
  - Map the clustered tags with original tags and update the result to the table “investor_clustered_tag”.
