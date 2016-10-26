import sys
import time
import curlparse
import urllib.parse as urlparse_urllib
import urlparse as urlparse_fast
import datetime as dt


if len(sys.argv) == 1:
    print('Usage: time_urlparse_file <filename>')
    exit(0)

filename = sys.argv[1]
total_url_count = 0

total_urllib = 0
total_f = 0
total_fc = 0
total_fcb = 0

curlparse.clear_cache()
urlparse_fast.clear_cache()
urlparse_urllib.clear_cache()

start_all = time.time()
for url in open(filename, 'r'):
    url_bytes = url.encode('utf-8')
    total_url_count += 1

    start = time.time()
    urlparse_fast.urlparse(url)
    total_f += time.time() - start

    start = time.time()
    curlparse.urlparse(url)
    total_fc += time.time() - start

    start = time.time()
    curlparse.urlparse(url_bytes)
    total_fcb += time.time() - start

    start = time.time()
    urlparse_urllib.urlparse(url)
    total_urllib += time.time() - start

result_f = total_f / total_url_count
result_fc = total_fc / total_url_count
result_fcb = total_fcb / total_url_count
result_urllib = total_urllib / total_url_count
total_runtime = time.time() - start_all

print('===========')
print('Comparison:')
print('===========')
print('urllib.parse                  {:.10f}  100%'.format(result_urllib))
print('fast_urlparse (python)        {:.10f}  {:.0f}%'.format(result_f, (result_f / result_urllib) * 100))
print('fast_urlparse (cython, str)   {:.10f}  {:.0f}%'.format(result_fc, (result_fc / result_urllib) * 100))
print('fast_urlparse (cython, bytes) {:.10f}  {:.0f}%'.format(result_fcb, (result_fcb / result_urllib) * 100))
print('===========')
print('Urls: {:,}'.format(total_url_count))
print('Total time: {}\n'.format(dt.timedelta(seconds=total_runtime)))
