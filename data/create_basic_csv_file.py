import csv

with open("fb_posts.csv", "w", encoding="UTF8") as file:
    writer = csv.writer(file, delimiter = ';')
    writer.writerow(['Date','Post'])
    
    for i in range(50):
        writer.writerow([str(i), ""])