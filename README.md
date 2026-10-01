# python-refresher

In Assignment 1, I made several additions that are noted here.\
\
(1) Created a working get_columns function\
(2) Modified the get_columns function such that is can accommodate integer or 
    string column inputs/outputs\
(3) Fixed the print_fires file such that is grabs the right columns\
(4) Modified the get_columns function to default the output column to column 1.
    Note: print_fires already could accommodate this change\
(5) Created a run.sh file to run the print_fires file\
\
In Assignment 2, I made several changes that are noted here.\
\
(1) Adapted the PIP8 styleguide using pycodestyle\
(2) Created a working environment named 'swe4s' and contained in 
    'environment.yml' with all required packages\
(3) Modified 'print_fires.py' to accommodate argparse argument handling for
    'country', 'country_column', 'fires_column', and 'file_name'\
(4) Modified the 'get_column' function within 'my_utils.py' to return the fires
    information as integers, including adding several possible exceptions\
(5) Updated 'run.sh' to contain three test cases: one that runs properly, one
    that fails due to a file error, and one that fails due to an input error\
\
In Assignment 3, I made several changes that are noted here.\
\
(1) Added supplementary math functions 'mean', 'median', and 'std' to compute
    the mean, median, and standard deviation of an input array, respectively\
(2) Added this functionality to 'print_fires.py' such that you can now perform 
    these basic operations on the number of yearly fires in a given country\
(3) Created several unit tests for the new functions in 'my_utils.py' under the
    'test_my_utils.py' file\
(4) Created functional tests for 'print_fires.py' and stored these in
    'test_print_fires.sh'\
(5) Maintained PIP8 styleguide compliance\
\
In Assignment 4, I made several changes that are noted here.\
\
(1) Added three tests to 'test.yml' under '.git/workflows' to automatically
    run pycodestyle, 'test_my_utils.py', and 'test_print_fires.sh' upon either
    push or commit\
(2) Updated several tests to run on the git startup linux server\
(3) Updated the 'environment.yml' file to be compatible with linux, whereas it
    was only compatible with windows systems beforehand and would not run with
    Github workflows\
(4) Maintained PIP8 styleguide compliance
