> laravel里所有的异常处理都经过`app\Exceptions\Handler.php`, 如果需要自定义异常返回, 可以修改`render`方法;

```
<?php

namespace App\Exceptions;

use App\Helpers\ExceptionReport;
use Exception;
use Illuminate\Foundation\Exceptions\Handler as ExceptionHandler;

class Handler extends ExceptionHandler
{
    // 省略其他代码
    
    public function render($request, Exception $exception)
    {
        // 将方法拦截到自己的ExceptionReport
        $reporter = ExceptionReport::make($exception);        
        if ( $reporter->shouldReturn() )
        {
            return $reporter->report();
        }
        
        return parent::render($request, $exception);
    }
}
```

其中`app\Helpers\ExceptionReport.php`代码如下:

```
<?php

namespace App\Helpers;

use Exception;
use Illuminate\Auth\AuthenticationException;
use Symfony\Component\HttpFoundation\Response as FoundationResponse;
use Illuminate\Database\Eloquent\ModelNotFoundException;
use Illuminate\Http\Request;
use Response;

class ExceptionReport
{
    public $exception;
    public $request;
    protected $report;

    function __construct(Request $request, Exception $exception)
    {
        $this->request = $request;
        $this->exception = $exception;
    }

    public $doReport = [
        AuthenticationException::class => ['未授权', 401],
        ModelNotFoundException::class => ['模型未找到', 404]
    ];

    public function shouldReturn()
    {
        if ( ! ( $this->request->wantsJson() || $this->request->ajax() ) )
        {
            return false;
        }

        foreach ( array_keys($this->doReport) as $report)
        {
            if ( $this->exception instanceof $report )
            {
                $this->report = $report;
                return true;
            }
        }
        return false;
    }

    public static function make(Exception $e)
    {
        return new static(\request(), $e);
    }

    public function report()
    {
        $message = $this->doReport[$this->report];
        return Response::json(['code'=>$message[0], 'message'=>$message[1]]);
    }

}
```
