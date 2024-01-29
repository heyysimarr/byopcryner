from flask import Flask, render_template, request
from markupsafe import Markup
import spacy
from spacy import displacy

app = Flask(__name__)

HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""


custom_model_directory_unigram = '/Users/simar/Downloads/BYOP_CryNER/output_single/model-best'
custom_model_directory_bigram = '/Users/simar/Downloads/BYOP_CryNER/output_bigram/model-best'
custom_model_directory_trigram = '/Users/simar/Downloads/BYOP_CryNER/output_trigram/model-best'

crypto_ner_model_unigram = spacy.load(custom_model_directory_unigram)
crypto_ner_model_bigram = spacy.load(custom_model_directory_bigram)
crypto_ner_model_trigram = spacy.load(custom_model_directory_trigram)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extract', methods=["GET", "POST"])
def extract():
    if request.method == 'POST':
        raw_text = request.form['rawtext']

        doc_unigram = crypto_ner_model_unigram(raw_text)
        html_unigram = displacy.render(doc_unigram, style="ent")
        html_unigram = html_unigram.replace("\n\n", "\n")
        result_unigram = Markup(HTML_WRAPPER.format(html_unigram))

        doc_bigram = crypto_ner_model_bigram(raw_text)
        html_bigram = displacy.render(doc_bigram, style="ent")
        html_bigram = html_bigram.replace("\n\n", "\n")
        result_bigram = Markup(HTML_WRAPPER.format(html_bigram))

        doc_trigram = crypto_ner_model_trigram(raw_text)
        html_trigram = displacy.render(doc_trigram, style="ent")
        html_trigram = html_trigram.replace("\n\n", "\n")
        result_trigram = Markup(HTML_WRAPPER.format(html_trigram))

    return render_template('result.html', rawtext=raw_text, result_unigram=result_unigram, result_bigram=result_bigram, result_trigram=result_trigram)

@app.route('/previewer')
def previewer():
    return render_template('previewer.html')

@app.route('/preview', methods=["GET", "POST"])
def preview():
    if request.method == 'POST':
        newtext = request.form['newtext']
        result = newtext

    return render_template('preview.html', newtext=newtext, result=result)

if __name__ == '__main__':
    app.run(debug=True)
