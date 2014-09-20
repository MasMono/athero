#CASHIER AUTHORIZATION REPORTS

##APPLICATION PURPOSE

The purpose of this application is to help managers asses cashier authorization
data per store. Everyday an email will be sent to regional/area managers
containing cashier authorization reports for stores under their command.

To achieve this goal, Pak Yosep has created a little application to query TP
Linux and send the data to `\\nakulo\datainterchange\CA`. On 9:00 am we need to do
the followings:

1. Iterate over `\\nakulo\datainterchange\CA` to find every files that are sent
   from stores.
2. On loading ca file, check whether or not we have upload the data into
   database by checking in log table for the filename.
3. Insert the data into MS Sql database.
4. Query current date data and send by email to every regional/area manager.
5. Do housekeeping for files that are 14 days old.

To manage the application we need to create a control panel application. This
application will have features as follow:

1. Modify regional/area manager and store information likewise, it means the
   following feature must exists:
    - Create new entry for regional/area and stores
    - Modify entries for regional/area and stores
    - Read entries for regional/area and stores
    - Delete entries for regional/area and stores
2. Send email on demand.
3. Housekeeping on demand.
4. Re-upload, if we have time to implement.

##CLASS DESIGN

1. Banner
    - id
    - short_desc
    - long_desc

2. Area
    - id
    - short_desc
    - long_desc
    - manager_name
    - manager_email

3. Store
    - id
    - location
    - short_desc
    - long_desc
    - manager_name
    - manager_email

4. CashierAuthLog
    - id
    - filename
    - processdate

5. CashierAuth
    - id
    - auth_type



