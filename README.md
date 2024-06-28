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
