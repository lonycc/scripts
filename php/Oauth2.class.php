<?php

class Oauth2
{
	public $REDIRECT_URL = "";
 	public $APPID = "";
 	public $SECRET = "";
 	
 	public $Code = "";
 	public $State = "";
 	public $Access_token = "";
 	
 	public $Openid = "";
 	
 	function __construct()
 	{		
 		//默认使用的appid
 		$this->APPID = '';
 		$this->SECRET = '';		
 	} 	
    
 	/**
 	 * 初始化参数。(包括微信接口参数$code、$state)
 	 * @param string $APPID
 	 * @param string $SECRET
 	 * @param string $REDIRECT_URL
 	 */
 	function init($APPID, $SECRET, $REDIRECT_URL='http://domain.com/api/wechat/test')
 	{
 		$this->REDIRECT_URL = $REDIRECT_URL;
 		$this->APPID = $APPID;
 		$this->SECRET = $SECRET;
 		
 		$this->Code = $_GET['code'];//code
 		$this->State = $_GET['state'];//state参数
 	}
 	
 	/**
 	 * 获取Code
 	 * (传递state参数)
 	 */
 	function get_code($state='1')
 	{		
 		$APPID = $this->APPID;
 		$redirect_uri = $this->REDIRECT_URL;
 		$url_get_code = "https://open.weixin.qq.com/connect/oauth2/authorize?appid={$APPID}&redirect_uri={$redirect_uri}&response_type=code&scope=snsapi_base&state={$state}#wechat_redirect";
 		header("Location: $url_get_code");//重定向请求微信用户信息
 	}
 	/**
 	 * 获取用户openid
 	 * @param string $redirect_uri
 	 * @param string $state 传参
 	 */
 	function get_openid()
 	{
 		$APPID = $this->APPID;
 		$SECRET = $this->SECRET;
 		$code = $this->Code;
 		
 		$url = "https://api.weixin.qq.com/sns/oauth2/access_token?appid={$APPID}&secret={$SECRET}&code={$code}&grant_type=authorization_code";
		$content = file_get_contents($url);
		$o = json_decode($content,true);
		$this->Openid = $o['openid'];
		return $o['openid'];
 	}
 	
 	/**
 	 * 授权获取code
 	 */
 	function get_code_by_authorize($state)
 	{
 		$APPID = $this->APPID;
 		$redirect_uri = $this->REDIRECT_URL;
 		$url_get_code = "https://open.weixin.qq.com/connect/oauth2/authorize?appid={$APPID}&redirect_uri={$redirect_uri}&response_type=code&scope=snsapi_userinfo&state={$state}#wechat_redirect";
 		header("Location: $url_get_code");//重定向请求微信用户信息		
 	}
 	
 	/**
 	 * 授权获取用户信息
 	 */
 	function get_userinfo_by_authorize()
 	{
 		$APPID = $this->APPID;
 		$SECRET = $this->SECRET;
 		$code = $this->Code;
 			
 		$url = "https://api.weixin.qq.com/sns/oauth2/access_token?appid={$APPID}&secret={$SECRET}&code={$code}&grant_type=authorization_code";
 		$content = file_get_contents($url);
 		$o = json_decode($content,true);
 		$openid = $o['openid'];
 		$access_token = $o['access_token'];
 		
 		$url2 = "https://api.weixin.qq.com/sns/userinfo?access_token={$access_token}&openid={$openid}&lang=zh_CN";
 		$content2 = file_get_contents($url2);
 		$o2 = json_decode($content2,true);//微信获取用户信息
 		
 		//处理昵称里的特殊字符
 		$str_nickname = substr($content2,strpos($content2,",")+1);
 		$str_nickname = substr($str_nickname,12,strpos($str_nickname,",")-13);
 		
 		$data = array('nickname'=>'','heading'=>'');
 		$data['nickname'] = base64_encode($str_nickname);
 		$data['headimgurl'] = $o2['headimgurl'];
 		
 		return $data;
 	}
 	
}

//code 微信接口参数(必须)
$code = @$_GET['code'];
//state微信接口参数(不需传参则不用), 若传参可考虑规则: 'act'.'arg1'.'add'.'arg2'
$state = @$_GET['state'];

$appid = '';
$secret = '';
$redirect_url = '';

$oauth = new Oauth2();
$oauth->init($appid, $secret, $redirect_url);

if ( empty($code) )
{
    //获取code, 会重定向到当前页. 若需传参, 使用$state变量传参
    $oauth->get_code_by_authorize($state);
    //$oauth->get_code($state); //将会重定向到生成code的页面, 仅当需要获取openid时执行该操作
}
$data = $oauth->get_userinfo_by_authorize();
$openid = $oauth->get_openid();

echo '</br>welcome test!';
echo '</br>nickname: '.$data['nickname'];
echo '</br>headimgurl: '.$data['headimgurl'];
