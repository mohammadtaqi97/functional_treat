arr = []
print("Welcome to Data analyser and transformer program")
print("This project allows users to \nanalyse and transform data in various ways")
while True:
    print()
    print("Main menu: ")
    print("1. Input data")
    print("2. Display data summary")
    print("3. Calculate factorial or fibonacci")
    print("4. Filter Data by Threshold")
    print("5. Sort Data")
    print("6. Display Dataset statistics")
    print("7. Exit program")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter array size: "))
        for i in range(n):
            element = int(input("Enter array element :"))
            arr.append(element)
        print(arr)

        print("Data stored succefully!")

    elif choice == 2:
        if len(arr) == 0:
            print("No data found")
        else:
            print("Data summary: ")
            print("Total elements: ",len(arr))
            print("Minimum value: ",min(arr))
            print("Maximum value: ",max(arr))
            print("Sum of all values: ",sum(arr))
            print("Average of all: ",sum(arr)/len(arr))

    elif choice == 3:
        print("1. Factorial")
        print("2. Fibonacci")
        option = int(input("Enter your choice: "))
        num = int(input("Enter your number: "))

        if option == 1:
            fact = 1
            for i in range(1,num+1): 
                fact = fact*i
            print(f"The factorial of {num} is {fact} ")

        elif option == 2:
            a = 0
            b = 1
            for i in range(num):
                print(a,end = " ")
                c = a + b 
                a = b
                b = c
            
    elif choice == 4:
        if len(arr) ==0:
            print("NO DATA FOUND!")

        else:
            threshold = int(input("Enter threshold value: "))
            print("Filtered data ")
            print("1. Above threshold")
            print("2. Below threshold")
            fil = int(input("Enter your choice: "))
            if fil == 1:
                result = []
                for j in arr:
                    if j > threshold:
                        result.append(j)
                print(f"Elements above {threshold} : {result}")
            else:
                result = []
                for j in arr:
                    if j< threshold:
                        result.append(j)
                print(f"Elements below {threshold} : {result}")

    elif choice == 5:
        if len(arr) == 0:
            print("NO DATA FOUND!")
        else:
            print("Enter sorting option ")
            print("1. Ascending")
            print("2. Descending")

            opt = int(input("Enter your choice: "))
            if opt == 1:
                arr.sort()
                print(arr)
                
            else:
                arr.reverse()
                print(arr)
                
    elif choice == 6:
        print("Dataset statistics: ")
        print("Minimum value: ",min(arr))
        print("Maximum value: ",max(arr))
        print("Sum of all value: ",sum(arr))
        print("Average of all value: ",sum(arr)/len(arr))

    elif choice == 7:
        print("Thank you for using the Data Analyser\nand Transformer program.\nGoodbye!")