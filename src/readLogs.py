def read_logs(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            yield line.rstrip("\n")

for log in read_logs("testing.txt"):
    print(log)
