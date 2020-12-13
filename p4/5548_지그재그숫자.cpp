#include <iostream>
#include <memory.h>
#include <string>
#define MOD 10000

using namespace std;

int dp[501][501][11][2][2];
int N, M;
string strNum;
int solve(int i, int mod, int prev, int dir, int f) {
	if (i == N)
		return mod == 0;

	int& ret = dp[i][mod][prev][dir][f];
	if (ret != -1)
		return ret;

	ret = 0;
	int mx = strNum[i] - '0';

	if (prev == 10) {
		ret = solve(i + 1, 0, 10, 0, 1);
		for (int l = 1, r = f ? 10 : mx + 1; l < r; l++) {			
			if (i + 1 != N)
				ret += solve(i + 1, l % M, l, 0, f || l != mx) + solve(i + 1, l % M, l, 1, f || l != mx);			
			else {
				ret += solve(i + 1, l % M, l, 0, f || l != mx);
			}
			ret %= 10000;			
		}
	}
	int l, r, v;
	if (dir == 0) 
		l = prev + 1, r = f ? 10 : mx + 1, v = 1;	
	else 
		l = f ? prev - 1 : min(mx, prev - 1), r = -1, l > r, v = -1;
	if ((v == 1 && l < r) || (v == -1 && r < l)) {
		while (l != r) {
			ret += solve(i + 1, (mod * 10 + l) % M, l, 1 - dir, f || l != mx);
			ret %= 10000;
			l += v;
		}
	}
	return ret;
}

int calc(string num) {
	memset(dp, -1, sizeof dp);
	N = num.length();
	strNum = num;

	return solve(0, 0, 10, 0, 0);
}

int main(void) {
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	string a, b;
	cin >> a >> b >> M;

	int idx = a.length() - 1;
	while (true) {
		if (a[idx] == '0') {
			a[idx] = '9';
			idx--;
		}
		else {
			a[idx] -= 1;
			break;
		}
	}
	if (a[0] == '0')
		a = a.substr(1);

	int res = calc(b) - calc(a);
	cout << (res < 0 ? res + 10000 : res) << endl;
}