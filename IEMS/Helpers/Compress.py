import gzip
import io
class Compress(object):
    """Zip and unzip file"""

    def GZipStr(strContent):
        out = io.BytesIO()
        print(strContent)
        with gzip.GzipFile(fileobj=out, mode='w') as fo:
            fo.write(strContent.encode())

        bytes_obj = out.getvalue()
        return bytes_obj

    def GunzipBytesObj(bytes_obj):
        """unzip content"""
        in_ = io.BytesIO()
        in_.write(bytes_obj)
        in_.seek(0)
        with gzip.GzipFile(fileobj=in_, mode='rb') as fo:
            gunzipped_bytes_obj = fo.read()
        return gunzipped_bytes_obj.decode()




