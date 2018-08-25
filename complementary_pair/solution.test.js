const { solution, solution2 } = require('./solution');

test('input a simple array and K is 6', () => {
  const A = [1, 8, -3, 0, 1, 3, -2, 4, 5];
  expect(solution(6, A)).toBe(7);
  expect(solution2(6, A)).toBe(7);
});
