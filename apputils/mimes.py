#!/usr/bin/env python

# A collection of mimetypes to help with parsing and correctly handling/sending content
# based on their extensions.

__all__ = ['get_mimes', 'get_extensions']

_mimetypes = {
	'hqx':		['application/mac-binhex40'],
	'cpt':		['application/mac-compactpro'],
	'csv':		['text/x-comma-separated-values', 'text/comma-separated-values', 'application/octet-stream', 'application/vnd.ms-excel', 'text/csv', 'application/csv', 'application/excel', 'application/vnd.msexcel'],
	'bin':		['application/macbinary'],
	'dms':		['application/octet-stream'],
	'lha':		['application/octet-stream'],
	'lzh':		['application/octet-stream'],
	'exe':		['application/octet-stream'],
	'class':	['application/octet-stream'],
	'psd':		['application/x-photoshop'],
	'so':		['application/octet-stream'],
	'sea':		['application/octet-stream'],
	'dll':		['application/octet-stream'],
	'oda':		['application/oda'],
	'pdf':		['application/pdf', 'application/x-download'],
	'ai':		['application/postscript'],
	'eps':		['application/postscript'],
	'ps':		['application/postscript'],
	'smi':		['application/smil'],
	'smil':		['application/smil'],
	'mif':		['application/vnd.mif'],
	'xls':		['application/excel', 'application/vnd.ms-excel', 'application/msexcel'],
	'ppt':		['application/powerpoint', 'application/vnd.ms-powerpoint'],
	'wbxml':	['application/wbxml'],
	'wmlc':		['application/wmlc'],
	'dcr':		['application/x-director'],
	'dir':		['application/x-director'],
	'dxr':		['application/x-director'],
	'dvi':		['application/x-dvi'],
	'gtar':		['application/x-gtar'],
	'gz':		['application/x-gzip'],
	'php':		['application/x-httpd-php'],
	'php4':		['application/x-httpd-php'],
	'php3':		['application/x-httpd-php'],
	'phtml':	['application/x-httpd-php'],
	'phps':		['application/x-httpd-php-source'],
	'js':		['application/x-javascript'],
	'swf':		['application/x-shockwave-flash'],
	'sit':		['application/x-stuffit'],
	'tar':		['application/x-tar'],
	'tgz':		['application/x-tar'],
	'json':     ['application/json'],
	'xhtml':	['application/xhtml+xml'],
	'xht':		['application/xhtml+xml'],
	'zip':  	['application/x-zip', 'application/zip', 'application/x-zip-compressed'],
	'mid':		['audio/midi'],
	'midi':		['audio/midi'],
	'mpga':		['audio/mpeg'],
	'mp2':		['audio/mpeg'],
	'mp3':		['audio/mpeg', 'audio/mpg'],
	'aif':		['audio/x-aiff'],
	'aiff':		['audio/x-aiff'],
	'aifc':		['audio/x-aiff'],
	'ram':		['audio/x-pn-realaudio'],
	'rm':		['audio/x-pn-realaudio'],
	'rpm':		['audio/x-pn-realaudio-plugin'],
	'ra':		['audio/x-realaudio'],
	'rv':		['video/vnd.rn-realvideo'],
	'wav':		['audio/x-wav'],
	'bmp':		['image/bmp'],
	'gif':		['image/gif'],
	'jpeg':		['image/jpeg', 'image/pjpeg'],
	'jpg':		['image/jpeg', 'image/pjpeg'],
	'jpe':		['image/jpeg', 'image/pjpeg'],
	'png':		['image/png',  'image/x-png'],
	'tiff':		['image/tiff'],
	'tif':		['image/tiff'],
	'css':		['text/css'],
	'html':		['text/html'],
	'htm':		['text/html'],
	'shtml':	['text/html'],
	'txt':		['text/plain'],
	'text':		['text/plain'],
	'log':		['text/plain', 'text/x-log'],
	'rtx':		['text/richtext'],
	'rtf':		['text/rtf'],
	'xml':		['text/xml'],
	'xsl':		['text/xml'],
	'mpeg':		['video/mpeg'],
	'mpg':		['video/mpeg'],
	'mpe':		['video/mpeg'],
	'qt':		['video/quicktime'],
	'mov':		['video/quicktime'],
	'avi':		['video/x-msvideo'],
	'movie':	['video/x-sgi-movie'],
	'doc':		['application/msword'],
	'docx':		['application/vnd.openxmlformats-officedocument.wordprocessingml.document'],
	'xlsx':		['application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'],
	'word':		['application/msword', 'application/octet-stream'],
	'xl':		['application/excel'],
	'eml':		['message/rfc822']
};


def get_mimes(extension=None):
    """Returns the mimetypes for the given extension"""   
    return _mimetypes.get(extension) if extension else None

def get_extensions(mimetype=None):
    """Returns possible extensions for the given mimetype"""
    exts = []
    for ext in _mimetypes:
        if mimetype in _mimetypes[ext]:            
            exts.append(ext)
    return exts
