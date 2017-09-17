# Henri

> **DEFINITION of 'High Earners, Not Rich Yet - HENRYs'**  
> A buzzword coined in a 2003 Fortune Magazine article to refer to a segment of families earning between $250,000 and $500,000, but not having much left after taxes, schooling, housing and family costs - not to mention saving for an affluent retirement. The original article in which the "high earners, not rich yet (HENRYs)" term appeared discussed the alternative minimum tax (AMT) and how hard it hits this group of people.

- LinkedIn job headline
- Emojis in tweets

# Supervised approach

Since "training data" or a "ground truth" doesn't really exist for finding HENRY's (finding exact income for people is tricky) we use a fuzzy rule-based imputation on the entire Henry column. This means hand-selecting some features that are prominent to our knowledge of a "HENRY" and applying a prior.

Once we had a "ground truth", we trained a deep feed-forward neural network to classify a HENRY.

# Unsupervised approach

K-means clustering with various hyperparameters and seeing which center(s) conform to our knowledge of a "HENRY".

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
