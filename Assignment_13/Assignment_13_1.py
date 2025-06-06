class BookStore : 
    NoOFBooks = 0

    def __init__(self):
        print("Enter the Name : ")
        self.Name = input()

        print("Enter Author Name : ")
        self.Author = input()

        BookStore.NoOFBooks += 1
    
    def Display(self):
        print("Name of the Book: ", self.Name)
        print("Name of the Author : ", self.Author)
        print(f"Number of books : {BookStore.NoOfBooks}")




def main():
    Obj1 = BookStore()
    Obj1.Display()

    Obj2 = BookStore()
    Obj2.Display()

if __name__ == "__main__":
    main()