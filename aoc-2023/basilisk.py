# Day 01: 347
[r:=range,m:=dict(zip(['one','two','three','four','five','six','seven','eight','nine',*map(str,z:=r(1,10))],[*z]*2)),t:=sum([s:=[*filter(lambda x:'0'<x<':',l)],f:=[m[j]for i in r(len(l))for j in m if l[i:i+len(j)]==j],complex(int(s[0]+s[-1]),10*f[0]+f[-1])][2]for l in __import__('sys').stdin),print('Part 1:',int(t.real),'\nPart 2:',int(t.imag))]
# Day 02: 274
[z:=int,u:=sum([g:=l.split(':'),t:=g[1].split(),h:=dict(sorted((t[2*i+1][0],z(t[2*i]))for i in range(len(t)//2))),complex(z(g[0][4:])*(h['g']<14>=h['b'])*(h['r']<13),h['b']*h['g']*h['r'])][3]for l in __import__('sys').stdin),print('Part 1:',z(u.real),'\nPart 2:',z(u.imag))]
# Day 03: 525
[r:=range,m:=[*map(str.strip,__import__('sys').stdin)],R:=len(m),C:=len(m[0]),q:=0,x:=r(-1,2),A:=set(),[[n:=set(),[[k:=v,[[k:=k-(k+1and'/'<m[u][k]<':'),v:=v+(v<C and'/'<m[u][v]<':')]for _ in r(C)],n.add((u,k+1,v))]for s in x for t in x if R>(u:=i+s)>=0and C>(v:=j+t)>=0and'/'<m[u][v]<':'],A:=A|n,0if len(n)!=2or'*'!=T else[y:=n.pop(),z:=n.pop(),q:=q+int(m[y[0]][y[1]:y[2]])*int(m[z[0]][z[1]:z[2]])]]for i in r(R)for j in r(C)if(T:=m[i][j])not in'0123456789.'],print('Part 1:',sum(int(m[i][j:k])for i,j,k in A),'\nPart 2:',q)]
# Day 04: 285
[c:=[[x:=l.split('|'),len({*map(int,x[1].split())}&{*map(int,x[0].split(':')[1].split())})][1]for l in __import__('sys').stdin],d:=[1]*len(c),[d.__setitem__(u:=i+j+1,d[u]+d[i])for i in range(len(c))for j in range(c[i])],print('Part 1:',sum(2**s*(s>0)//2for s in c),'\nPart 2:',sum(d))]
# Day 05: 698
[S:=str.split,A:=list.append,I:=__import__('sys').stdin.readline,c:=lambda s:[x:=[],[[u:=[],[[A(x,(max(a+p-q,p),min(b+p-q,p+r-1))),A(u,(max(a,q),min(b,q+r-1)))]for p,q,r in d if(a<q+r)*(b>=q)],0if u else[A(x,(a,b)),A(u,x[-1])],A(x,(a,u[0][0]-1)),u.insert(0,x[-1]),A(x,(u[-1][1]+1,b)),A(u,x[-1]),[A(x,(e[1]+1,f[0]-1))for e,f in zip(u,u[1:])]]for a,b in s],[(a,b)for a,b in x if a<=b]][2],s:=[s:=[*map(lambda x:[int(x)]*2,S(S(I(),':')[1]))],[[t:=s[2*i][0],t+s[2*i+1][0]-1]for i in range(len(s)//2)]],I(),[[I(),d:=[1],[(A(d,[*map(int,S(I()))])if not d or d[-1]else 0)for i in d],d:=d[1:-1],d.sort(key=lambda x:x[1]),s:=[*map(c,s)]]for _ in'.'*7],print('Part 1:',min(s[0])[0],'\nPart 2:',min(s[1])[0])]
# Day 06: 185
[f:=1,l:=[input().split()[1:]for _ in'..'],g:=lambda a,b:a-1-2*int((a-(a*a-4*b)**.5)/2),[f:=f*g(*map(int,i))for i in zip(*l)],print('Part 1:',f,'\nPart 2:',g(*map(int,map(''.join,l))))]
# Day 07: 349
[m:=dict(zip('TJQKA',':;<=>')),d:=[*map(str.split,(I:=__import__)('sys').stdin)],s:=lambda t:sum((i+1)*int(e[1])for i,e in enumerate(sorted(d,key=lambda c:max((lambda f:[max(f),-len(f)])(I('collections').Counter(c[0].replace(t,i)).values())for i in c[0])+[m.get(i,i)for i in c[0]]))),print('Part 1:',s('@')),m:={**m,'J':'1'},print('Part 2:',s('J'))]
# Day 08: 328
[I:=__import__,m:=input().strip(),input(),g:=dict(((n:=I('re').findall('\w+',l))[0],n[1:])for l in I('sys').stdin),d:=lambda p,s:[[p:=g[p][i>'L']for i in m],len(m)+(0if'Z'*s==p[3-s:]else d(p,s))][1],print('Part 1:',d('AAA',3),'\nPart 2:',I('functools').reduce(lambda x,y:x*y//I('math').gcd(x,y),[d(i,1)for i in g if'A'==i[2]]))]
# Day 09: 197
print('Part 1:',sum((M:=map)(E:=lambda l:l[-1]+E([b-a for a,b in zip(l,l[1:])])if l else 0,L:=[*M(lambda x:[*M(int,x.split())],__import__('sys').stdin)])),'\nPart 2:',sum(M(lambda x:E(x[::-1]),L)))
# Day 10: 792
[x:=range,b:=[*map(str.strip,__import__('sys').stdin)],m:=[[A:='@']*(C:=2*len(b[0])+1)],[m.extend([[*(A+A.join(l)+A)],m[0]])for l in b],R:=len(m),Z:=x(X:=R*C),d:=[-2]*X,S:=d.__setitem__,g:=[[]for _ in Z],q:=[(u,0)for u in Z if'S'==m[u//C][u%C]],s:=[(0,0)],f:=lambda a,b:(g[a].append(b),g[b].append(a)),[[t:=m[u//C][u%C],f(u,u-C)if t in'S|LJ'else 0,f(u,u+C)if t in'S|7F'else 0,f(u,u+1)if t in'S-LF'else 0,f(u,u-1)if t in'S-J7'else 0]for u in Z],[[t:=q[0][1],u:=q.pop(0)[0],[S(u,t),q.extend((v,t+1)for v in g[u])]if d[u]<0else 0]for _ in x(X*4)if q],[[r:=s[-1][0],c:=s.pop()[1],[S(C*r+c,0),s.extend((r+p,c+z)for p,z in((0,-1),(0,1),(-1,0),(1,0))if R>r+p>-1<c+z<C)]if 0>d[C*r+c]else 0]for _ in x(X*4)if s],print('Part 1:',max(d)//2,'\nPart 2:',sum(0>d[C*r+c]for r in x(1,R,2)for c in x(1,C,2)))]
# Day 11: 398
[A:=list.append,m:=[*map(str.strip,__import__('sys').stdin)],x:=range,f:=lambda e:[p:=[0],q:=[0],G:=[],r:={*x(R:=len(m))},c:={*x(C:=len(m[0]))},[[r:=r-{i},c:=c-{j},A(G,(i+1,j+1))]for i in x(R)for j in x(C)if'.'>m[i][j]],[A(l,l[i]+1+e*(i in h))for l,h,H in((p,r,R),(q,c,C))for i in x(H)],sum(abs(p[a]-p[c])+abs(q[b]-q[d])for a,b in G for c,d in G)//2][7],print('Part 1:',f(1),'\nPart 2:',f(999999))]
# Day 12: 467
[L:=len,g:=lambda l,p:[m:={},f:=lambda i,j,c:m[t]if(t:=(i,j,c))in m else(c==p[-1])*(L(p)-1==j)|(c<1)*(j==L(p))if i==L(l)else[r:=(f(i+1,j,c+1)if l[i]in'?#'else 0)+(f(i+1,j,0)if(k:=l[i]in'?.')*(c<1)else 0)+(f(i+1,j+1,0)if k*c*(j<L(p))and(p[j]==c)else 0),m.update({t:r}),r][2],f(0,0,0)][2],a:=sum(complex(g((d:=l.split())[0],p:=[*map(int,d[1].split(','))]),g('?'.join(5*[d[0]]),5*p))for l in __import__('sys').stdin),print('Part 1:',int(a.real),'\nPart 2:',int(a.imag))]
# Day 13: 313
print('Part 1:',int((u:=sum(complex((s:=lambda g,d=0:[0,*(i for i in range(len(g[0]))if sum(a!=b for r in g for a,b in zip(r[i-1::-1],r[i:]))==d)][-1])(g:=l.split('\n'))+100*s(h:=[*zip(*g)]),s(g,1)+100*s(h,1))for l in''.join(__import__('sys').stdin).replace('\r','').split('\n\n'))).real),'\nPart 2:',int(u.imag))
# Day 14: 559
[m:=[*map(list,map(str.strip,__import__('sys').stdin))],L:=len,R:=L(m),C:=L(m[0]),x:=range,w:=lambda m:[[[o:=1,[(m[s].__setitem__(c,'O'),m[s+1].__setitem__(c,'.'))for s in x(r)[::-1]if(o:=(m[s][c]=='.')*o)]]for c in x(C)for r in x(R)if'.'<m[r][c]],m][1],p:=lambda m:sum((R-i)*m[i].count('O')for i in x(R)),t:=lambda m:[[m[i][j]for i in x(R)[::-1]]for j in x(C)],y:=lambda m:t(w(t(w(t(w(t(w(m)))))))),h:=[],V:=[0],print('Part 1:',p(w(m))),[[h:=h+[e],V.append(p(m))]for _ in V if(e:=str(m:=y(m)))not in h],print('Part 2:',V[(10**9-(z:=h.index(e)))%(L(h)-z)+z])]
# Day 15: 384
[r:=range,u:=lambda x:[h:=0,[h:=(h+ord(i))*17%256for i in x],h][2],s:=input().split(','),b:=[[]for _ in r(256)],m:={},[[v:=t.split('='),x:=v[0],0if x in m else b[u(x)].append(x),m:={**m,x:int(v[1])}]if'='in t else(m.pop(x),b[u(x)].remove(x))if(x:=t[:-1])in m else 0for t in s],print('Part 1:',sum(map(u,s)),'\nPart 2:',sum((i+1)*(j+1)*m[b[i][j]]for i in r(256)for j in r(len(b[i]))))]
# Day 16: 560
[b:=[],R:=len(m:=[*map(str.strip,__import__('sys').stdin)]),C:=len(m[0]),f:=lambda i,j:((i,j+1),(i-1,j),(i,j-1),(i+1,j)),[b.extend(((0,i,3),(R-1,i,1)))for i in range(C)],[b.extend(((i,0,0),(i,C-1,2)))for i in range(R)],S:=lambda t:[s:=[t],e:=[0]*R*C,v:={1},[[k:=s.pop(),i:=k[0],j:=k[1],z:=k[2],[[v.add(k),e.__setitem__(i*C+j,1),s.extend((*f(i,j)[y],y)for y in([3-z],([z],(0,2))[z%2],[z],[z^1],((1,3),[z])[z%2])[ord(m[i][j])%12%8])]if(C>j>-1<i<R)*(k not in v)else 0]]if s else 0for _ in'.'*4*R*C],sum(e)][4],print('Part 1:',S((0,)*3),'\nPart 2:',max(map(S,b)))]
# Day 17: 582
[P:=(H:=(S:=__import__)('heapq')).heappush,G:=lambda L,U:[F:=range(4),D:=[0]*4+[1e9]*4*R*(C:=len(m[0])),K:=((0,1),(-1,0),(0,-1),(1,0)),Z:=((1,3),(0,2))*2,Q:=[],[P(Q,(0,s))for s in F],[[E:=Q[0][0],T:=H.heappop(Q)[1],r:=T//4//C,c:=T//4%C,z:=T%4,[[a:=r,b:=c,x:=K[i][0],y:=K[i][1],I:=0,[[a:=a+x,b:=b+y,[I:=I+int(m[a][b]),[D.__setitem__(t,N),P(Q,(N,t))]if L<k+2and(N:=E+I)<D[(t:=4*C*a+4*b+i)]else 0]if(C>b>-1<a<R)else 0]for k in range(U)]]for i in Z[z]if E==D[T]]]for _ in D*U if Q],min(D[-8:])][7],R:=len(m:=[*map(str.strip,S('sys').stdin)]),print('Part 1:',G(1,3),'\nPart 2:',G(4,10))]
# Day 18: 306
[I:=int,a:=[],b:=[],[[c:=(z:=l.split())[2],a:=a+[(z[0],I(z[1]))],b:=b+[('RDLU'[I(c[7])],I(c[2:7],16))]]for l in __import__('sys').stdin],f:=lambda i:[r:=0,p:=2,x:=0,[[p:=p+s,x:=x+(r.conjugate()*(r:=r+s*(-1,-1j,1j,1)[ord(d)%5])).imag]for d,s in i],I((abs(x)+p)/2)][4],print('Part 1:',f(a),'\nPart 2:',f(b))]
# Day 19: 669
[m:=[*map(str.strip,(I:=__import__)('sys').stdin)],k:=m.index(''),r:={(t:=l.split('{'))[0]:[u:=t[1][:-1].split(','),[[j:=v.split(':'),c:=j[0],(ord(c[0])%25%4,c[1]<'>',int(c[2:]),j[1])][2]for v in u[:-1]]+[u[-1]]][1]for l in m[:k]},f:=lambda h,c='in':I('math').prod(b-a+1for a,b in h)*(c<'B')if c<'Z'else sum([a:=h[v][0],b:=h[v][1],A:=h[:v],B:=h[v+1:],S:=h.__setitem__,[S(v,(x:=min(z,b+1),b)),f(A+[(a,x-1)]+B,w)][1]if s*(z>a)else[S(v,(a,x:=max(a-1,z))),f(A+[(x+1,b)]+B,w)][1]if(1-s)*(z<b)else 0][5]for v,s,z,w in r[c][:-1])+f(h,r[c][-1]),print('Part 1:',sum(sum(p:=[*map(int,I('re').findall('\d+',l))])*f([[x,x]for x in p])for l in m[k+1:]),'\nPart 2:',f([[1,4000]]*4))]
# Day 20: 724
[V:=dict.values,U:=dict.__setitem__,I:=__import__,G:={},R:={},T:={},S:={},[[r:=I('re').findall('[&%\w]+',l),U(T,c:=r[0][1:],ord(r[0][0])%8%5),U(S,c,0),U(G,c,r[1:]),[U(R,d,{**R.get(d,{}),c:0})for d in r[1:]]]for l in I('sys').stdin],D:=[0],z:=D*2,t:=0,K:=[*R['rx']][0],H:={},[len(H)==len(R[K])or[t:=t+1,q:=[('roadcaster',0,0)],[(u:=Z[0],p:=Z[1],z:=z if t>1e3else(z[0]+1-p,z[1]+p),u in T and[n:=-1,[(n:=p)if T[u]==2else(U(R[u],Z[2],p),n:=1-all(V(R[u])))if T[u]else U(S,u,n:=1^S[u])if p^1else 0],n<0 or q.extend((v,n,u)for v in G[u]),u==K and[U(H,k,t)for k in R[u]if(k not in H)*R[u][k]]])for Z in q],D.append(0)]for i in D],print('Part 1:',z[0]*z[1],'\nPart 2:',I('functools').reduce(lambda x,y:x*y//I('math').gcd(x,y),V(H)))]
# Day 21: 397
[R:=len(m:=[*__import__('sys').stdin]),H:=[1],T:=(0,1),p:={R//2*(1+1j)},q:=set(),s:={T},[([(s.add(v),[(w:=v+x,m[int(w.real)%R][int(w.imag)%R]<'.'or w in s or q.add(w))for x in(-1j,1j,1,-1)])for v in p],T:=[T[1],T[0]+len(p:=q)],q:=set(),H:=H+T[1:])for _ in'.'*3*R],f:=lambda n:[v:=H[n%R::R],n:=n//R,a:=v[0],a+n*(v[1]-a)+n*(n-1)//2*(v[2]-2*v[1]+a)][3],print('Part 1:',f(64),'\nPart 2:',f(26501365))]
# Day 22: 692
[X:=range,U:=list.__setitem__,P:=__import__,L:=lambda a,c,e,b,d,f:P('itertools').product(X(a,b+1),X(c,d+1),X(e,f+1)),M:=len(S:=sorted([[*map(int,P('re').findall('\d+',l))]for l in P('sys').stdin],key=lambda x:x[2])),B:={},I:=[0]*M,N:=X(M),C:=lambda i:[J:=[*I],s:=[i],d:=-1,[(d:=d+1,[U(J,v,J[v]-1)or J[v]or s.append(v)for v in G[u]])for u in s],d][4],[[j:=S[i]]+[(U(j,2,j[2]-1),U(j,5,j[5]-1),any(i-B.get(t,i)for t in L(*j))and[U(j,k,j[k]+1)for k in(2,5)])for _ in X(j[2])]+[B:={**B,t:i}for t in L(*j)]for i in N],G:=[(s:={B[j]for*a,z in L(*S[i])if i-B.get(j:=(*a,z+1),i)},[U(I,j,I[j]+1)for j in s])[0]for i in N],print('Part 1:',sum(all(I[j]-1for j in v)for v in G),'\nPart 2:',sum(map(C,N)))]