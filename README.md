CryNER is a named entity recognition (NER) model developed to identify cryptocurrency-related entities in text. The model uses three different approaches—unigram, bigram, and trigram detection—to accurately recognize and classify terms associated with cryptocurrencies. The project includes the development of a Flask-based web interface to facilitate user interaction with the models.

## Model Architecture

1. **Data Preprocessing**
   - Cleaning data by removing null and duplicate values.
   
2. **Exploratory Data Analysis**
   - Analyzing data to extract meaningful insights.

3. **Training Data Preparation**
   - Annotation of data (around 26,000 entries) using basic programming.
   - Creating a DocBin object to store and serialize spaCy documents.
   - Saving the DocBin object to disk in `.spacy` format for training.

4. **Model Training**
   - Training models for unigram, bigram, and trigram detection.

5. **Deployment**
   - Using Flask to deploy the models via a web interface.

## Final Deliverables

1. **Text Detection System**
   - Three NER models for unigram, bigram, and trigram detection of cryptocurrency-related content in text.

2. **Flask Website Interface**
   - A web interface with a text input area allowing users to input text and identify n-grams separately.

## Abstract and Methodology

CryNER aims to detect cryptocurrency-related entities in text. For example, in the text: “At its core, cryptocurrency leverages blockchain technology—a decentralized and transparent ledger—to facilitate secure transactions,” the model would identify words like `cryptocurrency` and `ledger` and label them as crypto.

### Dataset
- Crypto Headlines + NER Model -https://www.kaggle.com/datasets/kaballa/cryptoner-ml-model

## Tech Stack

- **Python**: Core programming language.
- **Jupyter Notebook**: Environment for code and markdowns.
- **Pandas**: Data manipulation library.
- **spaCy3**: NLP library for NER.
- **Matplotlib**: Library for data visualization.
- **Flask**: Web framework for developing the web interface.
- **HTML/CSS**: For structuring and styling the web interface.
- **JSON**: For storing annotations.
- **NumPy**: For numerical operations.
- **tqdm**: For progress bars.
- **re (Regular Expressions)**: For text processing.
- **Git**: For version control.
  
## Results

### Unigram Model
- Identifies single cryptocurrency entities.

### Bigram Model
- Identifies phrases containing two cryptocurrency-related terms.

### Trigram Model
- Identifies phrases containing three cryptocurrency-related terms.

---

This README provides an overview of the CryNER project, including the model architecture, methodology, tech stack, and deliverables. It aims to be informative for viewers and collaborators referring to this repository.





  
