import sys
import clipboard
import json

SAVED_DATA = "/home/clipboard/clipit.json"

def save_data(filepath, data):
    with open(filepath,"w") as f:
        json.dump(data,f)

def load_data(filepath):
    try:

        with open(filepath,"r") as f:
            data = json.load(f)
            return data
    except:
        return{}





if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == "s":
        key = input("Enter a key: ")
        data[key]=clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Data saved ***")  

    elif command == "lo":
        key = input("Ente a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to cipboard.")
        else:
            print("key doesn't exist.")

    elif command =="ls":
        print("list")
        print(data.keys())
   elif command =="-h":
        print("\n \n #Save clipboard data to clipit: clipit s \n \n #load data from clipit to clipboard : clipit lo \n \n #list tagnames saved in clipit : clipit ls \n \n")
    else:
        print("Unknown command . Use clipit.sh -h for help")

else:
    print("Please pass exactly one text >> Use clipit.sh -h for help")



