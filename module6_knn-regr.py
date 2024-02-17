
import numpy as np

def main():
    N = int(input("Enter the number of points N: "))
    k = int(input("Enter the number of nearest neighbors k: "))
    
    # Validate k
    if k > N:
        print("Error: k cannot be greater than N")
        return
    
    # Initialize arrays to store points
    points = np.zeros((N, 2))
    
    # Read N points from the user
    for i in range(N):
        x = float(input(f"Enter x value for point {i+1}: "))
        y = float(input(f"Enter y value for point {i+1}: "))
        points[i] = [x, y]
    
    X = float(input("Enter the input X value: "))
    
    # Calculate distances from the input X to each point's X
    distances = np.sqrt((points[:, 0] - X)**2)
    
    # Find the indices of the k nearest neighbors
    nearest_indices = np.argsort(distances)[:k]
    
    # Compute the average Y value of the k nearest neighbors
    Y = np.mean(points[nearest_indices, 1])
    
    print(f"The result (Y) of k-NN Regression is: {Y}")

if __name__ == "__main__":
    main()
