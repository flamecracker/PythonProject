import os
from wordcloud import WordCloud

def found_kakao_txt():
    txt_path = os.getcwd()+"\\Kakaotalk_crawling\\txt"
    txt_list = os.listdir(txt_path)
    return txt_list

def kakao_conv_rate(txt_file):
    with open(txt_file,"r",encoding="utf-8") as fr:
        lines = fr.readlines()
        error_words=["이모티콘","ㅋㅋ","사진"]
        text = ""
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
                text += line
    return text

def kakao_conv_share(txt_file):
    with open(txt_file,"r",encoding="utf-8") as fr:
        lines = fr.readlines() 
        text = ""
        for i, line in enumerate(lines[5:],1):
            if '] [' in line:
                text += line.split('[')[1].replace(']',' ') +str(i)+ ' '
                print(line.split('[')[1].replace(']',' ') +str(i)+ ' ')   
    return text
     
# 몸체
if __name__ == '__main__':
    print("안녕하세요, 분석시뮬레이터 입니다.")
    x = ""
    while True:
        print("\n분석하고자 하는 분야를 선택해주세요\n만약 분석을 원하지 않는다면 exit를 입력해주세요")
        print("1: 대화내용 분석\n2: 대화 비율 분석\n3: 카톡방 활성화 분석\n")
        print("입력: ",end='')
        x = input()
        if(x=="exit"):
            print("시뮬레이터를 종료합니다.")
            break
        elif(x=='1'):
            txt_list = found_kakao_txt()
            wc = WordCloud(font_path='‪C:\Windows\Fonts\H2GTRE.TTF',background_color="white",width=1000,height=1000,max_words=100,max_font_size=300)
            for i, txt_file in enumerate(txt_list, 1):
                text = ''
                result_png = "Kakaotalk_crawling/result/conv_"+str(i)+".png"
                text = kakao_conv_rate("Kakaotalk_crawling/txt/"+txt_file)
                wc.generate(text)
                wc.to_file(result_png)
        elif(x=='2'):
            txt_list = found_kakao_txt()
            wc = WordCloud(font_path='‪C:\Windows\Fonts\H2GTRE.TTF',background_color="white",width=400,height=400,max_words=20,max_font_size=150)
            for i, txt_file in enumerate(txt_list, 1):
                text = ''
                result_png = "Kakaotalk_crawling/result/share_"+str(i)+".png"
                text = kakao_conv_share("Kakaotalk_crawling/txt/"+txt_file)
                wc.generate(text)
                wc.to_file(result_png)
        else:
            print("무야호~")
    
    





