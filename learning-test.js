/* eslint-env mocha */
import pv from 'bio-pv'

describe('pv', function () {
  describe('#Viewer()', function () {
    it('should add an element to the DOM', function () {
      var options = {
        width: 600,
        height: 600,
        antialias: true,
        quality: 'medium'
      }
      var container = document.createElement('div')
      document.body.appendChild(container)
      pv.Viewer(container, options)
    })
  })
})
