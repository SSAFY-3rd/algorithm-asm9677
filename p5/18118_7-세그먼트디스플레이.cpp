#include <iostream>
#include <memory.h>
#define INF (1LL<<63)
using namespace std;
typedef long long ll;

ll _pow[20];
ll dp[11][100001];
int cnt[11][100001];
int n, m;

ll solve(int i, int j) {
	ll& value = dp[i][j];
	int& size = cnt[i][j];

	if (i == n) {
		value = j == 0 ? 0 : -INF;
		size = j == 0 ? 0 : -18;
	}

	if (value != -1)
		return value;

	value = -INF; size = -18;

	for (int k = 0; k < 10; k++) {
		int mod = (j * 10 + k) % m;
		ll v = solve(i + 1, mod);
		int s = cnt[i + 1][mod];

		v = k * _pow[s] + v; s += 1;
		if (size < s || (size == s && value < v)) {
			value = v;
			size = s;
		}
	}

	int mod = (j * 100 + 11) % m;
	ll v = solve(i + 1, mod);
	int s = cnt[i + 1][mod];

	v = 11 * _pow[s] + v; s += 2;
	if (size < s || (size == s && value < v)) {
		value = v;
		size = s;
	}
	return value;
}

int main()
{	
	ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
	
	_pow[0] = 1LL;
	for (int i = 1; i < 19; i++) {
		_pow[i] = _pow[i - 1] * 10LL;
	}

	int t;
	cin >> t;
	while (t--) {
		memset(dp, -1, sizeof dp);
		memset(cnt, -1, sizeof cnt);
		cin >> n >> m;
		ll res = solve(0, 0);
		cout << res << "\n";
	}
}