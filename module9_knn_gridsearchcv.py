
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def main():
    N = int(input("Enter the number of training pairs N: "))
    training_data = []
    for i in range(N):
        x = float(input(f"Enter x value for pair {i+1}: "))
        y = int(input(f"Enter y value for pair {i+1}: "))
        training_data.append((x, y))
    
    M = int(input("Enter the number of test pairs M: "))
    test_data = []
    for i in range(M):
        x = float(input(f"Enter x value for pair {i+1}: "))
        y = int(input(f"Enter y value for pair {i+1}: "))
        test_data.append((x, y))
    
    # Convert lists to numpy arrays
    train_array = np.array(training_data)
    test_array = np.array(test_data)
    
    # Splitting data into features and labels
    X_train = train_array[:, 0].reshape(-1, 1)
    y_train = train_array[:, 1]
    X_test = test_array[:, 0].reshape(-1, 1)
    y_test = test_array[:, 1]
    
    # Defining the model and parameters for grid search
    knn = KNeighborsClassifier()
    param_grid = {'n_neighbors': list(range(1, 11))}
    
    grid_search = GridSearchCV(knn, param_grid, cv=5, scoring='accuracy')
    grid_search.fit(X_train, y_train)
    
    best_k = grid_search.best_params_['n_neighbors']
    best_model = grid_search.best_estimator_
    
    predictions = best_model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    
    print(f"The best k is: {best_k} with test accuracy: {accuracy}")

if __name__ == "__main__":
    main()
