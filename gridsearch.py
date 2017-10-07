# Creation of train and test for the entire exercise

from sklearn.cross_validation import train_test_split
y = data.pop('<<Your target variable>>')
X = data
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.3, random_state=42)


# Libraries needed:

from time import time
from operator import itemgetter
from scipy.stats import randint as sp_randint

from sklearn.grid_search import GridSearchCV, RandomizedSearchCV
from sklearn.datasets import load_digits
from sklearn.ensemble import RandomForestClassifier


# Creation a base classifier

clf = RandomForestClassifier(n_estimators=200)

# Function to report the top three classifiers after the grid search

def report(grid_scores, n_top=3):
    top_scores = sorted(grid_scores, key=itemgetter(1), reverse=True)[:n_top]
    for i, score in enumerate(top_scores):
        print("Model with rank: {0}".format(i + 1))
        print("Mean validation score: {0:.3f} (std: {1:.3f})".format(
              score.mean_validation_score,
              np.std(score.cv_validation_scores)))
        print("Parameters: {0}".format(score.parameters))
        print("")



# Spicifying the parameters which need to be tuned by the grid search

param_dist = {"max_depth": [3, None],
              "max_features": sp_randint(1, 11),
              "min_samples_split": sp_randint(1, 11),
              "min_samples_leaf": sp_randint(1, 11),
              "bootstrap": [True, False],
              "criterion": ["gini", "entropy"]}

# running a randomized search on the grid when it is not possible to go through the entire theta space
n_iter_search = 20
random_search = RandomizedSearchCV(clf, param_distributions=param_dist,
                                   n_iter=n_iter_search)

start = time()
random_search.fit(X_train1, y_train1)
print("RandomizedSearchCV took %.2f seconds for %d candidates"
      " parameter settings." % ((time() - start), n_iter_search))
report(random_search.grid_scores_)


# Running the full grid search

grid_search = GridSearchCV(clf, param_grid=param_grid)
start = time()
random_search.fit(X_train1, y_train1)
print("RandomizedSearchCV took %.2f seconds for %d candidates"
      " parameter settings." % ((time() - start), n_iter_search))
report(random_search.grid_scores_)


# Running random forest for the tuned parameters
# Please specify the right parameters after looking at the top models

rf = RandomForestClassifier(n_estimators=200,bootstrap= True, min_samples_leaf= 3, min_samples_split= 3, criterion= 'entropy', max_features= 10, max_depth= None)
rf.fit(X_train, y_train)

## Printing the feature importances

pd.DataFrame({'Feature_Name':X_train1.columns, 'Relative_Importance':rf.feature_importances_})








