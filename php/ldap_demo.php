<?php
/**
 * windows域控制器连接测试
 */

$host = 'ldap://192.168.1.10';
$port = '389';
$ds = @ldap_connect($host, $port) or die('can not connect to ldap server');

ldap_set_option($ds, LDAP_OPT_PROTOCOL_VERSION, 3);
ldap_set_option($ds, LDAP_OPT_REFERRALS, 0);

$ldap_user = 'user';
$ldap_pwd = 'passwd';

$bind = @ldap_bind($ds, $ldap_user, $ldap_pwd) or die('cant not bind to ldap server');

//$base_dn='dc=domain,dc=com', $filter='ou=*', $fields=array('dn');  //一级组织

//$base_dn='ou=xx部,dc=domain,dc=com', $filter='sAMAccountName={$ldap_user}', $fields=array('sAMAccountName','displayName'); //某组织成员

$base_dn = 'ou=xxx,ou=xxx,dc=domain,dc=com';

$filter = 'cn=*';

$fields = array('mail','displayName', 'cn');

ldap_unbind($ds);

$sr = @ldap_list($ds, $base_dn, $filter, $fields) or die ("Error in search query: ".ldap_error($ds));

$info = ldap_get_entries($ds, $sr);

echo json_encode($info, JSON_UNESCAPED_UNICODE);

ldap_close($ds);
