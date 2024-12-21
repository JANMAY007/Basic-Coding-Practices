from matplotlib import pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import numpy as np
import PyPDF2

if __name__ == '__main__':
    data = ''
    file = open('Tesla.pdf', 'rb')
    pdf_file = PyPDF2.PdfFileReader(file)
    for pageNum in range(pdf_file.numPages):
        pageObj = pdf_file.getPage(pageNum)
        data += pageObj.extractText()
    file.close()
    print(data)
    mask = np.array(Image.open(r'img.png'))
    wc = WordCloud(stopwords=STOPWORDS,
                   mask=mask,
                   background_color="white",
                   max_words=2000,
                   max_font_size=500,
                   random_state=42,
                   width=500,
                   height=500)
    wc.generate(data)
    plt.imshow(wc, interpolation="None")
    plt.axis('off')
    plt.savefig('cloud.png')
    plt.show()
