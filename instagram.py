import csv, instaloader, re

file = open("insta-userlist.txt", "r")
usernames = []
for line in file:
    usernames.append(line.strip())

csv_file = open('insta_details.csv', 'w', newline ='')
with csv_file:
    header = ['username', 'email', 'phone']
    writer = csv.DictWriter(csv_file, fieldnames=header)
    writer.writeheader()
    for username in usernames:
        bot = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(bot.context, f"{username}")
        email = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", profile.biography)
        phone = re.findall(r"^[789]\d{9}$", profile.biography)
        writer.writerow(dict(username=f'{username}', email=" ".join(map(str, email)), phone=''.format(f'{phone}')))

print('---------------------')
print('CSV File download complete. Please check the folder for the csv file')
print('---------------------')