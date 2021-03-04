from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())

# 'followall' is the name of one of the spiders of the project.
process.crawl('d2_info')
process.start() # the script will block here until the crawling is finished

enemies = input("Type your enemies: ").split()
enemies = [enemy.capitalize() for enemy in enemies]
allies = input("Type your allies: ").split()
allies = [ally.capitalize() for ally in allies]

print("Enemies:\n")

print("\tReduced Duration:\n")
with open("reduced.txt", "r") as f:
    for line in f.readlines():
        for enemy in enemies:
            if (enemy in line):
                print("\t", line, end = '')
print("\n")

print("\tReduced Slow:\n")
with open("slow.txt", "r") as f:
    for line in f.readlines():
        for enemy in enemies:
            if (enemy in line):
                print("\t", line, end = '')
print("\n")

print("\tDynamic Tick Intervals:\n")
with open("dynamic.txt", "r") as f:
    for line in f.readlines():
        for enemy in enemies:
            if (enemy in line):
                print("\t", line, end = '')
print("\n")
