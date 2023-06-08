# CNN-text
CNN-text is a Python project that focuses on preprocessing the CNN-DailyMail news text summarization dataset using natural language processing (NLP) tools. The project includes scripts to create a CSV file from the BBC data, generate the preprocessed dataset, and create a word cloud based on article names.

## Dataset
### CNN-DailyMail News Text Summarization Dataset
The CNN-DailyMail news text summarization dataset used in this project is sourced from [this Kaggle dataset](https://www.kaggle.com/datasets/gowrishankarp/newspaper-text-summarization-cnn-dailymail). It contains a collection of news articles from CNN and DailyMail, along with corresponding article summaries. The dataset provides an excellent resource for text summarization research and analysis.

### BBC Dataset
[The BBC dataset](http://mlg.ucd.ie/datasets/bbc.html) used for classification in this project is sourced from the UCD Machine Learning Group. It consists of articles from the BBC website, categorized into five different classes: business, entertainment, politics, sport, and tech. The BBC dataset is utilized in conjunction with the CNN-DailyMail dataset for classification tasks.

Please note that some preprocessing has been applied to both datasets using various NLP tools as part of this project.
# Files
- **BBCDatasetCreator.py**: This script converts the BBC data into a CSV format, making it compatible with the project's preprocessing pipeline.

- **main.py**: Running this script generates the preprocessed dataset by applying various NLP techniques to the CNN-DailyMail dataset. The resulting preprocessed data can be used for further analysis and modeling.

- **WordcloudGenerator.py**: This script utilizes a dataset that includes article names to generate a word cloud visualization. The word cloud provides a visual representation of the most frequent words in the article names, allowing for quick insights into the dataset.

## Setup
1. To set up the CNN-text project, follow these steps:

2. Install Python 3.10 on your system.

3. Create a new virtual environment using Python 3.10.

4. Activate the virtual environment.

5. Navigate to the project directory.

6. Install the required dependencies using the following command:
```shell
   pip install -r requirements.txt
```
This will install all the necessary packages and libraries specified in the requirements.txt file.

## Instructions
To use the CNN-text project, follow these steps:

1. Download the CNN-DailyMail news text summarization dataset from [this Kaggle dataset](https://www.kaggle.com/datasets/gowrishankarp/newspaper-text-summarization-cnn-dailymail) link.

2. Unzip the downloaded dataset.

3. Place the unzipped dataset files into the ***'Resources/cnn_dailymail'*** directory within the CNN-text project directory.

4. Run the ***BBCDatasetCreator.py*** script to convert the BBC data into a CSV format. This step is necessary if you want to include the BBC data in your preprocessing pipeline.

5. Run the ***main.py*** script to preprocess the CNN-DailyMail dataset using various NLP tools. This will generate the preprocessed dataset, which can be used for further analysis and modeling.

6. If you want to generate a word cloud based on article names, run the ***WordcloudGenerator.py*** script. This will create a visual representation of the most frequent words in the article names.