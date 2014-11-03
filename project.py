
from operator import itemgetter
import heapq

#---------------------------------------Determine average bit rate-------------------------------------

def bit_rate(filename):
    list=[]
    with open(filename) as fp:
        for line in fp:
           s=line.split()
           list.append(s)
        sum=0
        list1=[sub_list[5] for sub_list in list]
        list1=map(int, list1)
        for s in list1:
            sum=sum+s
        add=0.0
        add=len(list1)*20
        total=0.0
        total=((sum+add)*8)/3600.360144
        print "Avg bit rate in bps:", total

def avg_bit_rate_five(filename):
    print "Average Bit rate in bps:"
    list=[]
    with open(filename) as fp:
        for line in fp:
           s=line.split()
           list.append(s)
        x=0
        y=299
        while (y<=3600.360144):
            sum=0
            avg=0.0
            list1=[sub_list[5] for sub_list in list if (float(sub_list[0])>x and float(sub_list[0])<y)]
            for l in list1:
               sum=sum+int(l)+20
            sum=sum*8
            avg=sum/300.0
            print x,"-",y,":", avg
            x=y+1
            y=y+300

#-----------------------------------------Determine payload size distribution --------------------------

def payload_size_distribution(filename):
    list=[]
    with open(filename) as fp:
        for line in fp:
           s=line.split()
           list.append(s)
        c0=0
        c127=0
        c255=0
        c383=0
        c511=0
        c512=0
        list1=[sub_list[5] for sub_list in list]
        for l in list1:
            if l=='0':
                c0=c0+1
            elif (l>'0' and l<='127'):
                c127=c127+1
            elif (l>'127' and l<='255'):
                c255=c255+1
            elif (l>'255' and l<='383'):
                c383=c383+1
            elif (l>'383' and l<='511'):
                c511=c511+1
            else:
                c512=c512+1
        print "Percentage based on number of packets:"
        print "0:", (float(c0)/len(list1))*100
        print "1-127:", (float(c127)/len(list1))*100
        print "128-255:", (float(c255)/len(list1))*100
        print "256-383:", (float(c383)/len(list1))*100
        print "383-511:", (float(c511)/len(list1))*100
        print "512:", (float(c512)/len(list1))*100

#------------------------------------Determine highest traffic volume received by source port------------------------

def sort_source(filename):
    source_count = {}
    list=[]
    list2=[]
    with open(filename) as fp:
        for line in fp:
           s=line.split()
           list.append(s)
    list1=[sub_list[1] for sub_list in list]
    list2=[sub_list[5] for sub_list in list]
    list1=map(int, list1)
    list2=map(int, list2)
    sum=0.0
    for data in list2:
        sum=sum+data+20
    for x,y in zip(list1,list2):
        if not x in source_count:
            source_count[x]=y + 20
        else:
            source_count[x]=source_count[x] + y + 20
    sorted_top=heapq.nlargest(3,source_count.items(),key=itemgetter(1))
    for i in sorted_top:
        print "Traffic Volume for %d is %d" %(i[0],i[1])
    print "Traffic Percentage:"
    print "Source IP",sorted_top[0][0],":",(float(sorted_top[0][1])/sum)*100
    print "Source IP",sorted_top[1][0],":",(float(sorted_top[1][1])/sum)*100
    print "Source IP",sorted_top[2][0],":",(float(sorted_top[2][1])/sum)*100

#------------------------------------------ Determine highest traffic volume sent by destination port----------------------
def sort_destnation_port(filename):
    destination_count = {}
    list=[]
    list2=[]
    with open(filename) as fp:
        for line in fp:
           s=line.split()
           list.append(s)
    list1=[sub_list[4] for sub_list in list]
    list2=[sub_list[5] for sub_list in list]
    list1=map(int, list1)
    list2=map(int, list2)
    sum=0.0
    for data in list2:
        sum=sum+data+20
    for x,y in zip(list1,list2):
        if not x in destination_count:
            destination_count[x]=y + 20
        else:
            destination_count[x]=destination_count[x] + y + 20
    sorted_top=heapq.nlargest(3,destination_count.items(),key=itemgetter(1))
    for i in sorted_top:
        print "Traffic Volume for port %d is %d" %(i[0],i[1])
    print "Traffic Percentage:"
    print "Destination Port",sorted_top[0][0],":",(float(sorted_top[0][1])/sum)*100
    print "Destination Port",sorted_top[1][0],":",(float(sorted_top[1][1])/sum)*100
    print "Destination Port",sorted_top[2][0],":",(float(sorted_top[2][1])/sum)*100

#------------------------------Round Robin analysis-----------------------------------

def round_robin(filename):
    print "Average Bit Rate in bps:"
    list=[]
    with open(filename) as fp:
        for line in fp:
           s=line.split()
           list.append(s)
    dmax={}
    dmin={}
    dmax_min={}
    p=0
    while (p<4):
        print "For Port P",p+1
        x=0
        y=299
        while (y<=3600.360144):
            sum=0
            avg=0.0
            p1=[sub_list[5] for sub_list in list[p::4] if (float(sub_list[0])>x and float(sub_list[0])<y)]
            for l in p1:
                sum=sum+int(l)+20
            sum=sum*8
            avg=sum/300.0
            print x,"-",y,":", avg
            if y not in dmax:
                dmax[y]=avg
            else:
                if avg> dmax[y]:
                    dmax[y]=avg
            if y not in dmin:
                dmin[y]=avg
            else:
                if avg< dmin[y]:
                    dmin[y]=avg
            x=y+1
            y=y+300
        p=p+1
    print "Max Difference:"
    dmax_min={k:float(dmax[k])-float(dmin[k]) for k in dmax if k in dmin}
    lst=sorted(dmax_min.iteritems(), key=itemgetter(0))
    for t in lst:
        print '%d : %f' % (t[0],t[1])


def main():
    filename=raw_input("Enter file Location:")
    print bit_rate(filename)
    print avg_bit_rate_five(filename)
    print payload_size_distribution(filename)
    print sort_source(filename)
    print sort_destnation_port(filename)
    print round_robin(filename)

print main()
