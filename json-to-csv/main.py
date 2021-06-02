
import json

def json_to_csv():
    try:
        with open("data.json","r") as json_dosya:
            data = json.loads(json_dosya.read())
        output = ','.join([*data[0]])
        for s in data:
            output += f'\n{s["id"]},{s["isim"]},{s["dogumyili"]}'
        with open("cikti.csv","w") as cikti_csv:
            cikti_csv.write(output)
    except:
        print("Error..")

if __name__ == '__main__':
    json_to_csv()

