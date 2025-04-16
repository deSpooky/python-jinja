from flask import Flask, render_template

app = Flask(__name__)

@app.route('/about')
def about():
    skills = ['Python', 'HTML/CSS', 'JS/Node.JS', 'MySQL', 'И еще много всего..']
    hobbies = [
        { "category": "Музыка", "items": ['Барабаны', 'Бас'] },
        { "category": "Спорт", "items": ['Йога', 'Кардио'] },
    ]
    return render_template('about.html', skills=skills, hobbies=hobbies)

if __name__ == '__main__':
    app.run(debug=True)
