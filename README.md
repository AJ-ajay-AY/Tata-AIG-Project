# Interview Project for Tata Aig

## To run code please clone Repository and follow:-
    1. Make sure you have python 3 and above installed
    2. create a virtual environment using venv using -> python3 -m venv /path/to/new/virtual/environment
    3. activate it using -> source /path/to/new/virtual/environment/bin/activate
    4. install requirements -> pip install -r requirements.txt
    5. run local server -> python manage.py runsever

## Api Spec Doc:-
### All API's tested with limited data only and rated at below 6 ms

    1.  Get a list of policy numbers owned by a user:-
        Payload Requirements  -: user_id(int)
        Rest APTcall -: user_policy/<int:usr_id>/
                        example-: http:/host:port/customer_insurance/user_policy/1/
![Policy numbers owned by a user](https://i.ibb.co/YNk0551/Screenshot-2020-09-01-at-12-22-20-PM.png "Policy numbers owned by a user")


    2. Get policy details for a given policy number:-
        Payload Requirements -:  policy_id(int)
        Rest APTcall          -:  policy_detail/<int:policy_id>/
                                  example:- http:/host:port/customer_insurance/policy_detail/3/
![Policy details for a given Policy number](https://i.ibb.co/Ltck0Y2/Screenshot-2020-09-01-at-12-20-38-PM.png "Policy details for a given Policy number")

    3.  Given a User and a format, get the List of Policies for the user in the prescribed format:-
        Payload Requirements -:  user_id(int), format_name(str)

        Rest APIcall for csv  -:  user_policy_dump/<int:usr_id>/<str:format_name>/
                                  example:- http:/host:port/customer_insurance/user_policy_dump/1/csv/
![Policy details for a given Policy number](https://i.ibb.co/N9MZ7Y0/Screenshot-2020-09-01-at-12-37-08-PM.png  "Policy details for a given Policy number")
        
        Rest APIcall for json -:  user_policy_dump/<int:usr_id>/<str:format_name>/
                                  example:- http:/host:port/customer_insurance/user_policy_dump/1/json/
![Policy details for a given Policy number](https://i.ibb.co/rQ7KGrF/Screenshot-2020-09-01-at-12-34-27-PM.png "Policy details for a given Policy number")

        Rest APIcall for xlsx -:  user_policy_dump/<int:usr_id>/<str:format_name>/
                                  example:- http:/host:port/customer_insurance/user_policy_dump/1/xlsx/
![Policy details for a given Policy number](https://i.ibb.co/TK0mD5t/Screenshot-2020-09-01-at-12-50-09-PM.png "Policy details for a given Policy number")

        Error Handleing and descriptive responses in place for failures.

    4. User list api:-
       Payload Requirements -: None

       Rest APIcall          -: user_list/
                                example :- http://host:port/customer_insurance/user_list/4/
![User list](https://i.ibb.co/GVW57WC/Screenshot-2020-09-01-at-12-21-45-PM.png "Policy details for a given Policy number")
        


## Error Handleing and descriptive responses in place for failures.

