---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashCandidateProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashCandidateProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashCandidateProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

### `core`

 The original argmin bank occupies ports 0 through 8. Port 9 is the
persistent current candidate and port 10 is preserving-copy scratch. 

### `load`

 One bounded current-record load. The entire family is never an input. 

### `loadProgram`

 Actual fixed finite table for one candidate load, suitable for relocation
into the selector bank. Its time is polynomial in one retained candidate. 

### `load_prefix_space`

 Every source prefix, including parser and copy microsteps, counts all
stacks. This local estimate is independent of the number of candidates. 

### `normalize_digit_runs`

 The existing fixed addition-and-reduction table also canonicalizes an
arbitrary word: its second summand is the empty representation of zero. 

### `state`

 Ports 0..7 are the existing modular arithmetic bank. The remaining
ports hold unread bits, the accumulated normalized payload and take scratch. 

### `command`

 Normalization scans one retained payload. It has polynomial bit time;
therefore the local all-stack prefix rule applies to every invocation. 

### `normalize_eval`

 Complete current-candidate canonicalization. The modulus and all digits
are ordinary bit words; scalar division, truncation and copies are charged. 

### `state`

 The retained modulus is port3; the binary depth is port2. Ports0,4,5
are scratch and port1 is the current framed counter under construction. 

### `command`

 Initialization adds the list/frame terminators; finalization adds the
leading list marker and clears the exhausted binary depth word. 

### `loader_eval`

 Loading changes just the candidate payload port, with all other leaf
stacks retained. The parser's bounded singleton queue is cleared. 

### `prepare_eval`

 The concrete preparation wrapper preserves every stack except the next
candidate payload; in particular incumbent, history, counter and parameters. 

### `globalCall`

 The global call uses the frozen80-register/1220-stack ABI embedding. 
