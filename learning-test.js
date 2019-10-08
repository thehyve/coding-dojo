/* eslint-env mocha */
import pv from 'bio-pv'
import assert from 'assert'

describe('a newly created element', function () {
  it('has no children', function () {
    var container = document.createElement('div')
    document.body.appendChild(container)

    var numberOfChildren = container.childElementCount

    assert.strictEqual(numberOfChildren, 0)
  })
})

describe('pv', function () {
  describe('#Viewer()', function () {
    it('adds an element to the DOM', function () {
      var options = {
        width: 600,
        height: 600,
        antialias: true,
        quality: 'medium'
      }
      var container = document.createElement('div')
      document.body.appendChild(container)

      pv.Viewer(container, options)

      assert.strictEqual(container.childElementCount, 1)
    })
  })
})
