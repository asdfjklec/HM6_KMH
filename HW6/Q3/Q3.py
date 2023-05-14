import csv
import matplotlib.pyplot as plt

def main():
    csv1 = open("제주도 남녀 성비 2002 - 2022.csv",'r' ,encoding='cp949')
    
    data = csv.reader(csv1, delimiter=',')

    header = next(data)
    header = next(data)
    header = next(data)
    
    gender_ratio = []
    years = []
    
    for i in range(0,21):
        years.append(i+2002)
        gender_ratio.append(float(header[i*3]))
    
    plt.plot(years, gender_ratio, marker='o', color='skyblue')
    plt.xlabel('Year')
    plt.ylabel('Gender Ratio (%)')
    plt.title('Gender Ratio in Jeju Island (2002-2022)')
    plt.xticks(years, rotation=45)
    plt.grid(True)
    plt.show()
    
    for a in range(0, 21):
        print( str(years[a]) + "년 남녀 성비 : " + str(gender_ratio[a]) + "%")
        
        
    print("\n 위 그래프를 보면 여자가 더 많은 해가 있으므로 속설은 옳지 않다. \n\n")
        
    print("남녀 성비는 남자/여자*100 으로 계산한다.")
    print("자료 출처 : 행정안전부(주민과), 2023.04, 2023.05.14, 남녀성비(시도/시/군/구)")
    print("https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1YL20701&conn_path=I2")
    
if __name__ == '__main__':
    main()
