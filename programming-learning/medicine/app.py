import os
import sys
from flask import Flask, render_template, request

# Path fix taaki module errors na aayein
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

try:
    from medicine import get_medicine_info
    from symptom import get_suggestion
except ImportError as e:
    print(f"Error importing modules: {e}")

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    search_type = None
    query = ""

    if request.method == 'POST':
        query = request.form.get('query')
        search_type = request.form.get('type')

        if search_type == 'medicine':
            result = get_medicine_info(query)
        else:
            result = get_suggestion(query)

    return render_template('index.html', result=result, search_type=search_type, query=query)

if __name__ == '__main__':
    # FIX: use_reloader=False dene se signal error khatam ho jayega
    app.run(debug=True, use_reloader=False)