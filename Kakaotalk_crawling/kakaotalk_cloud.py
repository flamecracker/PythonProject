import os, sys
from wordcloud import WordCloud

def kakaotalk_printer(txt_file,result_txt):
    with open(txt_file,"r",encoding="utf-8") as fr, open(result_txt,"w",encoding="utf-8") as fw:
        lines = fr.readlines()
        error_words=["이모티콘","ㅋㅋ","사진"]
        for line in lines[5:]: # 위의 5줄은 필요없으니 날린다.
            if '] [' in line:
                index = -1
                start = 0
                while True:
                    index = line.find('] ',index+1)
                    if index == -1:
                        break
                    start = index
                
                line = line[start+2:]
                for error_word in error_words:
                    line = line.replace(error_word,"")                 
                fw.write(line)

    fr.close()
    fw.close()

def found_kakao_txt():
    os.chdir(os.getcwd()+"\\Kakaotalk_crawling")
    txt_path = os.getcwd()+"\\txt"
    # print(txt_path)
    txt_list = os.listdir(txt_path)
    return txt_list

def kakao_to_cloud(text_name, i, wordcloud):
    text = ''
    with open(text_name, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            text += line
    wordcloud.generate(text)
    wordcloud.to_file(result_png)

# 몸체
txt_list = found_kakao_txt()
wc = WordCloud(font_path='‪C:\Windows\Fonts\H2GTRE.TTF',background_color="white",width=1000,height=1000,max_words=100,max_font_size=300)
for i, txt_file in enumerate(txt_list, 1):
    result_txt = "result/result_"+str(i)+".txt"
    result_png = "result/result_"+str(i)+".png"
    kakaotalk_printer("txt/"+txt_file,result_txt)
    kakao_to_cloud(result_txt, result_png, wc)





