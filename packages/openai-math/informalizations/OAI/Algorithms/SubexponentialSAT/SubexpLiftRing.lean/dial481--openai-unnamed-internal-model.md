---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpLiftRing.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpLiftRing.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpLiftRing.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Uniform coefficient representations for the growing-parameter argument

Every base residue has an explicit little-endian word of width
`mu * (Nat.log 2 p + 1)`. The polynomial quotient uses one such word per
basis coefficient. These bounds keep p and mu visible. Binary modular
operations below use the existing bit/list algorithms and normalize back
to the prescribed width; their counters are source-level finite events,
not a claimed Turing-machine simulation.


### `fixedBits`

 Fixed-width little-endian binary expansion. 

### `encodeBase`

 Canonical binary encoding of a base coefficient. 

### `baseCode`

 The fixed-width code also records the bounds needed for concatenation. 

### `coefficientList`

 The actual canonical quotient coordinates, in increasing degree order. 

### `encodeLambda`

 Binary storage of every quotient coefficient; no p-dependent alphabet. 

### `encodeQuartic_length`

 Degree four stays fixed while both p and mu vary. 

### `toNat_take_of_lt`

 Truncating high zero bits preserves any value already below the capacity. 

### `normalizeBits`

 Bounded list operations restore the canonical output width. 

### `addBaseRun`

 Addition of encoded residues using only the already verified binary
arithmetic, binary division, and bounded list normalization. 

### `addBaseRun_cost`

 Uniform source-event bound, with one extra modulus bit allowed. 
