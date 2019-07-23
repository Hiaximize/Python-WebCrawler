import requests


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

while True:
    firstAnswer = input("Press 1 to crawl for sub-domains or 2 to crawl for subdirectories> ")

    if firstAnswer == "1":
        while True:
            temp = input("What URL do you want to crawl?> ")
            url = temp.lower()
            if url == "quit":
                print("Exiting...")
                exit(1)
            else:
                with open("/root/PycharmProjects/crawler_testing/subdomains-wordlist.txt", "r") as wordlist:
                    for line in wordlist:
                        word = line.strip()
                        test_url = word + "." + url
                        response = request(test_url)
                        if response:
                            temp = response.text
                            print("[+] Subdomain detected --> " + test_url)
                            firstSplit = temp.split("FailureMode=")
                            print(firstSplit[0])



    elif firstAnswer == "2":
        while True:
            temp = input("URL?> ")
            url = temp.lower()
            if url == "quit":
                print("Exiting...")
                exit(1)
            else:
                with open("/root/PycharmProjects/crawler_testing/files-and-dirs-wordlist.txt", "r") as secondWordlist:
                    for line in secondWordlist:
                        word = line.strip()
                        test_url = url + "/" + word
                        response = request(test_url)
                        if response:
                            print("[+] File/Dir detected --> " + test_url)


    else:
        print("That is not a valid choice, please enter either '1 or 2'\n"
              "1: crawl a website\n"
              "2: crawl subdirectories")



temp = result.text
print(temp)


