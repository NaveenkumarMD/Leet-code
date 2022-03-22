/**
 * @param {number} n
 * @param {number} k
 * @return {string}
 */
var getSmallestString = function (n, k) {
	let numericArr = [],
		str = '';
	// Step 1 to build string numeric array
	for (let i = 1; i <= 26; i++) {
		numericArr[i] = String.fromCharCode(96 + i);
	}
	for (let i = n; i > 0; i--) {
		// Step 2: Find nth blanks value
		let val = k - (i - 1);
		// Step 3
		if (val >= 26) {
			str = numericArr[26] + str;
			k = k - 26;
		} else {
			str = numericArr[val] + str;
			k = k - val;
		}
	}
	return str;
};