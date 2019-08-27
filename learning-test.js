/* eslint-env mocha */
import pv from 'bio-pv'

describe('pv', function () {
  describe('#Viewer()', function () {
    it('should return -1 when the value is not present', function () {
      var options = {
        width: 600,
        height: 600,
        antialias: true,
        quality: 'medium'
      }
      // insert the viewer under the Dom element with id 'gl'.
      pv.Viewer(document.getElementById('viewer'), options)
    })
  })
})
