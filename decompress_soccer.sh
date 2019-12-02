#!/usr/bin bash

# 1. Takes 3 positional parameters. 2. Conditionally downloads the file:
#https://gitlab.oit.duke.edu/bios821/european_soccer_database/raw/master/esdb.md5
# and stores it according to one of the positional parameters, if and only if it does not already
# exist. 3. The other 2 positiional parameters should be used to optionally move and decompress
# the database already on disk (i.e. soccer.zip). Only execute this code if the md5 sum within the
# esdb.md5 file matches that of the database you downloaded (i.e. soccer.zip).

function  download { 
  #download after checking file does not exist (to don't download again).
  read -p 'Kaggle Username: '
  export KAGGLE_USERNAME="$REPLY"
  read -p 'Kaggle Key: '
  export KAGGLE_KEY="$REPLY"
  if [[ ! -e $1 ]]; then
    echo 'Free'
    #~/.local/bin/kaggle datasets download --force hugomathien/soccer -f "$1" #./ will download inside the repo
  else echo 'The dataset already exist'
    return 1
  fi

  if [[ ! -e $2 ]]; then
    echo 'Free'
    curl -o $2 "https://gitlab.oit.duke.edu/bios821/european_soccer_database/raw/master/esdb.md5"
  else echo 'The file already exist'
    return 1
  fi



  #move and decompress the database
  #mkdir data  #Maybe give the chance to set this as a variable
  #mv  soccer.zip "$2"
  #unzip soccer.zip -d data
}


download "$@"
