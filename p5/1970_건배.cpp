#include <iostream>
#include <memory.h>
using namespace std;

int dp[1001][1001];
int arr[1001];
int n;

int solve(int i, int j) {
	if (i >= j)
		return 0;

	int& ref = dp[i][j];
	if (ref != -1)
		return ref;

	ref = max(solve(i + 1, j), solve(i, j - 1));
	for (int k = i + 1; k <= j; k++) {
		if (arr[i] == arr[k])
			ref = max(ref, solve(i + 1, k - 1) + solve(k + 1, j) + 1);
	}
	return ref;
}

int main() {
	ios::sync_with_stdio(0); cout.tie(0); cin.tie(0);
	memset(dp, -1, sizeof dp);

	cin >> n;
	for (int i = 0; i < n; i++)
		cin >> arr[i];
	cout << solve(0, n - 1);
}