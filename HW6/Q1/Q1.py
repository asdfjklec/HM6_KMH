import csv
import matplotlib.pyplot as plt
import math


def main():
    seoul = open("서울 108 자료.csv", 'r', encoding='cp949')
    Daejeon = open("대전 133 자료.csv", 'r', encoding='cp949')
    busan = open("부산 159 자료.csv", 'r', encoding='cp949')
    Jeju_184 = open("제주 제주 184 .csv", 'r', encoding='cp949')
    Jeju_185 = open("제주 고산 185.csv", 'r', encoding='cp949')
    Jeju_188 = open("제주 성산 188.csv", 'r', encoding='cp949')
    Jeju_189 = open("제주 서귀포 189.csv", 'r', encoding='cp949')

    data_list = [seoul, Daejeon, busan, Jeju_184, Jeju_185, Jeju_188, Jeju_189]
    
    nation = []
    seoul = []
    daejeon = []
    busan = []
    
    for x in range(0,12):
        nation.append(0)
        seoul.append(0)
        daejeon.append(0)
        busan.append(0)

    month = []
    text = ["Seoul", "Daejeon", "Busan", 'Jeju', 'Nation']

    for x in range(1, 13):
        month.append(x)


    for lists in range(0, 3):
        location_data = csv.reader(data_list[lists], delimiter=',')
        header = next(location_data)

        tem = []
        
        flag = 0

        for row in location_data:
            tem.append(float(row[2]))
            nation[flag] += float(row[2]) 
            flag +=1
            
        if (lists == 0):
            for i in range(0,12):
                seoul[i] = tem[i]
        elif (lists == 1):
            daejeon = tem
        elif (lists == 2):
            busan = tem
        
        
            
            
        plt.plot(month, tem, label=text[lists])
        

        
    
    jeju_tem = []
    
    for i in range(0,12): 
        jeju_tem.append(0)
    
    for lists in range(3, 7):
        location_data = csv.reader(data_list[lists], delimiter=',')
        header = next(location_data)
        
        
        flag = 0

        for row in location_data:
            jeju_tem[flag] += (float(row[2]))
            flag +=1
            
        


    for i in range(0,12):
        jeju_tem[i] /= 4
        jeju_tem[i] = round(jeju_tem[i],2)
        nation[i] += jeju_tem[i]
        nation[i] /= 4
        nation[i] = round(nation[i],2)
        
        
        
    print("전국 기온 ")
    print(nation)
    print("서울 기온 ")
    print(seoul)
    print("대전 기온 ")
    print(daejeon)
    print("부산 기온")
    print(busan)
    print("제주 기온")
    print(jeju_tem)
            
    plt.plot(month, jeju_tem, label=text[3])

    plt.title("Average monthly temperature from January to December 2022")
  
    plt.xlabel("month")
    plt.ylabel("average temperature")
    
    plt.plot(month, nation, label=text[4])
    plt.legend()
    
    
    plt.xticks(month)
            

    plt.show()  
    
    print(" 서울108 만을 서울의 정의라 한다.")
    print(" 대전133 만을 서울의 정의라 한다.")
    print(" 부산159 만을 서울의 정의라 한다.")
    print(" 제주는 서귀포 189, 성산 188, 고산 185, 제주 184의 평균을 제주의 정의라 한다.")
    print(" 전국은 이 4가지 데이터의 평균을 기준으로 한다\n\n")
    
    print("전국과 서울의 기온 차")
    stra = ''
    for i in range(0,12):
        stra +=  ( str(i+1) + "월 기온 차:" + str(round(-nation[i]+seoul[i],2)) + "    ")
    
    print(stra)
    print("\n")
    
    print("전국과 대전의 기온 차")
    stra = ''
    for i in range(0,12):
        stra +=  ( str(i+1) + "월 기온 차:" + str(round(-nation[i]+daejeon[i],2)) + "    ")
    
    print(stra)
    print("\n")
    
    print("전국과 부산의 기온 차")
    stra = ''
    for i in range(0,12):
        stra +=  ( str(i+1) + "월 기온 차:" + str(round(-nation[i]+busan[i],2)) + "    ")
    
    print(stra)
    print("\n")
    
    print("전국과 제주의 기온 차")
    stra = ''
    for i in range(0,12):
        stra +=  ( str(i+1) + "월 기온 차:" + str(round(-nation[i]+jeju_tem[i],2)) + "    ")
    
    print(stra)
    print("\n")
    
    
    
    print(" 그래프의 경향을 보면 남단에 있을 수록 평균 기온이 높아지는 경향이 있다. ")
    print("전국 대비 기온이 높은 곳은 제주도와 부산이 있으며 대전, 서울은 전국 기온보다 낮다.")
    
    print("출처 : 기상청 기상자료개방포털, https://data.kma.go.kr/stcs/grnd/grndTaList.do?pgmNo=70")
    

if __name__ == '__main__':
    main()
