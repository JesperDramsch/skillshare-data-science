from pathlib import Path

nb = Path("notebooks")

github_stem = "jesperdramsch/skillshare-data-science/"
github_nb   = "blob/master/notebooks/"
github_url  = "https://github.com/"
colab_url   = "https://colab.research.google.com/github/"

chapters = { "0": "Data Loading",
             "1": "Data Cleaning",
             "2": "Exploratory Data Analysis",
             "3": "Machine Learning",
             "4": "Machine Learning Validation",
             "5": "Data Visualization",
             "6": "Report Generation"
}

current = None

## Head
string = f"""# Skillshare Data Science and Business Analytics in Python
[Skillshare - Data Science and Business Analytics with Python](https://skl.sh/2CROaFi) 
2-month Free Trial of Skillshare Premium for this course and many many others\n
[Download these Notebooks]({github_url}{github_stem}archive/master.zip)\n"""

## TOC

string += "---\n\n"
for num in range(7):
    string += f"{num}. [{chapters[str(num)]}](#{chapters[str(num)].lower().replace(' ','-')})\n"
string += "\n---\n"

## Description
string += """Business analytics and data science have become important skills across all industries. Knowing both how to perform analytics, as well as, sense checking analyses and understanding concepts is key in making decisions today.

Python has become the lingua franca of data science and is, therefore, the topic of this class. 

Programming can be intimidating, however, Python excels due to its readability and being freely available for all platforms including Linux, Mac and Windows. This class will assume some prior knowledge of Python syntax, but to establish a common learning environment some of the basics will be covered. We will cover the full data science workflow including:

- Loading data from files (e.g. Excel tables) and databases (e.g. SQL servers)
- Data cleaning
- Exploratory data analysis
- Machine learning
- Model validation and churn analysis
- Data visualization and report generation
In this class we will  use freely and openly available Python libraries including: Jupyter, NumPy, SciPy, Pandas, MatPlotLib, Seaborn, and Scikit-Learn and you will also learn how to quickly learn new libraries.\n
## Notebooks
Click the "notebok" badge to view or the "colab" badge to try out the notebooks interactively.\n
"""

## Notebooks
for f in nb.glob("*.ipynb"):
    title = f.stem
    file_name = f.name.replace(" ","%20")
    colab_link = colab_url + github_stem + github_nb + file_name

    if not str(current) == title[0]:
        current = title[0]
        string += f"## {chapters[current]}\n"

    string += f"""### {title.split("- ")[1]}\n
[![](https://img.shields.io/badge/view-notebook-orange)](notebooks/{file_name}) [![](https://img.shields.io/badge/open-colab-yellow)]({colab_link})\n
"""

## Class Project
string += """## Class Project
Create a PDF report of a data analysis in Python with at least one visualization.

Assignment: Use a dataset you have from a project you are working on. Prepare and analyze this data and create at least one meaningful visualization. The data could be sales, expenses, or your FitBit data! Make sure to anonymize the data in case anything is sensitive information! (If you don’t have any data, I have some data listed and even a data set you can use below!)

Deliverable: Create a Jupyter Notebook describing your analysis process that contains at least one visualization that tells a compelling story.

Details: The project will consist of loading data and performing the exploratory data analysis and visualizations outlined in the class. The project is relatively straight-forward, as the class will follow an applied structure that can be revisited for parts of the project analysis.

Students are encouraged to use their own datasets for the analysis, as these yield the most benefit in learning. Alternatively, it is also possible to search for data sets in the following places:

- OpenML: <https://www.openml.org/search?type=data>
- Google: <https://datasetsearch.research.google.com/>
- Amazon: <https://registry.opendata.aws/>
- Kaggle: <https://www.kaggle.com/datasets>
- Awesome Data: <https://github.com/awesomedata/awesome-public-datasets>

In addition, to encourage sharing, I will provide one example data set on Skillshare, where people can explore and apply the learnings from this class. This dataset contains California Housing Sales from the 1990 census.

Help each other! Data science thrives from collaboration. Students are encouraged to learn from each other and give feedback on tips and tricks they found during their own analysis. Use the project tab early and often and also check what others have accomplished and leave feedback and likes.

Installing all the libraries: When you have conda installed, you can easily use the environment.yml in the notebooks.zip it contains all libraries. Open it with a text editor to see the command to get the environment set up.
"""


with open("Readme.md", mode="w", encoding="utf-8") as f:
    f.write(string)