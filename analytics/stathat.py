import urllib
import urllib2

class StatHat(object):
    
    @static_method
    def http_post(self, path, data):
        pdata = urllib.urlencode(data)
        req = urllib2.Request('http://api.stathat.com' + path, pdata)
        resp = urllib2.urlopen(req)
        return resp.read()

    @static_method
    def post_value(self, user_key, stat_key, value, timestamp=None):
        args = {'key': stat_key, 'ukey': user_key, 'value': value}
        if timestamp is not None:
            args['t'] = timestamp
        return self.http_post('/v', args)

    @static_method
    def post_count(self, user_key, stat_key, count, timestamp=None):
        args = {'key': stat_key, 'ukey': user_key, 'count': count}
        if timestamp is not None:
            args['t'] = timestamp
        return self.http_post('/c', args)

    @static_method
    def ez_post_value(self, ezkey, stat_name, value, timestamp=None):
        args = {'ezkey': ezkey, 'stat': stat_name, 'value': value}
        if timestamp is not None:
            args['t'] = timestamp
        return self.http_post('/ez', args)

    @static_method
    def ez_post_count(self, ezkey, stat_name, count, timestamp=None):
        args = {'ezkey': ezkey, 'stat': stat_name, 'count': count}
        if timestamp is not None:
            args['t'] = timestamp
        return self.http_post('/ez', args)
