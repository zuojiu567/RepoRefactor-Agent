from src.scanner import scan
import sys
if __name__=='__main__':
    target=sys.argv[2] if len(sys.argv)>2 else './examples'
    print(scan(target))
