__author__ = 'Vishal PC'
__author__ = 'Vishal PC'
def sum_list(filename):
    #filename='C:\Programming\Python\HSN\dec-pkt-1.txt'
    dict={}
    list=[]
    with open(filename) as fp:
        for line in fp:
           s=line.split()
           list.append(s)
    list0=(sub_list[0] for sub_list in list)
    list1=(sub_list[1] for sub_list in list)
    list2=(sub_list[2] for sub_list in list)
    list3=(sub_list[3] for sub_list in list)
    list4=(sub_list[4] for sub_list in list)
    list0=map(float, list0)
    list1=map(int, list1)
    mlist1=(x%4 for x in list1)
    list2=map(int, list2)
    mlist2=(x%4 for x in list2)
    list3=map(int, list3)
    mlist3=(x%4 for x in list3)
    list4=map(int, list4)
    mlist4=(x%4 for x in list4)
    slist=[]
    for w,x,y,z in zip(mlist1,mlist2,mlist3,mlist4):
        sum=0
        sum=sum+w+x+y+z
        sum=sum%4
        slist.append(sum)
    slist=map(int,slist)
    return slist

def hash(filename):
    list=[]
    with open(filename) as fp:
        for line in fp:
           s=line.split()
           list.append(s)
    s=0
    e=299
    while (e<=3600.360144):
        print s, "--", e
        list1=(sub_list[5] for sub_list in list if (float(sub_list[0])>s and float(sub_list[0])<e))
        list1=map(int, list1)
        sum_p1=0.0
        avg_p1=0.0
        sum_p2=0.0
        avg_p2=0.0
        sum_p3=0.0
        avg_p3=0.0
        sum_p4=0.0
        avg_p4=0.0
        for x, y in zip(list1,sum_list(filename)):
            if y==0:
                sum_p1=sum_p1+x+40
            elif y==1:
                sum_p2=sum_p2+x+40
            elif y==2:
                sum_p3=sum_p3+x+40
            else:
                sum_p4=sum_p4+x+40
        avg_p1=float(sum_p1*8/(300*1024))
        avg_p2=float(sum_p2*8/(300*1024))
        avg_p3=float(sum_p3*8/(300*1024))
        avg_p4=float(sum_p4*8/(300*1024))
        print avg_p1,avg_p2,avg_p3,avg_p4
        mx=max(avg_p1,avg_p2,avg_p3,avg_p4)
        mn=min(avg_p1,avg_p2,avg_p3,avg_p4)
        dmax=0.0
        dmax=float(mx)-float(mn)
        print "Max Difference=", float(dmax)
        s=e+1
        e += 300
print hash('C:\Programming\Python\HSN\dec-pkt-1.txt')

