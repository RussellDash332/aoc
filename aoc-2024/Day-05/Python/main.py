r=range;m=z=s=0;p={};u=p.get;d={0};[len(l)==1and[m:=1]or m and[k:=len(a:=[*map(int,l.split(','))])//2,e:=a[k],c:=1,[a[i]in u(a[j],d)or[c:=0,t:=a[i],f:=a.__setitem__,f(i,a[j]),f(j,t)]for i in r(len(a))for j in r(i)],z:=z+e*c,s:=s+(1-c)*a[k]]or[a:=[*map(int,l.split('|'))],p.__setitem__(a[0],u(a[0],d)|{a[1]})]for l in open(0)];print('Part 1:',z,'\nPart 2:',s)