import sqlite3
conn = sqlite3.connect('youtube_videos_db')


cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS VIDEOS(
                ID INTEGER PRIMARY KEY,
                NAME TEXT NOT NULL,
                TIME TEXT NOT NULL
            
    )
''')


def list_videos():
    cursor.execute("SELECT * FROM VIDEOS")
    for row in cursor.fetchall():
        print(row)


def add_video(name, time):
    cursor.execute("insert into videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()
    

def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE ID = ?", (new_name, new_time, video_id ))
    conn.commit()

def delete_video(video_id,):
    cursor.execute("delete from videos where id = ?", (video_id))
    conn.commit()





def main():
    while True:
        print("\n youtube manager app with database ")
        print("1. List all youtube videos")
        print("2. Add a youtube videos")
        print("3. Update a youtube videos")
        print("4. Delete youtube videos")
        print("5. EXit")
        choice = input("enter your choicce: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter video Id to update: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_video(video_id, name, time,)

        elif choice == '4':
            video_id = input("Enter video Id to delete: ")
            delete_video(video_id)
        else:
            print("invalid choice")

    conn.close()

    






if __name__ == "__main__":
    main()
