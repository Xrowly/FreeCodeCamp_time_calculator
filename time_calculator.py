def add_time(start, duration, startday=None):
    #3:00_PM->3/:/00/PM
    st , tms =start.split(' ')
    #Hours,Mins
    sh, sm=map(int,st.split(':'))
    dh, dm =map(int,duration.split(':'))
    if tms=='PM' and sh!=12:
        dh+=12
    elif tms=='AM' and sh==12:
        dh=0

    nhp=(sh+dh+(sm+dm)//60)
    npm=(sm+dm)%60     #new +mins
    n= nhp//24
    nhp%=24
    #24->12
    tms='AM' if nhp<12  else 'PM'
    nhp= 12 if nhp == 0 or nhp == 12 else nhp % 12
      
    #min convert
    if len(str(npm))==1:
        mins='0'+str(npm)
        print(mins)
    else:
        mins=str(npm)
    time=str(nhp)+':'+mins+' '+tms
    if startday:
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day_index = days_of_week.index(startday.capitalize())
        new_day = days_of_week[(day_index + n) % 7]
        time += f', {new_day}'
    if n==1:
        time+=' (next day)'
    elif n>1:
        time+=f' ({n} days later)'
    
    print(time)
    return time
add_time('11:59 PM', '24:05', 'Wednesday')