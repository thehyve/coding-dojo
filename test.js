/* eslint-env mocha */
var assert = require('assert')
describe('Array', function () {
  describe('#indexOf()', function () {
    it('should return -1 when the value is not present', function () {
      assert.strictEqual([1, 2, 3].indexOf(4), -1)
    })
  })
})
/*
TODO: use https://airbnb.io/enzyme/#shallow-rendering to assert react component.
Shall we use shallow or deep rendering?
*/
