import {readFileSync} from "node:fs";

export function readDirectoryProof() {
  const read = path => JSON.parse(readFileSync(path, "utf8"));
  const proof = read("proofs/rh/proof.yml");
  proof.packages = Object.fromEntries(proof.sourceKeys.map(key => [key, read("packages/" + key + "/source.yml")]));
  return proof;
}
