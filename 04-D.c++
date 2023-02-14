#include <bits/stdc++.h>
using namespace std;

int main() {
	int garland_len, query_num;
	string garland;
	cin >> garland_len >> garland >> query_num;

	for (int i = 0; i < query_num; i++) {
		int max_repaint;
		char color;
		cin >> max_repaint >> color;

		int l = 0;
		int r = 0;
		int cnt = 0;
		int res = 0;
		while (l < garland_len && r < garland_len) {
		    if (garland[r] == color) cnt++;
			while (l <= r && r - l + 1 - cnt > max_repaint) {
				if (garland[l] == color) cnt--;
				l++;
			}
			res = max(res, r - l + 1);
			r++;
		}
		cout << res << endl;
	}
}
