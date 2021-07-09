from pathlib import Path

def sizeCalcPrint(header, size, count):
    avg_size = size/count
    avg_size_kb = avg_size/1000
    avg_size_mb = avg_size_kb/1000

    size_kb = size/1000
    size_mb = size_kb/1000
    size_gb = size_mb/1000

    print("*"*7,header,"*"*7)
    print(f"Total in bytes: {size}")
    print(f"Total in kilobytes: {size_kb}") if size > 1000 else ''
    print(f"Total in megabytes: {size_mb}") if size_kb > 1000 else ''
    print(f"Total in gigabytes: {size_gb}") if size_mb > 1000 else ''
    print(f"Number of Files: {count}")

    print(f'{"-"*20}\n')

def main():
    file_types = {}
    extension = ""
    calc_path = ""

    calc_path = input("What folder would you like to search?")

    path = Path(calc_path)
    for p in path.rglob("*"):
        extension = p.absolute().suffix.replace('.','')
        if(len(extension) != 0):
            if extension in file_types:
                file_types[extension]['count'] += 1
                file_types[extension]['size'] += p.stat().st_size
            else:
                file_types[extension] = {}
                file_types[extension]['count'] = 1
                file_types[extension]['size'] = p.stat().st_size

    for k in file_types.keys():   
        sizeCalcPrint(k, file_types[k]['size'], file_types[k]['count'])

    input()

if __name__ == "__main__":
    main()