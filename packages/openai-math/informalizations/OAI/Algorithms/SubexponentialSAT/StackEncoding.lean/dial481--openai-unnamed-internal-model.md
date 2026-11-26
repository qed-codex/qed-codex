---
{
  "module": "OAI/Algorithms/SubexponentialSAT/StackEncoding.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/StackEncoding.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/StackEncoding.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed-width binary encodings of finite stack alphabets

The primary representation has no appended binary sentinel: the tape alphabet
is `Option Bool`, data bits are wrapped in `some`, and `none` is blank. Thus a
Boolean input stack can use width one and needs no initialization scan.

An explicit binary bottom-marker representation is also provided separately.
No theorem in this file assigns a Turing-machine cost to list operations.


### `BlockCode`

 An injective, positive, fixed-width code. 

### `codingWidth`

 A positive width sufficient for every label in `Fin n`, including `n = 0`. 

### `codeOfEquiv`

 Code construction from an explicitly supplied finite enumeration. 

### `chunkOfList`

 Read exactly `w` bits, using a default only outside the supplied word. 

### `readCodeOfEquiv`

 A concrete decoder: check the width, decode the binary integer, then check
that it is a label in the finite alphabet. All checks are bounded. 

### `finiteCode`

 Any finite alphabet admits such a code. The chosen enumeration is fixed
data; the actual constructor `codeOfEquiv` is computable from that data. 

### `codeOfBoolEquiv`

 A width-one code for an alphabet explicitly equivalent to Boolean bits. 

### `boolCode`

 Raw Boolean input is already encoded and needs no setup pass. 

### `encodeDataStack`

 Top-at-head concatenation of symbol blocks, with blank as the external
end marker. 

### `drop_width_eq_tail`

 Removing one complete block is the encoding of stack pop, including empty
stacks. No partial-block boundary occurs. 

### `readCodeOfEquiv_take_encode`

 Reading the first complete block recovers exactly the source stack's
optional top symbol, including the empty-stack case. 

### `tapeWord`

 Wrap data bits in `some`, reserving `none` exclusively for blank tape cells. 

### `encodeStack`

 Optional representation with a *binary* bottom marker. This representation
is separate from `encodeDataStack`, which preserves the raw input format. 
