from flask import Flask,render_template,request
import pickle
popular_df = pickle.load(open('popular.pkl','rb'))
pt=pickle.load(open('pt.pkl','rb'))
books=pickle.load(open('books.pkl','rb'))
similarity_score=pickle.load(open('similarity_scores.pkl','rb'))



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',book_name = list(popular_df['Book-Title'].values), author = list(popular_df['Book-Author'].values), image = list(popular_df['Image-URL-M'].values),votes = list(popular_df['num_ratings'].values),rating = list(popular_df['avg_ratings'].values))

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books',methods=['post'])
def recommend():
    user_input = request.form.get('user_input')
    return str(user_input)


if __name__=='__main__':
    app.run(debug=True)