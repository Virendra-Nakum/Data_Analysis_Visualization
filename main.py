import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Data_Analyzer():

    def __init__(self):
        self.data = None
        self.graph = None

    def load_data(self):
        try:
            path = input("Enter Dataset Path (e.g. data/sales_data.csv): ").strip()
            self.data = pd.read_csv(path)
            print("Dataset Loaded Successfully!")
            return self.data
        except :
            print("Invalid File Name:")
 
    def explore_data(self) :

        if self.data is None:
            print("Please Load the Dataset First!")
            return
        elif self.data.empty:
            print("Dataset Is Empty!")
            return

        print("=== Explore Data ===")
        print("1. Display the First 5 Rows")
        print("2. Display the Last 5 Rows")
        print("3. Display Column Names")
        print("4. Display Data Types")
        print("5. Display Basic Information")
        print("6. Dataset Shape")

        try:
            choice = int(input("Enter Your Choice: "))

            if choice == 1  :
                print(self.data.head())

            elif choice == 2 :
                print(self.data.tail())

            elif choice == 3 :
                print(self.data.columns.tolist())

            elif choice == 4 :
                print(self.data.dtypes)

            elif choice == 5 :
                self.data.info()

            elif choice == 6 :
                print("Shape:", self.data.shape)

            else :
                print("Enter A Valid Choice !")

        except :
            print("Something Went Wrong !")

    def performance_data(self):
        if self.data is None:
            print("Please Load the Dataset First!")
            return

        print("=== DataFrame Operations ===")
        print("1. Total Sales")
        print("2. Top 5 Sales")
        print("3. Lowest 5 Sales")
        print("4. Region with Highest Sales")
        print("5. Total Quantity Product")

        try:
            choice = int(input("Enter Your Choice: "))

            if choice == 1 :
                print("Total Sales:", self.data["Sales"].sum())

            elif choice == 2 :
                print("Higest Sales :",self.data['Sales'].nlargest(5))

            elif choice == 3 :
                print("Lowest Sales :",self.data['Sales'].nsmallest(5))

            elif choice == 4:
                sales = self.data.groupby("Region")["Sales"].sum()
                print("Region with Highest Sales:", sales.idxmax())

            elif choice == 5:
                print(self.data.groupby("Product")["Quantity"].sum())

            else:
                print("Enter a Valid Choice!")
        except :
            print("Please Enter a Valid Number!")

    def missing_value(self):
            
        if self.data is None:
            print("Please Load the Dataset First!")
            return

        print("=== Handle Missing Data ===")
        print("1. Display Rows with Missing Values")
        print("2. Fill Missing Values with Mean")
        print("3. Drop Rows with Missing Values")
        print("4. Replace Missing Values with a Specific Value")

        try:
            choice = int(input("Enter Your Choice: "))

            if choice == 1 :
                print(self.data.isnull().sum())

            elif choice == 2 :
                self.data.fillna(self.data.mean(numeric_only=True))
                print(self.data.isnull().sum())
                print("Missing Values Filled Successfully!")

            elif choice == 3 :
                print('=== Before ===')
                self.data.isnull().sum()
                self.data.dropna(inplace=True)
                print("=== After ===")
                print(self.data.isnull().sum())
                print("Rows with Missing Values Removed!")

            elif choice == 4 :
                value = input("Enter a Value to Replace Missing Values: ")
                self.data.fillna(value, inplace=True)
                print("Missing Values Replaced Successfully!")
                print(self.data.isnull().sum())

            else:
                print("Enter A Valide Choice !")

        except :
            print("Please Enter a Valid Number!")
 
    def statistics_data(self):
        if self.data is None:
            print("Please Load the Dataset First!")
            return
        print(self.data.describe().columns)
        column = input("Enter Column Name: ")

        if column not in self.data.columns:
            print("Column Not Found!")
            return
 
        print("1. Minimum")
        print("2. Maximum")
        print("3. Average")
        print("4. Median")
        print("5. Standard Deviation")

        try:
            choice = int(input("Enter Your Choice: "))
 
            if choice == 1:
                print("Minimum:", self.data.min(numeric_only=True))

            elif choice == 2:
                print("Maximum:", self.data.max(numeric_only=True))

            elif choice == 3:
                print("Average:", self.data.mean(numeric_only=True))

            elif choice == 4:
                print("Median:", self.data.median(numeric_only=True))

            elif choice == 5:
                print("Standard Deviation:", self.data.std(numeric_only=True))

            else:
                print("Enter a Valid Choice!")

        except :
            print("Please Enter a Valid Number!")

    def data_visualization(self):
        print("\n========== DATA VISUALIZATION ==========")
        print(" Bar Plot")
        print(" Line Plot")
        print(" Scatter Plot")
        print(" Pie Chart")
        print(" Histogram")
        print(" Area Plot")

        plot_type = input("\nChoose Plot: ").lower().strip()
        print("\nAvailable Columns:")
        print(self.data.columns.tolist())
        

        try:
            if plot_type in ["bar", "line", "scatter", "area"]:
                x = input("Enter X-axis column: ").strip()
                y = input("Enter Y-axis column: ").strip()

                if x not in self.data.columns or y not in self.data.columns:
                    print("Column Not Found!")
                    return
                self.fig, ax = plt.subplots(figsize=(10, 5))

                if plot_type == "bar":
                    sns.barplot(data=self.data, x=x, y=y,errorbar=None)
                elif plot_type == "line":
                    sns.lineplot(data=self.data, x=x, y=y, marker="o")
                elif plot_type == "scatter":
                    sns.scatterplot(data=self.data, x=x, y=y)
                elif plot_type == "area":
 
                    sns.lineplot(data=self.data, x=x, y=y, marker="o")
                    plt.xticks(rotation=45)

                plt.xlabel(x)
                plt.ylabel(y)
                plt.title(plot_type.capitalize() + " Plot")
                plt.grid(alpha=0.3)

            elif plot_type == "pie":
 
                x = input("Enter Category Column: ").strip()
                y = input("Enter Value Column: ").strip()

                if x not in self.data.columns or y not in self.data.columns:
                    print("Column Not Found!")
                    return

                data = self.data.groupby(x)[y].sum()

                plt.figure(figsize=(8, 6))
                plt.pie(data, labels=data.index, autopct="%1.1f%%", startangle=90)
                plt.title(x + " Wise " + y + " Analysis")
                        
            elif plot_type == "histogram":
                column = input("Enter Column Name: ").strip()

                if column not in self.data.columns:
                    print("Column Not Found!")
                    return

                plt.figure(figsize=(10, 5))
                sns.histplot(data=self.data, x=column, bins=10)
                plt.xlabel(column)
                plt.ylabel("Frequency")
                plt.title("Histogram")
                plt.grid(alpha=0.3)

            else:
                print("Invalid Plot Type!")
                return

            plt.tight_layout()
            plt.legend(loc="upper right")
            plt.show() 
        except:
                print("Unable to Create Plot:")

    def save_visualization(self):
        if self.fig is None:
            print("Please Generate a Graph First!")
            return

        file_name = input("Enter File Name: ").strip()

        if not file_name:
            print("File Name Cannot Be Empty!")
            return

        try:
            path = "plot/" + file_name + ".png"
            self.fig.savefig(path, dpi=300, bbox_inches="tight")
            print("Graph Saved Successfully:", path)

        except :
            print("Unable to Save Graph:")
 
    def main_menu(self):
        print()
        print("=" * 15, "Data Analysis & Visualization Program", "=" * 15)
        print("1. Load Dataset")
        print("2. Explore Data")
        print("3. Perform DataFrame Operations")
        print("4. Handle Missing Data")
        print("5. Generate Descriptive Statistics")
        print("6. Data Visualization")
        print("7. Save Visualization")
        print("8. Exit")
        print("=" * 65)

    def start_program(self):
        while True:
            self.main_menu()

            try:
                choice = int(input("Enter Your Choice: "))
                print()

                if choice == 1:
                    self.load_data()

                elif choice == 2:
                    self.explore_data()

                elif choice == 3:
                    self.performance_data()

                elif choice == 4:
                    self.missing_value()

                elif choice == 5:
                    self.statistics_data()

                elif choice == 6:
                    self.data_visualization()

                elif choice == 7:
                    self.save_visualization()

                elif choice == 8:
                    print("Exiting the Program. Goodbye!")
                    
                    break
                else:
                    print("Invalid Choice!")

            except :
                print("Enter a Valid Choice!")
 
if __name__ == "__main__":
    obj = Data_Analyzer()
    obj.start_program()
 
