import optparse
import zipfile
from threading import Thread


def extract_zip(zip_file, password):
    """[summary]
    
    Arguments:
        zFile string -- zipped file
        password {[type]} -- [description]
    """
    try:
        zip_file.extractall(pwd=bytes(password, "utf-8"))
        print(password)
        print("[+] Password found : ", password)
    except NotImplementedError:
        pass


if __name__ == "__main__":
    print("[+] Cracking ZIP")
    parser = optparse.OptionParser("usage %prog -f <zip-file> -d <dictionary>")
    parser.add_option("-f", dest="zname", type="string", help="specify zip file")
    parser.add_option("-d", dest="dname", type="string", help="specify dictionary file")
    (options, args) = parser.parse_args()
    if options.zip_name is None or options.d_name is None:
        print(parser.usage)
        exit(0)
    else:
        zip_name = options.zip_name
        d_name = options.d_name
        zFile = zipfile.ZipFile(zip_name)
        passFile = open(d_name, "r")
        for line in passFile.readlines(1000):
            passwd = line.strip("\n")
            t = Thread(target=extract_zip, args=(zFile, passwd))
            t.start()
