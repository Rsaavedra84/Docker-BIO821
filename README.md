<H3><center> Final project - BIO821 </H3></center>
<H4><center>Joaquin Menendez (jm622)</H4></center>

To run the scripts and the notebooks we suggest using a Docker container.
**Warning!** You should have at least 4 Gb of free space.

The first step is setting **three environment variables**.
You should add your tokens for:
- KAGGLE_KEY
- KAGGLE_USERNAME
- MAPBOX_PRIVATE_TOKEN

**How to do this?**<br>
You will need to open your .bashrc file. Usually, this is located
in the following path `~/.bashrc` <br>
You can open the file typing `nano ~/.bashrc`. Write in the first line the following
```
export KAGGLE_KEY=<your_kaggle_key>
export KAGGLE_USERNAME=<your username>
export MAPBOX_PRIVATE_TOKEN=<your token>
```
Save the file and you are ready to run the Docker container

**Where do I get this tokens?**<br>
For the Kaggle variables check [here](https://github.com/Kaggle/kaggle-api#api-credentials) <br>
For the MapBox token check [here](https://docs.mapbox.com/api/#access-tokens-and-token-scopes)<br>

**Done, how should I proceed?**
clone this repository into your local machine
Inside the repository open a terminal and type:
```
docker build -t kaggle docker/.
```
*(this could take some time)*
```
bash docker/run_docker
```
Click on the last link that appears in the terminal
and a Jupyter notebook GUI will appear in your web browser.

**Some useful Docker commands**<br>

>docker ps (show all the running containers)<br>
docker images (show all the images in your local machine)<br>
docker rmi <IMAGE-ID> (removes the images from the local machine)<br>
docker stops <NAME> (stops the selected container)<br>

**I cannot install Docker (or you have a Windows SO)**<br>
Another alternative:
You should have the following programs and libraries installed in your local machine
- Python 3
    - os
    - matplotlib
    - pandas
    - seaborn
    - requests
    - sqlalchemy
    - jupyter notebooks
- SQLite<br>

You would need to  add your tokens manually into the following scripts: `mapbox/Country.py`  `augmented_data.py` and `decompress_soccer_v2.sh` <br>
 
If you have any doubt, please let me know. <br>
:email: [joaquin14@gmail.com](:mailto:joaquin14@gmail.com)
 
