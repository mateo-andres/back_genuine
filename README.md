python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m pip freeze > requirements.txt
uvicorn main:app --reload
