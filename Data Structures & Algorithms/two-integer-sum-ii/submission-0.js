class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {
        let i = 0;
        let j = numbers.length - 1;

        do {
            const result = numbers[i] + numbers[j];

            if (result === target) return [i + 1, j + 1];

            if (result < target) {
                i += 1;
            } else {
                j -= 1;
            }
        } while(i < j);

        return [];
    }
}
