const solution = require('./solution');

test('input a simple array and output is 5', () => {
  expect(solution([1, 1, 3, 3, 3, 4, 5, 5, 5, 5], 2)).toBe(5);
});
