# State-Results-Project

This is a Python program that was written to generate results of Class 12 TN State Results

The webpage in question works based on two parameters: the DOB of the student, and the Roll Number

This program is written so that all roll numbers, between the specified lower and upper limit by the
user, are generated and processed for a fixed DOB. This generates results for the combination and 
displays it in new tabs in a browser window.

# What it does

Users are asked to input the fixed DOB, and the Lower and Upper limits of roll numbers between which
the results are to be generated

It inputs the current combination out of the generated combinations and generates the result by sending
keystrokes to the shell application which has a browser window open.

This generates the result for that combination. Now, the whole process is dependent on delays in generating.
The delays that can be altered according to the needs of the user are: delay in Opening Chrome, delay in 
waiting for the page to load and delay in proceeding to the next result.

# What it cannot do

-> Cannot know if the generated combination yields a valid result or not
-> Does not use a web driver like Selenium so all process happens in foreground
-> Cannot use system/interrupt process as keystrokes are sent
-> Keystrokes are such a bad idea here or anywhere!

# What could be done

-> For god's sake IMPLEMENT A WEB DRIVER
-> By doing that, we can eliminate delays entirely
-> Make it look more sophisticated
