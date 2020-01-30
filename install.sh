docker pull toucantoco/backtechtest
docker run --rm -i -p 27017:27017 toucantoco/backtechtest &

python3 -m venv venv
source venv/bin/activate
echo 'source venv/bin/activate' # Tested on MacOS

pip3 install -r requirements.txt
