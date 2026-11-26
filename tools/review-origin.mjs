// Browser review checks run on loopback or this project's Pages previews.
export function reviewOrigin(address) {
  const url = new URL(address);
  const loopback = url.protocol === "http:" && ["localhost","127.0.0.1","[::1]"].includes(url.hostname);
  const preview = url.protocol === "https:" && /^[a-z0-9-]+\.qed-codex\.pages\.dev$/.test(url.hostname);
  if (!loopback && !preview) throw Error("Expected a local or project preview.");
  return url.origin;
}
