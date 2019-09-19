**laravel事件event**

> 事件是一种常见观察者模式的应用, 可以理解为if this, then that. 在laravel事件中对应 if event then listener

`php artisan event:generate`

```
<?php
namespace App\Events;
use App\Podcast;
use App\Events\Event;
use Illuminate\Queue\SerializesModels;
class PodcastWasPurchased extends Event
{
    use SerializesModels;
    public $podcast;
	
    /**
     * Create a new event instance.
     *
     * @param  Podcast  $podcast
     * @return void
     */
    public function __construct(Podcast $podcast)
    {
        $this->podcast = $podcast;
    }
}
```

```
<?php
namespace App\Listeners;
use App\Events\PodcastWasPurchased;
use Illuminate\Queue\InteractsWithQueue;
use Illuminate\Contracts\Queue\ShouldQueue;
class EmailPurchaseConfirmation
{
    /**
     * Create the event listener.
     *
     * @return void
     */
    public function __construct()
    {
        //
    }
	
    /**
     * Handle the event.
     *
     * @param  PodcastWasPurchased  $event
     * @return void
     */
    public function handle(PodcastWasPurchased $event)
    {
        // Access the podcast using $event->podcast...
    }
}
```

> 将event和listener绑定并注册, 在`app/Providers/EventServiceProvider.php`里

```
protected $listen = [
    'App\Events\PodcastWasPurchased' => [
        'App\Listeners\EmailPurchaseConfirmation',
    ],
];
```
