
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score

def main():
    N = int(input("Enter the number of points (N): "))
    

    k = int(input("Enter the number of nearest neighbors (k): "))
    
    if k > N:
        print("Error: k should be less than or equal to N")
        return
    
    points = np.zeros((N, 2))
    
    for i in range(N):
        x = float(input(f"Enter x value for point {i+1}: "))
        y = float(input(f"Enter y value for point {i+1}: "))
        points[i] = [x, y]
    
    X = points[:, 0].reshape(-1, 1)  # Features need to be 2D for scikit-learn
    y = points[:, 1]  # Target values
    
    X_pred = float(input("Enter X to predict Y: "))
    X_pred = np.array([[X_pred]])  # Needs to be 2D
    
    knn_regr = KNeighborsRegressor(n_neighbors=k)
    knn_regr.fit(X, y)
    Y_pred = knn_regr.predict(X_pred)
    
    print(f"Predicted Y: {Y_pred[0]}")
    
    # Calculate and print R2 score
    y_true_pred = knn_regr.predict(X)
    r2 = r2_score(y, y_true_pred)
    print(f"Coefficient of determination: {r2}")

if __name__ == "__main__":
    main()
