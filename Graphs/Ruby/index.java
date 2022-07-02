public void start(final httpservletrequest httpservletrequest, 
final httpservletresponse httpservletresponse) {
     final httpsession httpsession = httpservletrequest.getsession(true);
      httpsession.setattribute(auth_session_name, this); 
      final Cookie cookie = new cookie(auth_cookie_name, authtokenvalue);
      cookie.setdomain(ssorealm.sso_domain); 
      cookie.setmaxage(cookiemaxage); 
      cookie.setpath(" / ");
       httpservletresponse.addcookie(cookie);
     }

     //target:Starts new user session

     //predicted:Start a httpservletrequest. @param httpservletrequest the 
     //httpservletrequest @param httpservletresponse the httpservletresponse 

protected methodsecurityexpressionoperations createsecurityexpressionroot
( Authentication authentication, methodinvocation invocation) {
     methodsecurityexpressionroot root = new 
     methodsecurityexpressionroot( authentication);
      root.setthis(invocation.getthis());
    root.setpermissionevaluator(getpermissionevaluator()); 
    root.settrustresolver(gettrustresolver());
     root.setrolehierarchy(getrolehierarchy());
      root.setdefaultroleprefix(getdefaultroleprefix());
       return root;
     }

     //target:"Creates the root object for expression evaluation"

     //predicted:"Creates a {@link sivityoperation} for the given authentication
     // context. @param authentication the authentication authentication context
     // @param method the method to create the operation @return the operation expression"