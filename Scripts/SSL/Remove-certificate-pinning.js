/**
 * Remove certificate pinning
 */
if (Java.available) {
  console.log('[*] unpin.js - Java is available');
  Java.perform(function () {
    console.log('[*] unpin.js - Performing Java operation');
    var array_list = Java.use("java.util.ArrayList");
    var ApiClient = Java.use('com.android.org.conscrypt.TrustManagerImpl');
    ApiClient.checkTrustedRecursive.implementation = function (a1, a2, a3, a4, a5, a6) {
      var k = array_list.$new();
      return k;
    };

    /**
     * Java url proxy shit doesn't let us use proxies if they do this:
     * v6 = (HttpURLConnection)url.openConnection(Proxy.NO_PROXY);
     * java.net.URL.openConnection(java.net.Proxy)
     */
    var URL = Java.use('java.net.URL');
    URL.openConnection.overload('java.net.Proxy').implementation = function (proxyType) {
      console.log('Attempting to open connection with proxyType', proxyType);
      return this.openConnection() // (proxyType);
    };

    var HttpsURLConnection = Java.use("javax.net.ssl.HttpsURLConnection");
    HttpsURLConnection.setDefaultHostnameVerifier.implementation = function (hostnameVerifier) {
      console.log("HttpsURLConnection.setDefaultHostnameVerifier invoked");
      return null;
    };
    /* libcore/luni/src/main/java/javax/net/ssl/HttpsURLConnection.java */
    /* public void setSSLSocketFactory(SSLSocketFactory) */
    HttpsURLConnection.setSSLSocketFactory.implementation = function (SSLSocketFactory) {
      console.log("HttpsURLConnection.setSSLSocketFactory invoked");
      return null;
    };
    /* libcore/luni/src/main/java/javax/net/ssl/HttpsURLConnection.java */
    /* public void setHostnameVerifier(HostnameVerifier) */
    HttpsURLConnection.setHostnameVerifier.implementation = function (hostnameVerifier) {
      console.log("HttpsURLConnection.setHostnameVerifier invoked");
      return null;
    };

    var AppLog = Java.use('com.ss.android.common.applog.AppLog');
    AppLog.packString.implementation = function(str) {
        var out = this.packString(str);
        console.log('[packString Called]', str, 'Result:', out);
        return out;
    };

  });
}