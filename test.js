/* eslint-env mocha */
import { configure, shallow, mount, render } from 'enzyme'
import Adapter from 'enzyme-adapter-react-16'
import assert from 'assert'

configure({ adapter: new Adapter() })

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
