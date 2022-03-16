from flask import Flask, render_template, redirect, request
from wordsnips import word_value_calc, cap_and_strip, anagram_checker, caesar_all, scrabble_word_value_calc
from wordsnips import load_words, check_english
from numbersnips import clean_integer, is_prime, is_square, is_cube, is_fibonacci, is_triangular, factors
import sqlite3

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# sql inquiry simplification
# from https://stackoverflow.com/questions/21883119/how-to-count-number-of-records-in-an-sql-database-with-python
def numlet_sql(sqlcommand):
    """returns db result of an sql command to numletter db"""
    db = sqlite3.connect("numletter.db")
    cursor = db.cursor()
    cursor.execute(sqlcommand)
    return cursor.fetchall()


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/words/')
def words():
    return render_template("words.html")


@app.route('/numbers/')
def numbers():
    return render_template("numbers.html")


@app.route('/extras/')
def extras():
    return render_template("extras.html")


@app.route('/words/wv', methods=["GET", "POST"])
def wordswv():
    if request.method != "POST":
        wvword = ''
        return render_template("words/wv.html", wvword=wvword)
    wvin = request.form["wv"]
    scale = request.form["scale"]
    wvout = word_value_calc(wvin)
    wvscrabble = scrabble_word_value_calc(wvin)
    wvword = str(wvout[0])
    if wvword != '':
        wvvalue = str(wvout[1])
        reversewvvalue = str(wvout[2])
        return render_template("words/wv.html", wvword=wvword, wvvalue=wvvalue, reversewvvalue=reversewvvalue,
                               wvscrabble=wvscrabble, scale=scale)
    else:
        error = "Please enter a valid word."
        wvword = ''
        return render_template("words/wv.html", error=error, wvword=wvword)


@app.route('/words/anach', methods=["GET", "POST"])
def wordsanach():
    if request.method != "POST":
        return render_template("words/anach.html")
    sc1in = request.form["sc1"]
    sc2in = request.form["sc2"]
    if sc1in == '' or sc2in == '':
        result = "Please type 2 strings then hit Enter"
        return render_template("words/anach.html", res1=result, res2='', res3='')
    result = anagram_checker(sc1in, sc2in)
    return render_template("words/anach.html", res1=result[0], res2=result[1], res3=result[2])


@app.route('/words/caesar', methods=["GET", "POST"])
def wordscaesar():
    if request.method != "POST":
        return render_template("words/caesar.html")
    input = cap_and_strip(request.form["caes_string"])
    if len(input) == 0:
        error = "Please enter a valid string."
        return render_template("words/caesar.html", error=error)
    output, english = caesar_all(input)  # listof (key, result) tuples
    length = len(english)
    dictcite = "Dictionary from https://github.com/dwyl/english-words/blob/master/read_english_dictionary.py"
    return render_template("words/caesar.html", error="", keytitle="ROT",
                           valuetitle="Rotated string", output=output, input=input, english=english, length=length,
                           dictcite=dictcite)


@app.route('/words/letrep', methods=["GET", "POST"])
def wordsletrep():
    if request.method != "POST":
        return render_template("words/letrep.html")
    selection = request.form.getlist("letlist")
    result = ",".join(selection)
    sq = "SELECT " + result + " FROM letters"
    result = numlet_sql(sq)
    return render_template("words/letrep.html", selection=selection, result=result)


@app.route('/numbers/ffnum', methods=["GET", "POST"])
def numbersfunfacts():
    if request.method != "POST":
        num = False
        return render_template("numbers/ffnum.html", num=num)
    num = clean_integer(request.form["plainnum"])
    if not num:
        return render_template("numbers/ffnum.html", output='Invalid input - please try again.', num=num)
    if len(num) > 7:
        num = False
        return render_template("numbers/ffnum.html", output='Please enter a smaller number (max 7 digits).', num=num)
    num = int(num)
    prime = is_prime(num)
    fib = is_fibonacci(num)
    triangular = is_triangular(num)
    factorlist = factors(num)
    faclistlen = len(factorlist)
    faclist = factorlist[:-1]
    faclistlast = factorlist[-1]
    if prime:
        square = ''
        cube = ''
    else:
        square = is_square(num)
        cube = is_cube(num)
    return render_template("numbers/ffnum.html", num=num, prime=prime, square=square, cube=cube, fib=fib,
                           triangular=triangular, faclist=faclist, faclistlast=faclistlast, faclistlen=faclistlen)


@app.route('/numbers/numrep', methods=["GET", "POST"])
def numbersnumrep():
    if request.method != "POST":
        return render_template("numbers/numrep.html")
    selection = request.form.getlist("numlist")
    result = ",".join(selection)
    sq = "SELECT " + result + " FROM numbers"
    result = numlet_sql(sq)
    return render_template("numbers/numrep.html", selection=selection, result=result)


@app.route('/extras/reference', methods=["GET"])
def reference():
    return render_template("extras/reference.html")


@app.route('/extras/links', methods=["GET"])
def links():
    return render_template("extras/links.html")


if __name__ == '__main__':
    app.run(debug=True)
