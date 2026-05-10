def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_days_in_month(year, month):
    
    days=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    if month == 2 and is_leap_year(year):
        return 29
    return days[month]

def solve():
    try:
        y=int(input())
        m=int(input())
        d=int(input())
        h=int(input())
        k=int(input())
    h+=k
    while True:
        if h>=24:
            h-=24
            d+=1
            continue  
        max_days=get_days_in_month(y, m)
        if d>max_days:
            d-=max_days
            m+=1
            continue  
        if m>12:
            m-=12
            y+=1
            continue  
        break
    print(f"{y} {m} {d} {h}")

if __name__ == "__main__":
    solve()
