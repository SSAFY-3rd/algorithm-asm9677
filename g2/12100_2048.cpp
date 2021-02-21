#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int max = 0;

void func(int(*arr)[20], int n, int idx)
{
	if (idx >= 5)		
		return;

	int arr2[20][20] = { 0, };	
	memcpy(arr2, arr, sizeof(int) * 400);

	for (int i = 0; i < n; i++)
	{
		int prev = arr[i][0];
		if (max < prev)
			max = prev;
		int k = 0;
		for (int j = 1; j < n; j++)
		{
			if (max < arr[i][j])
				max = arr[i][j];
			if (arr[i][j] == 0);
			else if (arr[i][j] == prev) {
				arr[i][j] = 0;
				arr[i][k++] = prev * 2;
				if (max < prev * 2)
					max = prev * 2;
				prev = 0;
			}
			else if (arr[i][j] != prev && prev != 0)
			{
				arr[i][k++] = prev;
				prev = arr[i][j];
				arr[i][j] = 0;
			}
			else {
				prev = arr[i][j];
				arr[i][j] = 0;
			}
		}
		if (prev != 0)
			arr[i][k++] = prev;
	}

	func(arr, n, idx + 1);
	memcpy(arr, arr2, sizeof(int) * 400);

	for (int i = 0; i < n; i++)
	{
		int prev = arr[i][n - 1];
		if (max < prev)
			max = prev;
		int k = n - 1;
		for (int j = n - 2; j >= 0; j--)
		{
			if (max < arr[i][j])
				max = arr[i][j];
			if (arr[i][j] == 0);
			else if (arr[i][j] == prev) {
				arr[i][j] = 0;
				arr[i][k--] = prev * 2;
				if (max < prev * 2)
					max = prev * 2;
				prev = 0;
			}
			else if (arr[i][j] != prev && prev != 0)
			{
				arr[i][k--] = prev;
				prev = arr[i][j];
				arr[i][j] = 0;
			}
			else {
				prev = arr[i][j];
				arr[i][j] = 0;
			}
		}
		if (prev != 0)
			arr[i][k--] = prev;
	}

	func(arr, n, idx + 1);
	memcpy(arr, arr2, sizeof(int) * 400);

	for (int i = 0; i < n; i++)
	{
		int prev = arr[0][i];
		if (max < prev)
			max = prev;
		int k = 0;
		for (int j = 1; j < n; j++)
		{
			if (max < arr[j][i])
				max = arr[j][i];
			if (arr[j][i] == 0);
			else if (arr[j][i] == prev) {
				arr[j][i] = 0;
				arr[k++][i] = prev * 2;
				if (max < prev * 2)
					max = prev * 2;
				prev = 0;
			}
			else if (arr[j][i] != prev && prev != 0)
			{
				arr[k++][i] = prev;
				prev = arr[j][i];
				arr[j][i] = 0;
			}
			else {
				prev = arr[j][i];
				arr[j][i] = 0;
			}
		}
		if (prev != 0)
			arr[k++][i] = prev;
	}

	func(arr, n, idx + 1);
	memcpy(arr, arr2, sizeof(int) * 400);

	for (int i = 0; i < n; i++)
	{
		int prev = arr[n - 1][i];
		if (max < prev)
			max = prev;
		int k = n - 1;
		for (int j = n - 2; j >= 0; j--)
		{
			if (max < arr[j][i])
				max = arr[j][i];
			if (arr[j][i] == 0);
			else if (arr[j][i] == prev) {
				arr[j][i] = 0;
				arr[k--][i] = prev * 2;
				if (max < prev * 2)
					max = prev * 2;
				prev = 0;
			}
			else if (arr[j][i] != prev && prev != 0)
			{
				arr[k--][i] = prev;
				prev = arr[j][i];
				arr[j][i] = 0;
			}
			else {
				prev = arr[j][i];
				arr[j][i] = 0;
			}
		}
		if (prev != 0)
			arr[k--][i] = prev;
	}
	func(arr, n, idx + 1);
}

int main()
{
	int arr[20][20] = { 0, };
	int n = 0;
	scanf("%d", &n);

	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			scanf("%d", &arr[i][j]);

	func(arr, n, 0);

	printf("%d\n", max);
}