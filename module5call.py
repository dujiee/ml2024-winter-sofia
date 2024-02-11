
from module5_mod import NumberTracker

def main():
    tracker = NumberTracker()
    
    N = int(input("Enter the number of inputs N: "))
    for _ in range(N):
        num = int(input("Enter number: "))
        tracker.add_number(num)
    
    X = int(input("Enter the number X to find: "))
    result = tracker.find_index(X)
    print(result if result != -1 else "-1")

if __name__ == "__main__":
    main()
