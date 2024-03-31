// 建立簡易 service worker
self.addEventListener('install', function(event) {
    console.log('Service worker installing...');
});

self.addEventListener('activate', function(event) {
    console.log('Service worker activating...');
});

self.addEventListener('fetch', function(event) {
    // 這裡可以做 cache 相關的處理
});

// 當離線時，透過 service worker 回傳一個簡單的頁面
self.addEventListener('fetch', function(event) {
    event.respondWith(
        fetch(event.request).catch(function() {
            return new Response('You are offline.');
        })
    );
});