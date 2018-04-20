echo
echo "This installation sets up a new Ubuntu, installs all necessary packages"
echo "The whole installation time is about 10-15 minutes."
echo

read -p "Do you wish to continue (yes/no)? " yn
case $yn in
    [Nn]* ) exit;;
esac

cd ~

#Install anaconda
wget https://repo.continuum.io/archive/Anaconda3-4.2.0-Linux-x86_64.sh
bash Anaconda3-4.2.0-Linux-x86_64.sh
echo 'export PATH="~/anaconda3/bin:$PATH"' >> ~/.bashrc 

# Refresh basically
source .bashrc

conda update conda


sudo apt-get update && sudo apt-get -y dist-upgrade
sudo apt-get update

# Install dependencies
sudo apt install unzip
sudo apt-get update && sudo apt-get -y dist-upgrade

# Install 
sudo apt-get install libcupti-dev
pip install --upgrade pip
sudo apt-get update && sudo apt-get -y dist-upgrade
pip install --upgrade keras numpy scipy sklearn pandas
pip install plotly 
pip install hdbscan
pip install umap-learn
pip install isoweek
pip install pandas_summary
pip install cufflinks
pip install pyLDAvis
pip install gensim
pip install --upgrade gensim
pip install keras
sudo apt-get update && sudo apt-get -y dist-upgrade
pip install bcolz
pip install psycopg2
pip install Scrapy
python -m spacy download en_core_web_lg
python -m spacy.en.download all
spacy download en_vectors_web_lg

sudo apt-get update && sudo apt-get -y dist-upgrade
# to re install one need to clean first 
# make clean
sh ./build.sh
# Compl ./build.sh
cd ~
eted. Some notes to remember:
echo
echo "CONFIGURATION COMPLETE"
