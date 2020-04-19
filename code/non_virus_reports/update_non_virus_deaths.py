import requests
import re 
import os.path
from os import path
import bs4
from bs4 import BeautifulSoup
import couchdb
from urllib.parse import urlparse
import csv
import datetime
import time

# I scripted this in urgency, So code quality or the logic isn't great.
# This is mostly a hack. 

pushover_api_token =str(os.environ.get("pushover_api_token"))
pushover_user_key = str(os.environ.get("pushover_user_key"))
pushover_url = "https://api.pushover.net/1/messages.json"
covid_db_full_url = str(os.environ.get("covid_db_full_url"))
non_virus_archive_folder_path = "../../non-virus-deaths-media-reports-backup/{0}"
force_run = False

couchdb_db_name = "covid19"
couch = couchdb.Server(covid_db_full_url)
#database = couch[couchdb_db_name]


states = {}
states["Andhra Pradesh"]="AP"
states["Andra Pradesh"]="AP"
states["Arunachal Pradesh"]="AR"
states["Assam"]="AS"
states["Bihar"]="BR"
states["Chattisgarh"]="CT"
states["Chhattisgarh"]="CT"
states["Goa"]="GA"
states["Gujarat"]="GJ"
states["Haryana"]="HR"
states["Himachal Pradesh"]="HP"
states["Jharkhand"]="JH"
states["Karnataka"]="KA"
states["Kerala"]="KL"
states["Madhya Pradesh"]="MP"
states["MP"]="MP"
states["Maharashtra"]="MH"
states["Maharahstra"]="MH"
states["Maharastra"]="MH"
states["Manipur"]="MN"
states["Meghalaya"]="ML"
states["Mizoram"]="MZ"
states["Nagaland"]="NL"
states["Odisha"]="OR"
states["Orissa"]="OR"
states["Punjab"]="PB"
states["Rajasthan"]="RJ"
states["Rajastha"]="RJ"
states["Sikkim"]="SK"
states["Tamil Nadu"]="TN"
states["Telengana"]="TG"
states["Telangana"]="TG"
states["Tripura"]="TR"
states["Uttarakhand"]="UT"
states["Uttar Pradesh"]="UP"
states["UP"]="UP"
states["West Bengal"]="WB"
states["Andaman and Nicobar Islands"]="AN"
states["Chandigarh"]="CH"
states["Dadra and Nagar Haveli"]="DN"
states["Daman and Diu"]="DD"
states["Delhi"]="DL"
states["Jammu and Kashmir"]="JK"
states["JK"]="JK"
states["Ladakh"]="LA"
states["Lakshadweep"]="LD"
states["Pondicherry"]="PY"
states["Puducherry"]="PY"


def getDateTimeObject(passed_string):
      passed_string = passed_string.replace(" ","")
      if passed_string == "":
            return ""
      date_time_obj1 = datetime.datetime.strptime(passed_string,"%B%d,%Y" )  #      
      return time.strftime("%Y-%m-%d", date_time_obj1.timetuple())



file_name = non_virus_archive_folder_path.format("non-virus-deaths.tsv")
batch_to_process = "SET_APRIL_19"
message = ""
print("============================================{batch_to_process}===================================".format(batch_to_process=batch_to_process))
with open(file_name) as csv_file:
      csv_reader = csv.reader(csv_file, delimiter='\t')
      line_count = 0
      insert_rows = 0
      for row in csv_reader:            
            print("------------------------------------------------------------------------------")
            if line_count == 0 or line_count == 1:
                  pass
            else:
                  batch = row[0]

                  if batch.strip() == batch_to_process:
                        pass
                  else:
                        #anything else, skip
                        continue

                  seq = row[1]
                  location = row[2]
                  district = row[3]
                  state = (row[4]).strip()


                  # March 27,2020 to 2020-03-28                                     
                  incident_date = getDateTimeObject(row[5])  

                  deaths = int(row[6])

                  reasons = row[7]
                  convert_array = [x.strip() for x in reasons.split(",")]
                  reasons_array = [x.capitalize() for x in convert_array]
                  

                  source_publication = row[8]

                  source_date = getDateTimeObject(row[9])   
                  if incident_date == "" or incident_date is None:
                        incident_date = source_date


                  source_link = row[10]  

                  #_id = "{0}|{1}|{2}".format(source_date, "non_virus_deaths", batch)
                  data = {}
                  #data["_id"] = _id
                  data["type"] = "non_virus_deaths"
                  data["location"] = location
                  data["district"] = district
                  data["state"] = states[state]       
                  data["incident_date"] = incident_date 
                  data["deaths"] = deaths
                  data["reason"] = reasons_array
                  data["source_date"] = source_date
                  data["source_link"] = source_link
                  parsed_uri = urlparse(source_link)
                  data["source"] = parsed_uri.netloc
                  
                  insert_rows = insert_rows + 1
                  print("----------------------------------------------------------------------------{0}".format(insert_rows))
                  print(data)




                  #database.save(data)     
                              

            #print(message)
            line_count = line_count + 1
