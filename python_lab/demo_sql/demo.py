import sqlite3

# Kết nối đến database
conn = sqlite3.connect('trackmusic.sqlite')
cur = conn.cursor()

# Câu lệnh SQL
# query = "INSERT OR IGNORE INTO Artist (name) VALUES (?)"

# Đọc file CSV
with open('tracks.csv', 'r') as file:
    for line in file:
        # Xử lý dòng đọc từ file
        line = line.strip().split(',')
        
        # Kiểm tra dữ liệu đủ cột
        if len(line) < 6:
            print(f"Dòng không hợp lệ: {line}")
            continue

        name = line[0]
        artist = line[1]
        album = line[2]
        count = line[3]
        rating = line[4]
        length = line[5]

        print(name, artist, album, count, rating, length)

        cur.execute('''INSERT OR IGNORE INTO Artist (name) 
            VALUES ( ? )''', ( artist, ) )
        cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
        artist_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
            VALUES ( ?, ? )''', ( album, artist_id ) )
        cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
        album_id = cur.fetchone()[0]

        cur.execute('''INSERT OR REPLACE INTO Track
            (title, album_id, len, rating, count) 
            VALUES ( ?, ?, ?, ?, ? )''', 
            ( name, album_id, length, rating, count ) )

# Commit thay đổi và đóng kết nối
conn.commit()
cur.close()
conn.close()
