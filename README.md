# Assaydashboard

A Dashboard application built using django and chart.js

## Data requirements
1. The uploaded CSV files must contain be in the following format.
| Assay                                     | January | November | December | Year | AssayID       | MachineID           |
| ----------------------------------------- | ------- | -------- | -------- | ---- | ------------- | ------------------- |
| Sick panel (MS/MS)                        | 279     | 219      | 220      | 2020 | SICKPANEL\_20 | FI-MSMS             |
| Urine organic Acid (UOA)                  | 119     | 101      | 127      | 2020 | UOA\_20       | GC-MS               |
| Plasma Amino Acid (PAA)                   | 69      | 0        | 5        | 2020 | PAA\_20       | Amino acid analyzer |
| Plasma Very Long Chain Fatty Acid (VLCFA) | 28      | 48       | 54       | 2020 | VLCFA\_20     | LC-MSMS-1           |
| Serum Methyl Maalonic Acid (MMA)          | 44      | 44       | 40       | 2020 | MMA\_20       | LC-MSMS-2           |
| Serum Biotinidase                         | 16      | 11       | 36       | 2020 | SERUM\_20     | Spectrophotometer   |

2. The assayID and machineID must be unique. and the ID must the 2 digit year for the corresponding data.
3. The app is designed such that the user uploads the sample collected data every month, for the same ASSAYID's.  
## ✨ Deploy in production using `Docker`

> Get the code

```bash
$ git clone <repo>
$ cd genelookup
```
> Configure environment variables
```
1. Create a .env file and paste the contents. 

DEBUG=1
DB_NAME=dbname
DB_USER=rootuser
DB_PASS=changeme
SECRET_KEY=changeme
ALLOWED_HOSTS=127.0.0.1

2. Change the variables to store real values.
3. Allowed hosts can be a comma seperated list of multiple hosts (IP's or domain names)
```
> Start the app in Docker

```bash
$ docker-compose up --build
$ docker-compose run --rm app sh -c "python manage.py createsuperuser"
```

Visit `http://localhost:80` in your browser. The app should be up & running.


<br />

## ✨ How to use it for development
The development deployment provies hot reloading for the code to update in real time
```bash
$ # Get the code
$ git clone <repo>
$ cd genelookup
$
$ 
$ # Docker compose
$ docker-compose -f docker-compose-dev.yml up --build
$
$ # open a new terminal and run 
$ docker-compose -f docker-compose-dev.yml run --rm app sh -c "python manage.py createsuperuser"
$
$ # Access the web app in browser: http://127.0.0.1/
```

<br />
