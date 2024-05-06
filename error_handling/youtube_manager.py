import json
# we use json.load and json.dump to write what and where

def load_data():
    try:
        with open('youtube.txt', 'r')as file:
            return json.load(file)
            # print(type(test))
            # return test
    except FileNotFoundError:
        return []
        
    
def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)
 





def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index, video  in enumerate(videos, start=1):
        
        # print(f"{index}. {video['name']}, Duration: {video['time']}")
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    print("\n")
    print("*" * 70)    


def add_videos(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)


def update_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update"))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name  ")
        time = input("Enter the new video  time ")
        videos[index-1] = {'name': name, 'time': time}
        save_data_helper(videos)
    else:
        print("Invalid index selected")

    

def delete_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to delete"))

    if 1<= index <= len(videos):
        del videos[index-1]
    else:
        print("Invalid videos index selected")






def main():
    videos = load_data()


    while True:
        print("\n Youtube Manager| Choose an option ")
        print("1. List all youtube videos")
        print("2. Add a youtube videos")
        print("3. Update a youtube videos")
        print("4. Delete youtube videos")
        print("5. EXit")
        choice = input("Enter your choice: ")
        # print(videos)


        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_videos(videos)
            case '3':
                update_videos(videos)
            case '4':
                delete_videos(videos)
            case '5':
                break
            case _:
                print("Invalid Choice")

if __name__ == "__main__":
    main()


