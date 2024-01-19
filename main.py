from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Простейшая база данных для хранения вопросов и ответов
questions = [
    {'id': 1, 'title': 'Как использовать Flask?', 'content': 'Я новичок и я не знаю?(('},
    {'id': 2, 'title': 'Как использовать Django?', 'content': 'Я новичок и я не знаю?(('}
]

answers = [
    {'id': 1, 'question_id': 1, 'answer': 'Просто скачай Flask через команду pip install flask'},
    {'id': 2, 'question_id': 2, 'answer': 'Просто скачай Django через команду pip install django'}
]


# главная страница
@app.route('/')
def home():
    return render_template('index.html', questions=questions)

# Страница с деталями вопроса и ответами для вопросa
@app.route('/question/<int:question_id>')
def question(question_id):
    question = next((q for q in questions if q['id'] == question_id), None)
    if question:
        question_answers = [a for a in answers if a['question_id'] == question_id]
        return render_template('question.html', question=question, answers=question_answers)
    else:
        return 'Вопрос не найден'

# Старница для добавления нового вопроса
@app.route('/ask', methods=['GET', 'POST'])
def ask():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        new_question = {
            'id': len(questions) + 1,
            'title': title,
            'content': content
        }

        questions.append(new_question)
        return redirect(url_for('home'))
    else:
        return render_template('ask.html')

app.run()
