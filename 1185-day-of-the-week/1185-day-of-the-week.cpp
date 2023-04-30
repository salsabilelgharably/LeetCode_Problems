class Solution {
public:
    string dayOfTheWeek(int day, int month, int year) {
        vector<string> dow = {"Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"};
        vector<int> months = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        auto is_leap = [](int year) { return year % 4 == 0 && (year % 100 != 0 || year % 400 == 0); };
        auto days = 0;
        for (auto y = 1971; y < year; ++y) {
            days += 365 + is_leap(y);
        }
        for (auto m = 0; m < month - 1; ++m) {
            days += months[m];
        }
        days += day + (month > 2 && is_leap(year));
        return dow[days % 7];
    }
};