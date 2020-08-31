# Tata-AIG-Project
Interview Project for Tata Aig

## TO run code please clone Repository and follow:-
    1. Make sure you have python 3 and above installed
    2. create a virtual environment using venv using -> `python3 -m venv /path/to/new/virtual/environment`
    3. activate it using -> `source /path/to/new/virtual/environment/bin/activate`
    4. install requirements -> `pip install -r requirements.txt`
    5. run local server -> `python manage.py runsever`

## Api Spec Doc:-
    ### All API's tested with limited data only and rated at 6 ms

    1. Get a list of policy numbers owned by a user:-
        *Payload Requirements  -: user_id(int)*
        Rest APTcall -: user_policy/<int:usr_id>/
                        example-: http:/host:port/customer_insurance/user_policy/1/


    2. Get policy details for a given policy number:-
        *Payload Requirements -:  policy_id(int)*
        Rest APTcall          -:  policy_detail/<int:policy_id>/
                                  example:- http:/host:port/customer_insurance/policy_detail/3/

    3.  Given a User and a format, get the List of Policies for the user in the prescribed format:-
        *Payload Requirements -:  user_id(int), format_name(str)*

        Rest APIcall for csv  -:  user_policy_dump/<int:usr_id>/<str:format_name>/
                                  example:- http:/host:port/customer_insurance/user_policy_dump/1/csv/
        Rest APIcall for json -:  user_policy_dump/<int:usr_id>/<str:format_name>/
                                  example:- http:/host:port/customer_insurance/user_policy_dump/1/json/
        Rest APIcall for xlsx -:  user_policy_dump/<int:usr_id>/<str:format_name>/
                                  example:- http:/host:port/customer_insurance/user_policy_dump/1/xlsx/

        Error Handleing and descriptive responses in place for failures.

    4. User list api:-
       *Payload Requirements -: None

       Rest APIcall          -: user_list/
                                example :- http://host:port/customer_insurance/user_list/4/
        

