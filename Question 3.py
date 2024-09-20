def main():
    a = input("Enter numbers:")
    array = list(map(float, a.split()))

    average = sum(array) / len(array)
    
    greater = sum(1 for x in array if x > average)
    
    print(f"The average is:{average}")
    print(f"Number of elements greater than the average:{greater}")

if __name__ == "__main__":
    main()
