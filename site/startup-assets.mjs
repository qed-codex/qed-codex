// Asynchronous XHR reuses immutable HTTP responses across navigations in WebKit.
export function bytes(url) {
  return new Promise((resolve, reject) => {
    const request = new XMLHttpRequest();
    request.open("GET", url);
    request.responseType = "arraybuffer";
    request.onload = () => {
      if (request.status === 200 && request.response) resolve(request.response);
      else reject(Error(`HTTP ${request.status} fetching ${url}`));
    };
    request.onerror = request.onabort = () => reject(Error("Could not load " + url));
    request.send();
  });
}
