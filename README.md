An online biding project built using django framework.  In this a bidder can bid and seller can sell the product.

Requirements:-
    python3


Create virtual enviornment:-
    Step 1 :-
        Create a virtualenv using below command :-
            python3 -m virtualenv auction
    
    A directory with "auction" name will be created.

To activate virtual enviornment:-
    source auction/bin/activate

To intiate directory with git :-
    
    Step 2.1 :-
        git init

    Step 2.2 :-
        git pull https://github.com/rohanJa/onlineAuction.git
    
    Step 2.3 :-
        pip install -r requirements.txt
    

Now to intialize project:-

    Step 3.1 :-
        python manage.py makemigrations

    Step 3.2 :-
        python manage.py migrate


Now run the project :-

        python manage.py runserver 127.0.0.1:8000  
