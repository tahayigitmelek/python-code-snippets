
import requests
import csv

durum_dict = {}

def main():
    with open("siteler.txt", "r") as siteler:
        for satir in siteler:
            site = satir.strip()
            status = requests.get(site).status_code
            if (status == 200):
                durum_dict[site] = "site calisiyor"
            else:
                durum_dict[site] = "site calismiyor"

    with open("site_durumlari.csv", "w", newline="") as yazilacak_dosya:
        csv_yazici = csv.writer(yazilacak_dosya)
        for key in durum_dict.keys():
            csv_yazici.writerow([key, durum_dict[key]])

if __name__ == "__main__":
    main()

