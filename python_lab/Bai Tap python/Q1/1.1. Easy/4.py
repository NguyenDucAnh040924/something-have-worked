# Create a dictionary to store information about your favorite book (title, author, year)

title = input('Nhap title: ')
author = input('Nhap author: ')
year = input('Nhap year: ')


if not (title.strip() or author.strip() or year.strip()):
    title = "Transformer"
    author = "Alex"
    year = "2018"
else:
    title = str(title)
    author = str(author)
    year = str(year)



d={"Tilte": f"{title}",
       "Author": f"{author}",
       "Year":f"{year}"}

print(d.get("Author"))