pdf_file = '../temp/YusufBerkayGirgin_Resume.pdf'

with open(pdf_file, 'rb') as f:
    ret = f.read().decode("utf-8")
    print(ret)
