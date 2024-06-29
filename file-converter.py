import markdown as md
import sys

def validate_args(args):
    if len(args) != 4 or args[1] != 'markdown':
        return False
    return True
    
def markdown(inputfile, outputfile):
    with open(inputfile) as f:
        contents = f.read()
    with open(outputfile, 'w') as f:
        html = md.markdown(contents, extensions=['markdown.extensions.tables'])
        f.write(html)

def main():
    args = sys.argv

    if not validate_args(args):
        print('Error: Please enter the correct input!\nFor more information, see the README.md')
        return
    
    markdown(args[2], args[3])

if __name__ == "__main__":
    main()