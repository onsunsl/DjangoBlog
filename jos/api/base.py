# -*- coding: utf-8 -*-
try: import httplib
except ImportError:
    import http.client as httplib
import urllib
import time
import hashlib
import json
import jd
import itertools
import mimetypes

'''
����һЩϵͳ����
'''

P_APPKEY = "app_key"
P_API = "method"
P_ACCESS_TOKEN = "access_token"
P_VERSION = "v"
P_FORMAT = "format"
P_TIMESTAMP = "timestamp"
P_SIGN = "sign"
P_JSON_PARAM_KEY = "360buy_param_json"

P_CODE = 'code'
P_SUB_CODE = 'sub_code'
P_MSG = 'msg'
P_SUB_MSG = 'sub_msg'


N_REST = '/routerjson'

def sign(secret, parameters):
    #===========================================================================
    # '''ǩ������
    # @param secret: ǩ����Ҫ����Կ
    # @param parameters: ֧���ֵ��string����
    # '''
    #===========================================================================
    # ���parameters ���ֵ���Ļ�
    if hasattr(parameters, "items"):
        keys = parameters.keys()
        keys.sort()
        
        parameters = "%s%s%s" % (secret,
            str().join('%s%s' % (key, parameters[key]) for key in keys),
            secret)
    sign = hashlib.md5(parameters).hexdigest().upper()
    return sign

def mixStr(pstr):
    if(isinstance(pstr, str)):
        return pstr
    elif(isinstance(pstr, unicode)):
        return pstr.encode('utf-8')
    else:
        return str(pstr)
    
class FileItem(object):
    def __init__(self,filename=None,content=None):
        self.filename = filename
        self.content = content

class MultiPartForm(object):
    """Accumulate the data to be used when posting a form."""

    def __init__(self):
        self.form_fields = []
        self.files = []
        self.boundary = "PYTHON_SDK_BOUNDARY"
        return
    
    def get_content_type(self):
        return 'multipart/form-data; boundary=%s' % self.boundary

    def add_field(self, name, value):
        """Add a simple field to the form data."""
        self.form_fields.append((name, str(value)))
        return

    def add_file(self, fieldname, filename, fileHandle, mimetype=None):
        """Add a file to be uploaded."""
        body = fileHandle.read()
        if mimetype is None:
            mimetype = mimetypes.guess_type(filename)[0] or 'application/octet-stream'
        self.files.append((mixStr(fieldname), mixStr(filename), mixStr(mimetype), mixStr(body)))
        return
    
    def __str__(self):
        """Return a string representing the form data, including attached files."""
        # Build a list of lists, each containing "lines" of the
        # request.  Each part is separated by a boundary string.
        # Once the list is built, return a string where each
        # line is separated by '\r\n'.  
        parts = []
        part_boundary = '--' + self.boundary
        
        # Add the form fields
        parts.extend(
            [ part_boundary,
              'Content-Disposition: form-data; name="%s"' % name,
              'Content-Type: text/plain; charset=UTF-8',
              '',
              value,
            ]
            for name, value in self.form_fields
            )
        
        # Add the files to upload
        parts.extend(
            [ part_boundary,
              'Content-Disposition: file; name="%s"; filename="%s"' % \
                 (field_name, filename),
              'Content-Type: %s' % content_type,
              'Content-Transfer-Encoding: binary',
              '',
              body,
            ]
            for field_name, filename, content_type, body in self.files
            )
        
        # Flatten the list and add closing boundary marker,
        # then return CR+LF separated data
        flattened = list(itertools.chain(*parts))
        flattened.append('--' + self.boundary + '--')
        flattened.append('')
        return '\r\n'.join(flattened)

class JdException(Exception):
    #===========================================================================
    # ҵ���쳣��
    #===========================================================================
    def __init__(self):
        self.errorcode = None
        self.message = None
        self.subcode = None
        self.submsg = None
        self.application_host = None
        self.service_host = None
    
    def __str__(self, *args, **kwargs):
        sb = "errorcode=" + mixStr(self.errorcode) +\
            " message=" + mixStr(self.message) +\
            " subcode=" + mixStr(self.subcode) +\
            " submsg=" + mixStr(self.submsg) +\
            " application_host=" + mixStr(self.application_host) +\
            " service_host=" + mixStr(self.service_host)
        return sb
       
class RequestException(Exception):
    #===========================================================================
    # ���������쳣��
    #===========================================================================
    pass

class RestApi(object):
    #===========================================================================
    # Rest api�Ļ���
    #===========================================================================
    
    def __init__(self, domain='gw.api.360buy.net', port = 80):
        #=======================================================================
        # ��ʼ������
        # Args @param domain: �������������ip
        #      @param port: ����Ķ˿�
        #=======================================================================
        self.__domain = domain
        self.__port = port
        self.__httpmethod = "POST"
        if(jd.getDefaultAppInfo()):
            self.__app_key = jd.getDefaultAppInfo().appkey
            self.__secret = jd.getDefaultAppInfo().secret
        
    def get_request_header(self):
        return {
                 'Content-type': 'application/x-www-form-urlencoded',
                 "Cache-Control": "no-cache",
                 "Connection": "Keep-Alive",
        }
        
    def set_app_info(self, appinfo):
        #=======================================================================
        # ���������app��Ϣ
        # @param appinfo: import jd
        #                 appinfo jd.appinfo(appkey,secret)
        #=======================================================================
        self.__app_key = appinfo.appkey
        self.__secret = appinfo.secret
        
    def getapiname(self):
        return ""
    
    def getMultipartParas(self):
        return [];

    def getTranslateParas(self):
        return {};
    
    def _check_requst(self):
        pass
    
    def getResponse(self, accessToken=None, version='2.0', timeout=30):
        #=======================================================================
        # ��ȡresponse���
        #=======================================================================
        connection = httplib.HTTPConnection(self.__domain, self.__port, timeout)
        sys_parameters = {
            P_APPKEY: self.__app_key,
            P_VERSION: version,
            P_API: self.getapiname(),
            P_TIMESTAMP: time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        }
        if accessToken is not None:
            sys_parameters[P_ACCESS_TOKEN] = accessToken
        application_parameter = self.getApplicationParameters()
        sys_parameters[P_JSON_PARAM_KEY] = json.dumps(application_parameter,ensure_ascii=False, default=lambda value:value.__dict__)
        sys_parameters[P_SIGN] = sign(self.__secret, sys_parameters)
        connection.connect()
        url = "http://" +self.__domain +N_REST + "?" + urllib.urlencode(sys_parameters)
        connection.request(self.__httpmethod, url)
        response = connection.getresponse();
        result = response.read()
        jsonobj = json.loads(result)
        return jsonobj
    
    
    def getApplicationParameters(self):
        application_parameter = {}
        for key, value in self.__dict__.iteritems():
            if not key.startswith("__") and not key in self.getMultipartParas() and not key.startswith("_RestApi__") and value is not None :
                if(key.startswith("_")):
                    application_parameter[key[1:]] = value
                else:
                    application_parameter[key] = value
        #��ѯ�����ֵ������һЩ�ؼ�������
        translate_parameter = self.getTranslateParas()
        for key, value in application_parameter.iteritems():
            if key in translate_parameter:
                application_parameter[translate_parameter[key]] = application_parameter[key]
                del application_parameter[key]
        return application_parameter
