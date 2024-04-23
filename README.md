1. In this project we are going to work on Electoral bond data.
   These are two files of purchase details([EB_Purchase_Details.pdf](https://github.com/TanmayTanmayGarg/electoral-bond/files/15071520/EB_Purchase_Details.pdf)) and redumption details([EB_Redemption_Details.pdf](https://github.com/TanmayTanmayGarg/electoral-bond/files/15071524/EB_Redemption_Details.pdf)).
   we will convert these files into csv by pdf_to_csv.py code which use Fitz library. 

   We will use MySQL Workbench to create schema named electoral_bond.
   ![Screenshot 2024-04-23 103541](https://github.com/TanmayTanmayGarg/electoral-bond/assets/143330134/f52ffea8-0929-4972-8baf-405297410036)

   In this schema we will import both csv in two different tabels. 
   here I am showing how to import csv in the tabel of Schema electoral_bond.
   
  1.1. right click on tabels, then select 'tabel data import wizard'. browse csv file of 'purchase details' and 'redumption details'
![Screenshot 2024-04-23 104929](https://github.com/TanmayTanmayGarg/electoral-bond/assets/143330134/851e6bc7-8ebf-440b-b48c-3a0250f8f02a)

  1.2. browse csv file of 'purchase details' and 'redumption details'. here I am importing 'redumption details' csv file.
![Screenshot 2024-04-23 104347](https://github.com/TanmayTanmayGarg/electoral-bond/assets/143330134/6ba584c3-0923-4011-9723-ed6e34475613)

  1.3. click on next.
![Screenshot 2024-04-23 104507](https://github.com/TanmayTanmayGarg/electoral-bond/assets/143330134/141b7030-e745-41ff-8613-2bc467c71209)

  1.4. click on next.
![Screenshot 2024-04-23 104521](https://github.com/TanmayTanmayGarg/electoral-bond/assets/143330134/5a280e53-2575-46ad-a269-bf731ae1bf9a)

  1.5. It will stat importing.
![Screenshot 2024-04-23 104611](https://github.com/TanmayTanmayGarg/electoral-bond/assets/143330134/2f3794e7-8f70-441c-921b-804cd1ed8031)

  1.6. click on next.
![Screenshot 2024-04-23 104653](https://github.com/TanmayTanmayGarg/electoral-bond/assets/143330134/b856c841-3446-4a6d-9f58-e7bd87d59144)

  1.7. click on finish.
![Screenshot 2024-04-23 104709](https://github.com/TanmayTanmayGarg/electoral-bond/assets/143330134/73143d5f-af41-41ca-b1ce-65b966ad13d5)

  Similarly import 'purchase details' files.
  Refresh the schema and these two files now be available in the tabels section.
  ![Screenshot 2024-04-23 110224](https://github.com/TanmayTanmayGarg/electoral-bond/assets/143330134/3c651a16-d5b6-4d88-b388-f12a66f13177)
  ![Screenshot 2024-04-23 110316](https://github.com/TanmayTanmayGarg/electoral-bond/assets/143330134/26f60c89-62d6-4727-bfd5-d469e6804abf)

  Now MySQL part has compleated.

2. In your destop create a folder a folder, in my case I have named it as 'Dcc Assignment 4'.

  2.1. Open this folder in vs code.

  2.2. Go to the extension secton and make sure that python, html, live server, python debugger are installed and enabled. 

  2.3. run these command on terminal first run: 'pip install pip -D' and  then run 'pip install Flask Flask-MySQLdb'

  2.4. in this create a folder name 'templates'.

    2.4.1. In this folder create a new file named 'index.html' and put down the code I have provided in 'index.html' file in 'templates' folder and save it (ctrl+s).
    
    2.4.2. In this folder also create a new file named 'search_results.html' and put down the code I have provided in 'search_results.html' file in 'templates' folder and save it (ctrl+s).
    
  2.5.  create new file named 'app.py'.

    2.3.1. In this file put down the code I have provided in 'app.py' and save it (ctrl+s). But make sure to replace MYSQL_PASSWORD and MYSQL_USER. 
  ![image](https://github.com/TanmayTanmayGarg/electoral-bond/assets/143330134/628b0301-382e-4c2c-b6b1-f665296ee91e)

  2.6 Run this python file. you will see a link, like I have underlined.
![image](https://github.com/TanmayTanmayGarg/electoral-bond/assets/143330134/45304a9b-b6d9-4da4-bd06-7ce53f8569e3)

3. The Web-page will look like this.
![Screenshot 2024-04-23 142430](https://github.com/TanmayTanmayGarg/electoral-bond/assets/143330134/983b324e-ffb7-42ac-95b2-6d53c09cd7e8)
![Screenshot 2024-04-23 142439](https://github.com/TanmayTanmayGarg/electoral-bond/assets/143330134/67bf72d1-1965-4724-bd24-4d979ff7bc08)

  ## Features

- **Robust Search Functionality**: Search for records based on Bond Number, Political Party Name, Company Name, Reference No (URN), or Pay Branch Code.
- **Bar Chart Visualization**: Visualize the total amount of donations to all parties.
- **Download Button**: To download the bar plot shown 
- **About section**: It is on top shows the roll number and name.
- **Donor Information**: write the political party name and see which companies have donated to it.
  
e1. you have to enter the bond number and it will give out all purchase details and redumption details associate with it.
![Screenshot 2024-04-23 145628](https://github.com/TanmayTanmayGarg/electoral-bond/assets/143330134/8f902dc2-2ffd-4ecf-b858-7dd438e35a3e)
![Screenshot 2024-04-23 145648](https://github.com/TanmayTanmayGarg/electoral-bond/assets/143330134/a9fec1f8-2293-4e29-ba33-567e80c0b1a6)

e2. you can search by entering company name it will give data how many bonds they have purchased.
![Screenshot 2024-04-23 153633](https://github.com/TanmayTanmayGarg/electoral-bond/assets/143330134/766307c1-dc04-467e-b674-ca69bf48bf17)
![Screenshot 2024-04-23 153653](https://github.com/TanmayTanmayGarg/electoral-bond/assets/143330134/760d1c7d-c542-44ad-a644-cfe3e25615be)

e3. you can search for a political party, it will give data about date of encashment and denomination.
![Screenshot 2024-04-23 154138](https://github.com/TanmayTanmayGarg/electoral-bond/assets/143330134/c1b8d8ac-b88d-4602-a640-2bd4803dea36)
![Screenshot 2024-04-23 154225](https://github.com/TanmayTanmayGarg/electoral-bond/assets/143330134/8ac35758-d3a6-4751-b9bb-be6cb643fde8)

e4. when you seach for a political party it will filter out all data from redumption table.
![Screenshot 2024-04-23 161916](https://github.com/TanmayTanmayGarg/electoral-bond/assets/143330134/abd6fe87-8cf6-44b6-a8cc-964466b55099)
![Screenshot 2024-04-23 161956](https://github.com/TanmayTanmayGarg/electoral-bond/assets/143330134/5175cd49-fa60-4a96-910b-e831f72c12a7)

e5. when you seach for a company it will filter out all data from purchase table.
![Screenshot 2024-04-23 162138](https://github.com/TanmayTanmayGarg/electoral-bond/assets/143330134/e15329a0-5c3d-48e0-ba28-3ee05fad420c)
![Screenshot 2024-04-23 162117](https://github.com/TanmayTanmayGarg/electoral-bond/assets/143330134/5a4791b8-9cdb-40a3-8322-bad8a5da3cec)

f. download button below the graph allow the user to download graph in inmage format.
![Screenshot 2024-04-23 162323](https://github.com/TanmayTanmayGarg/electoral-bond/assets/143330134/b25abef8-1657-41ba-b219-7595cb88b549)
![Screenshot 2024-04-23 162336](https://github.com/TanmayTanmayGarg/electoral-bond/assets/143330134/1193a113-878e-47e9-9f2b-52e724adcaee)
![bar_chart (2)](https://github.com/TanmayTanmayGarg/electoral-bond/assets/143330134/20801220-7e07-4dac-9d2c-82cf8b0e36ae)

3. I have bar plot which shows which company received how many bonds value in rupees.

    
