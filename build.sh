
#build the project
echo "Build the project..."
pip install -r requirements.txt

echo  "Make migrations"
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "collect static"
python manage.py collectstatic  --noinput --clear


