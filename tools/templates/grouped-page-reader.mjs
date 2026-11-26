// This grouped layout addresses files by one-based piece number, SQLite reads by page number.

const pagesPerPiece = @PAGES_PER_PIECE@;
const totalPages = @TOTAL_PAGES@;
const maxPieces = 32;
const pieces = new Map();

export function readAsset(url, size) {
  if (!url.pathname.includes("/p/")) return readGzip(url,size);
  const page = Number(url.pathname.split("/").at(-1));
  const piece = Math.floor((page - 1) / pagesPerPiece);
  const within = (page - 1) % pagesPerPiece;
  let bytes = pieces.get(piece);
  if (bytes) {
    pieces.delete(piece); // Reinsert this hit at the most recently used end.
  } else {
    if (pieces.size === maxPieces) pieces.delete(pieces.keys().next().value);
    const count = Math.min(pagesPerPiece, totalPages - piece * pagesPerPiece);
    bytes = readGzip(new URL(String(piece + 1), url), size * count);
  }
  pieces.set(piece, bytes);
  return bytes.subarray(size * within, size * (within + 1));
}
