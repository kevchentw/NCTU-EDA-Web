#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <algorithm>
#include <deque>
#include <vector>
#include <queue>
#include <map>
#include <complex>
#ifdef __WINDOWS__
#define __I64d "%I64d"
#define __I64u "%I64u"
#else
#define __I64d "%lld"
#define __I64u "%llu"
#endif
#define PB push_back
#define PPB pop_back
typedef long long ll;
typedef double db;
using namespace std;
int N;
struct Node
{
	ll x,y;
	Node(){}
	Node(ll _x,ll _y)
	{
		x=_x,y=_y;
	}
	bool operator < (const Node &n)const
	{
		if(n.x==x)return n.y>y;
		else return n.x>x;
	}
}s[100010];
ll x[100010],y[100010];
int main()
{
	scanf("%d",&N);
	for(int i=0;i<N;i++)
	{
		scanf(__I64d,&s[i].x);
		scanf(__I64d,&s[i].y);
	}
	sort(s,s+N);
	for(int i=0;i<N;i++)
	{
		x[i]=s[i].x;
		y[i]=s[i].y;
	}
	int Q;
	scanf("%d",&Q);
	for(int i=0;i<Q;i++)
	{
		ll x1,x2,y1,y2;
		int cnt=0;
		scanf(__I64d,&x1);
		scanf(__I64d,&y1);
		scanf(__I64d,&x2);
		scanf(__I64d,&y2);
		int l,r;
		l=lower_bound(x,x+N,x1)-x;
		r=upper_bound(x,x+N,x2)-x-1;
		//printf(" %d %d\n",l,r);
		for(int j=l;j<=r&&j<N;)
		{
			int k=j;
			while(x[k]==x[j]&&k<N)k++;
			if(k>N)break;
			int uy=upper_bound(y+j,y+k-1,y2)-y;
			//uy--;
			int dy=lower_bound(y+j,y+k-1,y1)-y;
			if(y[uy]>y2)uy--;
			//printf("%d %d %d %d\n",j,k-1,uy,dy);
			if(uy>=dy&&(uy!=dy||(uy==dy&&y[dy]>=y1&&y[dy]<=y2)))cnt+=(uy-dy+1);
			j=k;
		}
		printf("%d\n",cnt);
	}
	
	return 0;
}

