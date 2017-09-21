# Henri

Winner of the sponsor prize ("Spot the HENRY") awarded by BNP Paribas at HackMIT 2017.

Data wrangling and project management: [@rainiera](https://github.com/rainiera)

Data visualization: [@evonneng](https://github.com/evonneng), [@rohitdatta](https://github.com/rohitdatta)

LinkedIn scraper: [@rohitdatta](https://github.com/rohitdatta)

> **DEFINITION of 'High Earners, Not Rich Yet - HENRYs'**  
> A buzzword coined in a 2003 Fortune Magazine article to refer to a segment of families earning between $250,000 and $500,000, but not having much left after taxes, schooling, housing and family costs - not to mention saving for an affluent retirement. The original article in which the "high earners, not rich yet (HENRYs)" term appeared discussed the alternative minimum tax (AMT) and how hard it hits this group of people.

**Ideas**

- LinkedIn job headline
- Emojis in tweets

# Supervised approach

We used the H1B Visa dataset.

Since "training data" or a "ground truth" doesn't really exist for finding HENRY's (finding exact income for people is tricky) we use a fuzzy rule-based imputation on the entire Henry column. This means hand-selecting some features that are prominent to our knowledge of a "HENRY" and applying a prior.

~~Once we had a "ground truth", we trained a deep feed-forward neural network to classify a HENRY.~~ (almost)

# Unsupervised approach

K-means clustering with various hyperparameters and seeing which center(s) conform to our knowledge of a "HENRY".

# Job2Vec

Because of all the different job titles that companies make up that exist on the H1B data set, we attempted word2vec on the job titles to cluster similar-sounding jobs in a vector space. However, it looks like there needed to be more context around the corpus to make it more accurate - nearest-neighbors to "ENGINEER", for example, in the vector space, weren't very promising. Even when we used the pretrained models. Oh well.

# Visualization

Deck.gl and Neo4j

### Installation process:

If you have not already, install babel on your machine
1. ```npm install -g babel```
2. ```npm install -g babel-cli```

Then install of the dependencies and webpacks necessary to run react
```bash
npm install webpack --save 
npm install webpack-dev-server --save
npm install react --save
npm install react-dom --save
npm install babel-core --save
npm install babel-loader
npm install babel-preset-react
npm install babel-preset-es2015
```

To get the server up and running
```npm start```
and then head over to http://localhost:8080
