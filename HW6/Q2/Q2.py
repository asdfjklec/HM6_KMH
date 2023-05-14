import csv
import random
import matplotlib.pyplot as plt

def plot_histogram(data, title):
    counts = [data.count(i) for i in range(1, 7)]
    plt.bar(range(1, 7), counts, color='skyblue')
    plt.xlabel('Number')
    plt.ylabel('Count')
    plt.title(title)
    plt.show()
    
def main():

    with open('random_numbers.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Random Numbers"])  
        writer.writerow([])  

        num_runs = [1, 10, 100, 1000]  

        for num in num_runs:
            data = []
            for _ in range(num):
                row = [random.randint(1, 6) for _ in range(100)]  
                data.extend(row)
                writer.writerow(row)

            writer.writerow([])  
            plot_histogram(data, f'Histogram ({num}x100)')

    print("CSV 파일에 데이터가 저장완료\n")

    print("csv의 파일 저장 방식은 100개의 열을 입력하면 다음 행으로 넘어가게 설계했다.")
    print("횟수는 공백 행으로 구별했다.\n")

    print("히스토그램을 보면 횟수가 증가하면서 확률이 거의 동일해지는 것을 볼 수 있다. ")
    print("다시 말해 표본집단의 크기가 커지면 그 표본평균이 모평균에 가까워지고 있음을 볼 수 있다.")
    print("따라서 취합하는 표본의 수가 많을수록 통계적 정확도는 올라가게 된다.")
    print("이를 통하여 큰 수의 법칙(law of large numbers)을 따르는 것을 알 수 있다.")
    

    
if __name__ == '__main__':
    main()
    
    
