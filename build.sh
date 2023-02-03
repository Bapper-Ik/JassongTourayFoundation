
#build the project
echo "Build the project..."
python3.11.1 -m pip install -r requirements.txt

echo  "Make migrations"
python3.11.1 manage.py makemigrations --noinput
python3.11.1 manage.py migrate --noinput

echo "collect static"
python manage.py collectstatic  --noinput --clear


