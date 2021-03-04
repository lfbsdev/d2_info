from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())
process.crawl('d2_info')
process.start()

stdin = input("\nType heroes, items, creeps (ex: pudge bane abyssal boar): ").split()
stdin = [arg.capitalize() for arg in stdin]

print("\tReduced Duration:\n")
with open("reduced.txt", "r") as f:
    for line in f.readlines():
        for arg in stdin:
            if (arg in line.split(",")[0]):
                print("\t", line, end = '')
print("\n")

print("\tReduced Slow:\n")
with open("slow.txt", "r") as f:
    for line in f.readlines():
        for arg in stdin:
            if (arg in line.split(",")[0]):
                print("\t", line, end = '')
print("\n")

print("\tDynamic Tick Intervals:\n")
with open("dynamic.txt", "r") as f:
    for line in f.readlines():
        for arg in stdin:
            if (arg in line.split(",")[0]):
                print("\t", line, end = '')
print("\n")

print("\tOther interactions:\n")
with open("other.txt", "r") as f:
    while f:
        line = f.readline()
        if (line == ''):
            break
        for arg in stdin:
            if (arg in line):
                line2 = f.readline()
                print("\t", line, "\t\t", line2)
        
