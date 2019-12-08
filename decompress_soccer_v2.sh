#!/usr/bin bash

function  download {
  #Download the European Soccer dataset from Kaggle (kaggle.com/hugomathien/soccer)
  #The function ask the user for the Kagle's username and key (for a detailed instrucion of how to get this check the
  # README.md
  # 1 argument : str [Name of the dataset]
  # 2 argument: str [Name of the md5 file]
  # 3 argument(optative) : str [Move the dataset to a existing folder (i.e.  './data')]
  # 4 argument(optative) : str "d" [decompress the file (it will decompress the file in the new location)]
  export KAGGLE_USERNAME=$KAGGLE_USERNAME
  export KAGGLE_KEY=$KAGGLE_KEY
  if [[ ! -e $1 ]]; then
    /opt/conda/bin/kaggle datasets download --force hugomathien/soccer -w #./ will download inside the repo
    mv soccer.zip $1 #rename the file
  else echo 'The dataset already exist'
    #return 1
  fi

  if [[ ! -e $2 ]]; then
    wget -O $2 "https://gitlab.oit.duke.edu/bios821/european_soccer_database/raw/master/esdb.md5"
  else echo 'The MD5 file already exist'
    #return 1
  fi

  md5_file=$(echo $(md5sum $1) | cut -f 1 -d ' ')
  md5_hash=$(echo $(cat $2) | cut -f 1 -d ' ')
        if [[ $md5_file = $md5_hash ]]; then  #If hash match proceed
            echo 'Hash file and md5 hash match ('$md5_file' | '$md5_hash')'
                if [[ ! -z $3 ]]; then  #if there is a third argument...
                  mv $1 $(echo $3'/'$1)
                  cd $3
                  if [[ $4 = 'd' ]];then
                    unzip $1
                  fi
                fi
        else echo 'The hash of the database does not match with the md5 file. Check the links (database line , md5 line )'
        return 1
        fi
}
download "$@"
