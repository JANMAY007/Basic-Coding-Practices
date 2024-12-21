import zipfile
import optparse
from threading import Thread


def extract_zip(zip_file, password):
    try:
        zip_file.extractall(pwd=bytes(password, "utf-8"))
        print("[+] Match Found : " + password)
    except Exception:
        print("[-] Match Not Found : " + password)
        pass


if __name__ == "__main__":
    parser = optparse.OptionParser("usage %prog -f <zipfile> -d <dictionary>")
    parser.add_option("-f", dest="zipname", type="string", help="Specify the zip file")
    parser.add_option("-d", dest="dname", type="string", help="Specify the dictionary file")
    (options, args) = parser.parse_args()
    if options.dname is None or options.zipname is None:
        print(parser.usage)
        exit(0)
    else:
        zip_name = options.zipname
        dname = options.dname
        zFile = zipfile.ZipFile(zip_name)
        passFile = open(dname, "r")
        print("[+] Cracking zip using dictionary attack")
        for line in passFile.readlines():
            passwd = line.strip("\n")
            t = Thread(target=extract_zip, args=(zFile, passwd), )
            t.start()
