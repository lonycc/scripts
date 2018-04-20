axios.get('/user?ID=12345')
    .then(function(response) {
        console.log(response);
    })
    .catch(function(err) {
        console.log(err);
    });


axios.get('/user', {
        params: {
            ID: 12345
        }
    })
    .then(function(response) {
        console.log(response);
    })
    .catch(function(err) {
        console.log(err);
    });

axios.post('/user', {
        firstName: 'Fred',
        lastName: 'Flintstone'
    })
    .then(function(response) {
        console.log(response);
    })
    .catch(function(error) {
        console.log(error);
    });
    
function getUserAccount() {
    return axios.get('/user/12345');
}

function getUserPermissions() {
    return axios.get('/user/12345/permissions');
}

// 并发请求
axios.all([getUserAccount(), getUserPermissions()])
    .then(axios.spread(function(acct, perms) {
        // 当这两个请求都完成的时候会触发这个函数，两个参数分别代表返回的结果
    }));

// 配置请求
axios({
        method: "POST",
        url: '/user',
        data: {
            firstName: "Fred",
            lastName: "Flintstone"
        }
    })
    .then(function(response) {
        console.log(response);
    })
    .catch(function(error) {
        console.log(error);
    });

// 发起一个GET请求
axios('/user/123');

// 创建一个axios实例
var instance = axios.create({
    baseURL: "https://some - domain.com/api/",
    timeout: 1000,
    headers: { 'X-Custom-Header': 'foobar' }
});
instance.get('/user', {timeout: 5000});

// 全局默认配置
axios.defaults.baseURL = 'http://api.exmple.com';
axios.defaults.headers.common['Authorization'] = AUTH_TOKEN;
axios.defaults.headers.post['content-Type'] = 'appliction/x-www-form-urlencoded';

// 添加一个请求拦截器
axios.interceptors.request.use(function(config) {
    //在请求发出之前进行一些操作
    return config;
}, function(err) {
    // 处理请求错误
    return Promise.reject(error);
});

// 添加一个响应拦截器
axios.interceptors.response.use(function(res) {
    // 在这里对返回的数据进行处理
    return res;
}, function(err) {
    // 处理响应错误
    return Promise.reject(error);
});

// 取消拦截器
var myInterceptor = axios.interceptor.request.use(function() { /*....*/ });
axios.interceptors.request.eject(myInterceptor);

// 给自定义的axios实例添加拦截器
var instance = axios.create();
instance.interceptors.request.use(function() {});

// 通过 cancel token 取消请求
var CancelToken = axios.CancelToken;
var source = CancelToken.source();

axios.get('/user/12345', {
    cancelToken: source.token
}).catch(function(thrown) {
    if (axios.isCancel(thrown)) {
        console.log('Request canceled', thrown.message);
    } else {
        // 处理错误
    }
});


// 给cancelToken构造函数传递一个executor function来创建一个cancel token
var cancelToken = axios.CancelToken;
var cancel;
axios.get('/user/12345', {
    cancelToken: new CancelToken(function(c) {
        // 这个executor函数接受一个cancel function作为参数
        cancel = c;
    });
});
//取消请求
cancel();
