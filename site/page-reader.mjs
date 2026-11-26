// Called by xRead in the SQLite worker. Each response is one complete, stored gzip file.
import { Inflate } from "./vendor/pako-inflate.mjs";

function readGzip(url, expected) {
  const request = new XMLHttpRequest();
  request.open("GET", url, false);
  request.responseType = "arraybuffer";
  request.send();
  if (request.status !== 200 || !request.response) throw Error(`HTTP ${request.status} fetching ${url}`);

  return inflateAsset(request.response, expected, url);
}

export function inflateAsset(buffer, expected, url) {
  const output = new Uint8Array(expected);
  let offset = 0;
  const decoder = new Inflate({windowBits:31, chunkSize:32768});
  decoder.onData = chunk => {
    if (offset + chunk.length > expected) throw Error(`Oversized inflated asset: ${url}`);
    output.set(chunk, offset);
    offset += chunk.length;
  };
  decoder.push(new Uint8Array(buffer), true);
  if (decoder.err || !decoder.ended || offset !== expected) {
    throw Error(`Invalid gzip at ${url}: ${decoder.msg || "incomplete asset"}`);
  }
  return output;
}

export {readGzip as readAsset};
