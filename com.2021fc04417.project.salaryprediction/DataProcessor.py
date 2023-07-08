
import CleanData as cd


def dataProcessor(data):
        # printing top 5 records
        print("top 5 records :")
        print(data.head(5))
        print("\n\n")

        # printing info about data
        print("info about columns :")
        print(data.info())
        print("\n\n")

        print("print null values count before cleaning ---:")
        cd.printNullCount(data)
        print("\n\n")

        print("After clearning null values ---:")
        data = cd.removeNull(data)
        cd.printNullCount(data)