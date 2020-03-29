# Media Report based Non Virus Deaths 

There are many deaths (Suicide, due to lockdown, lathicharge, hunger ,during migration etc) reported from the field which are related to COVID-19 disease but are not attributed to virus. Community (see credits) has collected them and organized them. 

Before using this data, please note the following:
 
 1. This is based on media reports
 2. We only archive, scrape and parse the data


## Credits

- [Kanika](https://twitter.com/_kanikas_)
- [Aman](https://twitter.com/CB_Aman)
- [Thejesh GN](https://thejeshgn.com)




## Submit
We have a google form where you can [submit the incidents](https://forms.gle/4BkJvBZH66kS65qbA).


## DataMeet Discussions 
You can follow and participate in discussions at [DataMeet](https://groups.google.com/forum/#!topic/datameet/vIsv3EgrX5s)


### Raw Data
We have semi parsed data availabe as [CSV](https://github.com/datameet/covid19/tree/master/non-virus-deaths-media-reports-backup).

### Web Archive of media
Individual articles are archived automatically on archive.org. 


### Parsed Data
 Parsed data in the form of JSON is availabe inside [data](https://github.com/datameet/covid19/tree/master/data). We update once a day. It has data since 2020-03-25


```
{
  "id": "2020-03-25|non_virus_deaths|17",
  "key": "2020-03-25|non_virus_deaths|17",
  "value": {
    "_id": "2020-03-25|non_virus_deaths|17",
    "_rev": "3-3381b76df61bff8c3b28276a1cffad27",
    "type": "non_virus_deaths",
    "location": "Rasingapuram",
    "district": "Theni",
    "state": "KL",
    "incident_date": "2020-03-24",
    "deaths": 4,
    "reason": [
      "Forest fire",
      "Roadblock"
    ],
    "source_date": "2020-03-25",
    "source_link": "https://www.thehindu.com/news/national/tamil-nadu/death-toll-rises-to-4-in-theni-forest-fire-tragedy/article31160605.ece and https://www.thenewsminute.com/article/3-women-and-one-year-old-child-die-theni-forest-fire-121088",
    "source": "www.thehindu.com"
  }
}
```

`deaths` : no of deaths reported in this specific incident report

### API
Send an email to thej@datameet.org to get access to API.


## Projects Using this dataset
