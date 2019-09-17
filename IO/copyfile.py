import sys

def copy_file(src, dst):
    with open(src) as src_file, open(dst, 'w') as dst_file:
        for n, line in enumerate(src_file.readlines()):
            dst_file.write('{} {}'.format(n+1, line))
    with open(dst) as file:
        print(file.read())



if __name__ == '__main__':
    if len(sys.argv) == 3:
        copy_file(sys.argv[1], sys.argv[2])
        
    else:
        print("Paramter Error")
        print(sys.argv[0], 'srcfile dstfile')
        exit()
