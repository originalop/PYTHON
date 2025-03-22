count=1
with open("Table.txt", "w") as fp:
    fp.writelines([f" {count} |",f" {count+1} |",f" {count+2} |",f" {count+3} |",f" {count+4} |",f" {count+5} |",f" {count+6} |",f" {count+7} |",f" {count+8} |",f" {count+9} |"])
    # print(fp.readlines())
    # fp.close()

with open("table.txt","r") as fp:
    
    print(fp.read())
    print("Hello")
    fp.close()