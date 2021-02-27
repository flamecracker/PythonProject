import os
from wordcloud import WordCloud

def kakaotalk_printer(txt_file,result_txt):
    with open(txt_file,"r",encoding="utf-8") as fr, open(result_txt,"w",encoding="utf-8") as fw:
        lines = fr.readlines()
        for line in lines[5:]: # 위의 5줄은 필요없으니 날린다.
            if '] [' in line:
                index = -1
                start = 0
                while True:
                    index = line.find('] ',index+1)
                    if index == -1:
                        break
                    start = index                    
                fw.write(line[start+2:])

    fr.close()
    fw.close()

def found_kakao_txt():
    txt_path = os.getcwd()+"/txt"
    txt_list = os.listdir(txt_path)
    return txt_list
# 몸체
txt_list = found_kakao_txt()
wc=WordCloud(font_path='‪C:\Windows\Fonts\H2GTRE.TTF',background_color="white",width=1000,height=1000,max_words=100,max_font_size=300)
for i, txt_file in enumerate(txt_list, 1):
    result_txt = "result/result_"+str(i)+".txt"
    kakaotalk_printer("txt/"+txt_file,result_txt)
    wc.generate(result_txt)
    wc.to_file("result/result_"+str(i)+".png")




