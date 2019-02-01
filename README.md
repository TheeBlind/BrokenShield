```
 _               _                  _     _      _     _ _ 
| |__  _ __ ___ | | _____ _ __  ___| |__ (_) ___| | __| | |
| '_ \| '__/ _ \| |/ / _ \ '_ \/ __| '_ \| |/ _ \ |/ _` | |
| |_) | | | (_) |   <  __/ | | \__ \ | | | |  __/ | (_| |_|
|_.__/|_|  \___/|_|\_\___|_| |_|___/_| |_|_|\___|_|\__,_(_)
                                                           


          ````````````````````````````````    
         /MyyyyyyyyyyyyyyyyyyyyyyyyyyyyydN    
         /M`:yyyyo       /yyyyyyyyyyyys +N    
         :M.+MMMMMd`     `dMMMMMMMMMMMN`oN    
         -M-:MMMMMMm-     `dMMMMMMMmyo/ sm    
         `M/.MMMMMMMM+     `hdyo/--/shh hh    
          ms NMMMMMMMMy      -shNMMMMMy ms    
          ym yMMMMMMMMMd.    `dMMMMMMM+`M/    
          :M.:MMMMMMNdyo-     `dMMMMMM./M.    
           ms mMMN/.:+o`    +yo`hMMMMd yd     
           +N`/MMMd`+MMm-   /MMs`++++-`N+     
            my hMMMm./MMM+   /MMmddmy sm`     
            -M/`mMMMm`:MMMh.  +MMMMN.-M/      
             +N-.mmo.+mMMMMN/  oMMM:`ms       
              +N:`.sNMMMMMMMMy` sN:.my        
               :No`oNMMMMMMMMMm- `:No         
                `ym/`omMMMMMMNy--hd-          
                  .sms:-+yy+:-odh:            
                     :sdhsyhds/`              
                         .`                                                
```                                                                                               

This tool was build for easily access information released on the internet through a db which preserves them for us.
The database is feeded with public accessible information relased from third parts.

The construction of the current database is for information and research purposes only.

### Installation

```pip3 install psycopg2-binary termcolor pyfiglet colorama progressbar```

```python3 Brokenshield.py```

### Usage

To access our database use the data provided to authenticate you, or use your own to connect to your db.

If you build your own db,

the tool is configured by default to integrate with postgresql,you can load the data and look for them directly through the menu.

Psuh new data to the server:

![alt text](https://i.imgur.com/UBvlRsp.png)


You can select from the menù the field of research.

For example

```Select what you want to search or press q for quit
 0) USERNAME
 1) DOMAIN
 2) PASSWORD
 3) WRITE FROM FILE
 4) CHANGE TABLE
 5) QUIT

  choice: 1

username selected

Write the username: test
I have found this:

username: test
e-mail: test@test.test
password: test
```

you can edit the queries in the source code to make it better adapt to your db.

###### Push new data to BrokenShield db

The data entered in the database are collected from public sources and sorted in the following format:

```┊username┊domain.ccTLD┊password┊```

this to avoid bad formatting using special characters commonly used in passwords like the following:

```" !#$%&'()*+,-./:;<=>?@[\]^_`{|}~```

to send new data to our db, 
these data to be accepted must comply with the following requirements:

1. Have been publicly released previously (website,forum,paste direct data link must be attached)
2. It must have been cleaned up and ordered
3. Use this character as a separator```┊```
4. BrokenShield DB do not accept cc or any financial data


### TODO

new menù queries that still need to be added:

* Phone
* IP

### request access to brokenshield db
Send me a message on twitter, I took the request into consideration.

### BrokenShield DB is actual under development and update

