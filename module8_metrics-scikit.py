
import numpy as np
from sklearn.metrics import precision_score, recall_score

def main():
    N = int(input("Enter the number of points (N): "))
    
    X = np.zeros(N, dtype=int)
    Y = np.zeros(N, dtype=int)
    
    for i in range(N):
        x, y = input(f"Enter x and y for point {i+1} (separated by space): ").split()
        X[i] = int(x)
        Y[i] = int(y)
        
    precision = precision_score(X, Y)
    recall = recall_score(X, Y)
    
    # Output Precision and Recall
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")

if __name__ == "__main__":
    main()
